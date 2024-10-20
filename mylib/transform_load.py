"""
Transforms and Loads data into Azure Databricks Database
"""

import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


def transform_load(
    dataset="data/georgia_commits.csv", dataset2="data/georgia_offers.csv"
):
    """Transforms and Loads data into the local Databricks database"""
    try:
        # Load CSV files
        payload = pd.read_csv(dataset, delimiter=",", skiprows=1)
        payload2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)

        # Load environment variables
        load_dotenv()
        server_hostname = os.getenv("SERVER_HOST")
        access_token = os.getenv("API_KEY")

        if not server_hostname or not access_token:
            raise ValueError(
                "Server hostname or API key missing in environment variables."
            )

        # Connect to Databricks
        with sql.connect(
            server_hostname=server_hostname,
            http_path="/sql/1.0/warehouses/2d6f41451e6394c0",
            access_token=access_token,
        ) as connection:
            cursor = connection.cursor()
            print("Connected!")

            # Check if uduGeorgiaCommitsDB table exists
            cursor.execute("SHOW TABLES FROM default LIKE 'uduGeorgiaCommits*'")
            result = cursor.fetchall()
            print(result)

            # Create table and insert data if it doesn't exist
            if not result:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS uduGeorgiaCommitsDB (
                        name STRING,
                        school STRING,
                        city STRING,
                        state STRING,
                        ranking FLOAT
                    )
                    """
                )
                print("Created table uduGeorgiaCommitsDB.")

                # Insert data into the uduGeorgiaCommitsDB table
                for _, row in payload.iterrows():
                    cursor.execute(
                        """
                        INSERT INTO uduGeorgiaCommitsDB (name, school, city, state, ranking)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        tuple(row),
                    )
                print("Inserted data into uduGeorgiaCommitsDB.")

            # Check if uduGeorgiaOffersDB table exists
            cursor.execute("SHOW TABLES FROM default LIKE 'uduGeorgiaOffers*'")
            result = cursor.fetchall()

            if not result:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS uduGeorgiaOffersDB (
                        name STRING,
                        school STRING,
                        city STRING,
                        state STRING,
                        ranking FLOAT
                    )
                    """
                )
                print("Created table uduGeorgiaOffersDB.")

                # Insert data into the uduGeorgiaOffersDB table
                for _, row in payload2.iterrows():
                    cursor.execute(
                        """
                        INSERT INTO uduGeorgiaOffersDB (name, school, city, state, ranking)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        tuple(row),
                    )
                print("Inserted data into uduGeorgiaOffersDB.")

            cursor.close()
            print("Cursor closed.")
            return "Transforming data completed successfully."

    except Exception as e:
        print(f"Error during transform_load: {e}")
        raise


if __name__ == "__main__":
    result = transform_load()
    print(result)

"""
Transforms and Loads data into Azure Databricks Database 
"""

import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into a Databricks database
def transform_load(
    dataset="data/georgia_commits.csv", dataset2="data/georgia_offers.csv"
):
    """Transforms and Loads data into the local Databricks database"""
    payload = pd.read_csv(dataset, delimiter=",", skiprows=1)
    payload2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    load_dotenv()
    server_hostname = os.getenv("SERVER_HOST")
    access_token = os.getenv("API_KEY")
    http_path = os.getenv("HTTP_PATH")
    print(
        server_hostname,
        access_token,
    )  # http_path)
    # Connect to Databricks
    with sql.connect(
        server_hostname=server_hostname,
        http_path="/sql/1.0/warehouses/2d6f41451e6394c0",
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        print("Connected!")
        # Check if the tables exist, create if not
        c.execute("SHOW TABLES FROM default LIKE 'uduGeorgiaCommits*'")
        result = c.fetchall()
        print(result)
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS uduGeorgiaCommitsDB (
                    name string,
                    school string,
                    city string,
                    state string,
                    ranking float
                )
                    """
            )
            # Insert data into the table
            for _, row in payload.iterrows():
                convert = tuple(row)
                c.execute(f"INSERT INTO uduGeorgiaCommitsDB VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'uduGeorgiaOffers*'")
        result = c.fetchall()

        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS uduGeorgiaOffersDB (
                    name string,
                    school string,
                    city string,
                    state string,
                    ranking float
                    )
                    """
            )

            for _, row in payload2.iterrows():
                convert = tuple(row)
                c.execute(f"INSERT INTO uduGeorgiaOffersDB VALUES {convert}")
        c.close()

        return "Transforming data..."


if __name__ == "__main__":
    transform_load()

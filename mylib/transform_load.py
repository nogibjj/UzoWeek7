"""
Transforms and Loads data into Azure Databricks Database 
"""

import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into a Databricks database
def load(dataset="data/georgia_commits.csv", dataset2="data/georgia_offers.csv"):
    """Transforms and Loads data into the local Databricks database"""
    payload = pd.read_csv(dataset, delimiter=",", skiprows=1)
    payload2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    load_dotenv(dotenv_path=".env")
    server_hostname = os.getenv("server_host")
    access_token = os.getenv("api_key")
    http_path = os.getenv("http_path")
    # Connect to Databricks
    with sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()

        # Check if the tables exist, create if not
        c.execute("SHOW TABLES FROM default LIKE 'uduGeorgiaCommits*'")
        result = c.fetchall()
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

        return "Success"

import os
from databricks import sql
from dotenv import load_dotenv


# Define a global variable for the log file
LOG_FILE = "query_log.md"


def edit_markdown(query, result="none"):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    load_dotenv()
    server_h = os.getenv("server_host")
    access_token = os.getenv("api_key")
    http_path = os.getenv("http_path")
    with sql.connect(
        server_host=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
    c.close()
    edit_markdown(f"{query}", result)

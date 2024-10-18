import os
from databricks import sql
from dotenv import load_dotenv


# Define a global variable for the log file
QUERY = """ 
SELECT a.state, avg(a.ranking) as average_ranking
FROM udugeorgiaoffersdb a
JOIN udugeorgiacommitsdb b
ON a.name = b.name
GROUP BY a.state
ORDER BY a.state DESC;
"""


# def edit_markdown(query, result="none"):
#     """adds to a query markdown file"""
#     # with open(QU, "a") as file:
#         file.write(f"```sql\n{query}\n```\n\n")
#         file.write(f"```response from databricks\n{result}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    load_dotenv()
    server_hostname = os.getenv("SERVER_HOST")
    access_token = os.getenv("API_KEY")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_hostname,
        http_path="/sql/1.0/warehouses/2d6f41451e6394c0",
        access_token=access_token,
    ) as connection:
        print("Connected!")
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
    c.close()
    # edit_markdown(f"{query}", result)
    print(result)


if __name__ == "__main__":
    print(QUERY)
    general_query(QUERY)
    # edit_markdown(f"{query}", result)

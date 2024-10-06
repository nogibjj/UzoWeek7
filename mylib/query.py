"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("SolCryptoDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SolCryptoDB LIMIT 5")
    print("Top 5 rows of the SolCryptoDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"

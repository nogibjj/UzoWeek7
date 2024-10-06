"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="C:\Users\uzoma\UzoSqlLiteLab\unisex_names_table.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS GroceryDB")
    c.execute(
        "CREATE TABLE unisexdb ( , name, total, male_share, female_share, gap)"
    )
    # insert
    c.executemany("INSERT INTO unisexdb VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "unisexdb.db"

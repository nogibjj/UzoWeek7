import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """Adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """Runs a query a user inputs"""
    conn = sqlite3.connect("unisexdb.db")
    cursor = conn.cursor()

    cursor.execute(query)

    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    cursor.close()
    conn.close()
    log_query(query)


# Update the `create_record` function to match the unisexdb table
def create_record(name, total, male_share, female_share, gap):
    """Create a record in unisexdb"""
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO unisexdb 
        (NAME, TOTAL, MALE_SHARE, FEMALE_SHARE, GAP) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (name, total, male_share, female_share, gap),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""INSERT INTO unisexdb 
        (NAME, TOTAL, MALE_SHARE, FEMALE_SHARE, GAP) 
        VALUES ({name}, {total}, {male_share}, {female_share}, {gap});
        """
    )


# Update the `update_record` function
def update_record(record_id, name, total, male_share, female_share, gap):
    """Update a record in unisexdb"""
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE unisexdb
        SET NAME=?, TOTAL=?, MALE_SHARE=?, FEMALE_SHARE=?, GAP=? 
        WHERE id=?
        """,
        (name, total, male_share, female_share, record_id),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""UPDATE unisexdb 
        SET NAME = {name}, TOTAL = {total},
        MALE_SHARE = {male_share}, 
        FEMALE_SHARE = {female_share}, GAP = {gap}
        WHERE id = {record_id};
        """
    )


# Update the `delete_record` function
def delete_record(record_id):
    """Delete a record from unisexdb"""
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()
    c.execute("DELETE FROM unisexdb WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    log_query(f"DELETE FROM unsisexdb WHERE id={record_id};")


# Update the `read_data` function to read from unisexdb
def read_data():
    """Read all data from unisexdb"""
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()
    c.execute("SELECT * FROM unisexdb")
    data = c.fetchall()
    log_query("SELECT * FROM unisexdb;")
    return data

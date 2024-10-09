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


# Fix the `create_record` function to match the unisexdb table structure
def create_record(ID, name, total, male_share, female_share, gap):
    """Create a record in unisexdb"""
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()

    # Insert the record into the database
    c.execute(
        """
        INSERT INTO unisexdb 
        (ID ,NAME, TOTAL, MALE_SHARE, FEMALE_SHARE, GAP) 
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (ID, name, total, male_share, female_share, gap),
    )

    conn.commit()
    conn.close()

    # Log the SQL statement for the operation
    log_query(
        f"""INSERT INTO unisexdb 
        (NAME, TOTAL, MALE_SHARE, FEMALE_SHARE, GAP) 
        VALUES ( '{ID}', {name}', {total}, {male_share}, {female_share}, {gap});
        """
    )


# Fix the `update_record` function
def update_record(ID, name, total, male_share, female_share, gap):
    """Update a record in unisexdb"""
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()

    # Update the record with the specified ID
    c.execute(
        """
        UPDATE unisexdb
        SET NAME=?, TOTAL=?, MALE_SHARE=?, FEMALE_SHARE=?, GAP=? 
        WHERE ID=?
        """,
        (ID, name, total, male_share, female_share, gap),
    )

    conn.commit()
    conn.close()

    # Log the SQL statement for the operation
    log_query(
        f"""UPDATE unisexdb 
        SET NAME = '{name}', TOTAL = {total}, MALE_SHARE = {male_share}, 
        FEMALE_SHARE = {female_share}, GAP = {gap}
        WHERE ID = {ID};
        """
    )


# Fix the `delete_record` function
def delete_record(ID):
    """Delete a record from unisexdb"""
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()

    # Delete the record with the specified ID
    c.execute("DELETE FROM unisexdb WHERE id=?", (ID,))

    conn.commit()
    conn.close()

    # Log the SQL statement for the operation
    log_query(f"DELETE FROM unisexdb WHERE id={ID};")


# Fix the `read_data` function to read from unisexdb
def read_data():
    """Read all data from unisexdb"""
    conn = sqlite3.connect("unisexdb.db")
    c = conn.cursor()

    # Select all data from the table
    c.execute("SELECT * FROM unisexdb")
    data = c.fetchall()

    # Log the SQL query
    log_query("SELECT * FROM unisexdb;")

    return data

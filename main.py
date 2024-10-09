"""
Handles CLI commands
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_record, read_data, update_record, delete_record

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
create_record(
    "7",
    "Alex",
    3000,
    0.45,
    0.55,
    0.1,
)

# Read the first 10 rows of the data
data = read_data()
print(data)

# Update a record
update_record(
    "8",
    "Taylor",
    5000,
    0.45,
    0.55,
    0.1,
)

# Delete a record
print("Deleting data...")
delete_record(9)

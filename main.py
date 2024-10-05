"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
import fire

def main(query_statements):
  print("Extracting data...")
  extract()

# Transform and load
  print("Transforming data...")
  load()

# Query
  print("Querying data...")
  query()

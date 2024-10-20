"""
Handles CLI commands
"""

import argparse
from mylib.extract import extract
from mylib.transform_load import transform_load
from mylib.query import general_query

QUERY = """ 
SELECT a.state, avg(a.ranking) as average_ranking
FROM udugeorgiaoffersdb a
JOIN udugeorgiacommitsdb b
ON a.name = b.name
GROUP BY a.state
ORDER BY a.state DESC;
"""


def handle_arguments():
    parser = argparse.ArgumentParser(description="Handle data pipeline tasks.")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("extract", help="Extract data")
    subparsers.add_parser("transform_load", help="Transform and load data")
    subparsers.add_parser("query", help="Run query")

    return parser.parse_args()


def main():
    args = handle_arguments()

    if args.command == "extract":
        print("Extracting data...")
        extract()
    elif args.command == "transform_load":
        print("Transforming data...")
        transform_load()
    elif args.command == "query":
        print("Running query...")
        general_query(QUERY)
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()

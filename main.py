"""
Handles CLI commands
"""

import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import transform_load
from mylib.query import general_query


def handle_arguments(args):
    """Create action for CL Calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=["extract", "transform_load", "query"],
    )
    args = parser.parse_args(args[:1])
    print(args.action)

    if args.action == "query":
        parser.add_argument("query")
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "transform_load":
        print("Transforming data...")
        transform_load()
    elif args.action == "query":
        general_query(args.query)

    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()

"""
Handles CLI commands
"""

import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    update_record,
    delete_record,
    create_record,
    general_query,
    read_data,
)


def handle_arguments(args):
    """add action based on initial calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "update_record",
            "delete_record",
            "create_record",
            "general_query",
            "read_data",
        ],
    )
    args = parser.parse_args(args[:1])

    if args.action == "update_record" or args.action == "create_record":
        parser.add_argument("record_id", type=int)
        parser.add_argument("name")
        parser.add_argument("total", type=int)
        parser.add_argument("female_share", type=float)
        parser.add_argument("male_share", type=float)
        parser.add_argument("gap", type=float)

    if args.action == "general_query":
        parser.add_argument("query")

    if args.action == "delete_record":
        parser.add_argument("record_id", type=int)

    return parser.parse_args(sys.argv[1:])


def main():
    """Handles all the CLI commands"""
    args = handle_arguments(sys.argv[1:])

    result = {}

    if args.action == "extract":
        print("Extracting data...")
        extract()
        result["extract"] = "/data/unisex_names_table.csv"
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
        result["transform_load"] = "unisexdb.db"
    elif args.action == "update_record":
        update_record(
            args.record_id,
            args.name,
            args.total,
            args.male_share,
            args.female_share,
            args.gap,
        )
        result["update_record"] = "Update Success"
    elif args.action == "delete_record":
        delete_record(args.record_id)
        result["delete_record"] = "Delete Success"
    elif args.action == "create_record":
        create_record(
            args.record_id,
            args.name,
            args.total,
            args.male_share,
            args.female_share,
            args.gap,
        )
        result["create_record"] = "Create Success"
    elif args.action == "general_query":
        general_query(args.query)
    elif args.action == "read_data":
        data = read_data()
        result["read_data"] = "Read Success"
        print(data)
    else:
        print(f"Unknown action: {args.action}")

    return result


if __name__ == "__main__":
    main()

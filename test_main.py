"""
Test goes here

"""

from main import main


def test_func():
    return main()


if __name__ == "__main__":
    assert test_func()["extract"] == "/data/unisex_names_table.csv"
    assert test_func()["transform_load"] == "unisexdb.db"
    assert test_func()["create_record"] == "Create Success"
    assert test_func()["read_data"] == "Read Success"
    assert test_func()["update_record"] == "Update Success"
    assert test_func()["delete_record"] == "Delete Success"

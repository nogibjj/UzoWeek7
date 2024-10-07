"""
Test goes here

"""

import subprocess


def test_load():
    """Tests the load operation."""
    result = subprocess.run(
        ["python", "main.py", "load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming and loading data..." in result.stdout


def test_query():
    """Tests the query operation."""
    query_string = "SELECT * FROM unisexdb"
    result = subprocess.run(
        ["python", "main.py", "query", query_string],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Querying data" in result.stdout


def test_create_record():
    """Tests the create_record operation."""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "create",
            # Name
            "Alex",
            # Total as int
            "1000",
            # Male share (as float, e.g., proportion of males)
            "0.55",
            # Female share (as float, e.g., proportion of females)
            "0.45",
            # Gap (difference between male and female share)
            "0.1",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Create Record" in result.stdout


def test_update_record():
    """Tests the update_record operation."""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "update",
            # Record ID (assuming we're updating the record with ID 1)
            "1",
            # Name (updated name)
            "Updated Alex",
            # Total (updated total number of people with the name)
            "1200",
            # Male share (updated proportion of males)
            "0.55",
            # Female share (updated proportion of females)
            "0.45",
            # Gap (updated difference between male and female share)
            "0.1",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Update Record" in result.stdout


def test_delete_record():
    """Tests the delete_record operation."""
    result = subprocess.run(
        ["python", "main.py", "delete", "1"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Delete Record" in result.stdout


if __name__ == "__main__":
    test_load()
    test_query()
    test_create_record()
    test_update_record()
    test_delete_record()

"""
Test script for the Georgia recruiting data pipeline.
"""

import subprocess


def test_extract():
    """Tests the extract() function."""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """Tests the transform_load() function."""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_query():
    """Tests the query() function."""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "query",
            """
            SELECT a.state, avg(a.ranking) as average_ranking
            FROM udugeorgiaoffersdb a
            JOIN udugeorgiacommitsdb b
            ON a.name = b.name
            GROUP BY a.state
            ORDER BY a.state DESC;
            """,
        ],
        capture_output=True,
        text=True,
        check=False,  # Disable the check for exit status 0 to prevent immediate failure
    )

    # Print stdout and stderr for debugging purposes
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

    # Now, you can check if the result returned an error
    assert (
        result.returncode == 0
    ), f"Command failed with return code {result.returncode}. stderr: {result.stderr}"


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_query()

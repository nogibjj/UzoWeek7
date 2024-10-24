"""
Test script for the Georgia recruiting data pipeline.
"""

from dotenv import load_dotenv
import subprocess

load_dotenv()

QUERY = """ 
SELECT a.state, avg(a.ranking) as average_ranking
FROM udugeorgiaoffersdb a
JOIN udugeorgiacommitsdb b
ON a.name = b.name
GROUP BY a.state
ORDER BY a.state DESC;
"""


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
        ["python", "main.py", "query"],
        capture_output=True,
        text=True,
        check=True,  # Enable check to ensure the process completes successfully
    )
    assert result.returncode == 0
    assert "Running query..." in result.stdout


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_query()

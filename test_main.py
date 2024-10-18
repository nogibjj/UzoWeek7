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
        ["python", "main.py", "load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_query():
    """Tests a general SQL query on both Georgia offers and commits data."""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "query",
            """
            WITH all_players AS (
                SELECT 'Offers' AS source, name, school, city, state, ranking
                FROM georgia_offers
                UNION ALL
                SELECT 'Commits' AS source, name, school, city, state, ranking
                FROM georgia_commits
            )

            SELECT state, COUNT(*) AS total_players, AVG(ranking) AS avg_ranking
            FROM all_players
            GROUP BY state
            ORDER BY total_players DESC;
            """,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "state" in result.stdout
    assert "total_players" in result.stdout
    assert "avg_ranking" in result.stdout


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_query()

"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

Unisex names  dataset
"""

import requests


def extract(
    url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/unisex-names/unisex_names_table.csv",
    file_path="UzoSqlLiteLab/unisex_names_table.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path

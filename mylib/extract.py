"""
Extract a dataset from a URL like Kaggle or data.gov. (JSON OR CSV)

Unisex names  dataset
"""

import os
import requests


def extract(
    url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/unisex-names/unisex_names_table.csv",
    file_path="data/unisex_names_table.csv",
    directory="data",
):
    """ "Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path

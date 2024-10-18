"""
Extract a dataset from a URL like github, kaggle or data.gov. (JSON OR CSV)

Georgia College Football Recruitment Data
"""

import os
import requests
import pandas as pd


def extract(
    url="""
    https://github.com/acgowda/cfb-recruit-net/blob/525eea9f7a803080e57cee3e8b0cc0dd319ce0d3/data/2017/georgia_commits.csv?raw=true
    """,
    url2="""
    https://github.com/acgowda/cfb-recruit-net/blob/525eea9f7a803080e57cee3e8b0cc0dd319ce0d3/data/2017/georgia_offers.csv?raw=true
    """,
    file_path="data/georgia_commits.csv",
    file_path2="data/georgia_offers.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    with requests.get(url2) as r:
        with open(file_path2, "a") as f:
            f.write(r.text)
    df = pd.read_csv(file_path)
    df_2 = pd.read_csv(file_path2)

    df_subset = df.head(50)
    df_subset2 = df_2.head(50)

    df_subset.to_csv(file_path, index=False)
    df_subset2.to_csv(file_path2, index=False)
    return file_path, file_path2


if __name__ == "__main__":
    extract()

from setuptools import setup, find_packages

# etl script needs to output correctly

setup(
    name="ETLpipelineUzoUwaz",
    version="0.1.0",
    description="ETLpipline",
    author="Uzoma Uwazurike",
    author_email="uzomauwazurike12@gmail.com",
    packages=find_packages(),
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)

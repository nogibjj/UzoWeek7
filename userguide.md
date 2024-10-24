# ETL-Query Script User Guide

## Overview

The ETL-Query script is a command-line interface (CLI) tool that performs Extract, Transform, Load (ETL) operations and executes general queries. This guide provides instructions on how to use the script effectively.

## Startup 
To access the cli command tool you would need to run setup.py by typing:

```bash
python setup.py develop
```
Without this your command line tools will not work. 

## Usage

### Running the Script

To run the ETL-Query script, use the following command:

```bash
etl_query <action> 
```

### Available Actions

The script supports the following actions:

- `extract`: Extract data
- `transform_load`: Transform and load data
- `query`: Execute a general query

## Example

### Extract Data

```bash
etl_query transform_load
```

This command will transform the data. If it works you should see a "Transforming Data..." output. 


### Executing a Query

```bash
etl_query general_query <query>
```

 - Don't forget : (Replace `<query>` with the specific query you want to execute) If you want to make things fancy using the SQL to create your queries directly from the command line!

## Note! 

- Be sure to have required dependencies installed or this will not work. 
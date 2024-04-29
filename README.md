# Earthquakes Data (WIP)

This project revolves around mastering the extraction of data from external sources, like APIs or web scraping, and storing it for further processing. Starting with backing up extracted data into a CSV file, ensuring original data is safe in case anything unexpected occurs. Then, using Python and psycopg2, rows of date will be reading from CSV and then insert into a PostgresSQL database.

We'll start by backing up this extracted data into CSV files, ensuring we have a safety net in case anything unexpected occurs. Then, using Python and psycopg2, we'll seamlessly insert this data into a PostgreSQL database.

## Tech Stacks

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white) ![Dbeaver](https://img.shields.io/badge/DBeaver-382923.svg?style=for-the-badge&logo=DBeaver&logoColor=white)

## Learning Goals:

- Data Extraction: Dive into the world of data extraction, pulling information from external sources such as APIs and web scraping methods.
- Data Backup: Prioritize data safety by storing the extracted information in CSV files as a precautionary measure.
- Database Integration: Gaining practical experience in integrating Python with PostgreSQL using psycopg2 to efficiently insert extracted data into a relational database, learning database management skills along the way.
- Access and Query: Once stored, effortlessly access the data through a database GUI or terminal interface. Practice writing and executing SQL queries to explore, manipulate, and retrieve the data of interest.

## What I learned from this so far?

1. This marks my first time encounter with handling large datasets. Inititally, I attempted to loop through the CSV data and API data to filter out any existing entries. I noticed a significant slowdown in processing speed. I realized that both CSV and API data were in `tuple` structure, this means I was looping through both datasets, resulting in a time complexity of `O(n^2)`. Realizing the root cause, I switched to using `set` data strcuture for codes. This allows for `O(1)` lookup and improved the processing speed.
   - `get_existing_db_codes` under `utils/db_connect.py` and `get_existing_csv_codes` under `utils/handle_csv.py`
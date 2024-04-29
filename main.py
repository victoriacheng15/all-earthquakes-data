import logging
from sys import argv
from utils.db_connect import Postgres
from utils.get_api_data import get_earthquakes_data
from utils.handle_csv import setup_csv, get_existing_csv_codes, append_data_to_csv, get_all_csv_data


def main(action):
    logging.basicConfig(level=logging.INFO)
    logging.info(" ====> starting the process...")

    api_data = get_earthquakes_data()

    if action == "csv":
        setup_csv()
        codes_count_before = get_existing_csv_codes()
        logging.info(f" Total number of codes before: {len(codes_count_before)}")

        filtered_data = tuple([data for data in api_data if data["code"] not in codes_count_before])
        logging.info(f" Total number of rows to be inserted: {len(filtered_data)}")

        for data in filtered_data:
            append_data_to_csv(data)

        codes_count_after = get_existing_csv_codes()
        logging.info(f" Total number of codes after: {len(codes_count_after)}")

    elif action == "db":
        postgres = Postgres()

        try:
            conn = postgres.connect()

            db_existing_codes = postgres.get_existing_db_codes()
            logging.info(f" Total number of rows from DB before: {len(db_existing_codes)}")

            all_csv_data = get_all_csv_data()
            logging.info(f" Total number of rows from csv: {len(all_csv_data)}")

            filtered_data = tuple([data for data in all_csv_data if data["code"] not in db_existing_codes])
            logging.info(f" Total number of rows to be inserted: {len(filtered_data)}")

            for data in filtered_data:
                postgres.insert_data(data)

            db_existing_codes_after = postgres.get_existing_db_codes()
            logging.info(f" Total number of rows from DB after: {len(db_existing_codes_after)}")

        except Exception as e:
            logging.error(f"Error: {e}")
        finally:
            postgres.close()
    else:
        logging.error(f" Unknown {action}, please enter 'csv' or 'db'")
        exit(1)
    
    logging.info(" ====> the process is complete...")


if __name__ == "__main__":
    if len(argv) < 2:
        logging.error("Usage: python3 main.py <csv|db>")
        exit(1)

    action = argv[1]

    main(action)

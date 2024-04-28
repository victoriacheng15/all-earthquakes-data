import logging
from utils.db_connect import Postgres
from utils.get_api_data import get_earthquakes_data


def main():
    logging.basicConfig(level=logging.INFO)
    postgres = Postgres()

    try:
        conn = postgres.connect()
        logging.info(" ====> starting the process...")
        print()

        api_data = get_earthquakes_data()
        db_ids = postgres.get_all_db_data()

        for data in api_data:
            if data["code"] not in db_ids:
                postgres.insert_data(data)

        print()
        logging.info(" ====> the process is complete...")
        print()

    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        postgres.close()


if __name__ == "__main__":
    main()

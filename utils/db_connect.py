import os, logging
import psycopg2
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")


class Postgres:
    def __init__(self):
        self.conn = psycopg2.connect(
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            database=POSTGRES_DB,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
        )
        self.cursor = self.conn.cursor()
        self.logger = logging.getLogger(__name__)

    def connect(self):
        try:
            self.logger.info("Connecting to database...")
            return self.conn
        except Exception as e:
            self.logger.error(f"Failed to connect to database: {e}")
            return None

    def close(self):
        try:
            self.logger.info("Closing database connection...")
            self.cursor.close()
            self.conn.close()
            self.logger.info("Database connection closed.")
        except Exception as e:
            self.logger.error(f"Error while closing database connection: {e}")

    def get_existing_db_codes(self):
        self.cursor.execute("SELECT code from raw_data;")
        result = self.cursor.fetchall()
        return set([code for code, in result])

    def insert_data(self, data):
        query = """
            INSERT INTO raw_data (code, event_id, place, city, country, magnitude, latitude, longitude, depth,utc_time, url, details)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        self.cursor.execute(
            query,
            (
                data.get("code"),
                data.get("event_id"),
                data.get("place"),
                data.get("city"),
                data.get("country"),
                data.get("magnitude"),
                data.get("latitude"),
                data.get("longitude"),
                data.get("depth"),
                data.get("utc_time"),
                data.get("url"),
                data.get("details"),
            ),
        )
        self.conn.commit()

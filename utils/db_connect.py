import os, logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.sql import text

load_dotenv()
POSTGRES_DB = os.environ.get("POSTGRES_DB")


class Postgres:
    def __init__(self):
        self.engine = create_engine(POSTGRES_DB)
        self.logger = logging.getLogger(__name__)

    def connect(self):
        try:
            self.logger.info("Connecting to database...")
            return self.engine.connect()
        except Exception as e:
            self.logger.error(f"Failed to connect to database: {e}")
            return None

    def close(self):
        try:
            self.logger.info("Closing database connection...")
            self.engine.dispose()
            self.logger.info("Database connection closed.")
        except Exception as e:
            self.logger.error(f"Error while closing database connection: {e}")

    def get_all_db_data(self, connection):
        result = connection.execute(text("""SELECT id from earthquakes"""))
        return tuple(row[0] for row in result.fetchall())

    def insert_data(self, connection, data):
        query = """
            INSERT INTO earthquakes (id, place, magnitude, latitude, longitude, utc_time)
            VALUES (:id, :place, :magnitude, :latitude, :longitude, :utc_time)
        """
        self.logger.info(f" ==> inserting data: {data.get('id')} <==")
        connection.execute(text(query), data)
        connection.commit()

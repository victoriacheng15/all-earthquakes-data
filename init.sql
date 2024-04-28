CREATE TABLE IF NOT EXISTS raw_data (
  id SERIAL PRIMARY KEY,
  code VARCHAR(150) NOT NULL,
  event_id VARCHAR(150),
  place TEXT NOT NULL,
  city VARCHAR(150),
  country VARCHAR(150),
  magnitude DECIMAL(5, 1) NOT NULL,
  latitude DECIMAL(9, 6) NOT NULL,
  longitude DECIMAL(9, 6) NOT NULL,
  depth DECIMAL(10, 2) NOT NULL,
  utc_time TIMESTAMP NOT NULL,
  url TEXT,
  details TEXT
)
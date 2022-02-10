CREATE SCHEMA IF NOT EXISTS nasa_data;

CREATE TABLE IF NOT EXISTS nasa_data.asteroids(
    id serial NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    nametype TEXT NOT NULL,
    recclass TEXT NOT NULL,
    mass TEXT,
    fall TEXT NOT NULL,
    year TEXT,
    reclat TEXT,
    reclong TEXT,
    geolocation TEXT
);

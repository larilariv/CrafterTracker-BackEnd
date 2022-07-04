-- settings.sql
CREATE DATABASE crafter_tracker;
CREATE USER crafter_trackeruser WITH PASSWORD 'crafter_tracker';
GRANT ALL PRIVILEGES ON DATABASE crafter_tracker TO crafter_trackeruser;

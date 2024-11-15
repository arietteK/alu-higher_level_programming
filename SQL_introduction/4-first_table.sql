-- This script creates a table called 'first_table' in the current database.
-- The table will only be created if it does not already exist.

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

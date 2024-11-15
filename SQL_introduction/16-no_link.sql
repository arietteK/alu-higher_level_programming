-- This script lists all records from 'second_table' with a non-null 'name'.

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

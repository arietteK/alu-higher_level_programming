-- This script lists the number of records with the same score in 'second_table'.
-- It displays 'score' and the count of records labeled as 'number'.
-- The results are sorted by 'number' in descending order.

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

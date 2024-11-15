-- Query to calculate the average temperature by city and order by temperature in descending order

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

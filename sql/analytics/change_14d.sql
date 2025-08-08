--Zmiana procentowa z ostatnich 14 dni--

SELECT MIN(date) AS first_date,
       MAX(date) AS last_date,
       ROUND (100 * (MAX(price) - MIN(price)) / MIN(price),
              2) AS change_14d
FROM (
         SELECT date, price
         FROM sp500_daily
         ORDER BY date DESC
         LIMIT 14
     ) AS last_14d;

--Liczba dni ze wzrostem/spadkiem/bez zmiany--

SELECT
    SUM(CASE WHEN change_daily > 0 THEN 1 ELSE 0 END) AS up_days,
    SUM(CASE WHEN change_daily < 0 THEN 1 ELSE 0 END) AS down_days,
    SUM(CASE WHEN change_daily = 0 THEN 1 ELSE 0 END) AS without_change_days
FROM sp500_daily
WHERE change_daily IS NOT NULL;

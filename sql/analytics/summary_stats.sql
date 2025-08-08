--Statystyki dzienne--

SELECT
    count(*) AS total_days,
    round(AVG(change_daily), 2) AS avg_daily_change,
    max(change_daily) AS max_daily_change,
    min(change_daily) AS min_daily_change,
    round(AVG(price), 2) AS avg_price,
    max(date) AS last_day
FROM sp500_daily
WHERE change_daily IS NOT NULL;

--Średnia zmienność--

SELECT
    round(AVG(abs(change_daily)), 2) AS avg_volatility
FROM sp500_daily
WHERE change_daily IS NOT NULL;

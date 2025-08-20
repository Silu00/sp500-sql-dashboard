SELECT
    date_trunc('week', date) AS week,
    round(AVG(change_daily), 2) AS avg_weekly_change
FROM sp500_daily
WHERE change_daily IS NOT NULL
GROUP BY week
ORDER BY week;

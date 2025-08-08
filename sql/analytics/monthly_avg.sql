--Średnia zmiana dzienna w danych miesiącach--

SELECT
    date_trunc('month', date) AS month,
    round(AVG(change_daily), 2) AS avg_monthly_change
FROM sp500_daily
WHERE change_daily IS NOT NULL
GROUP BY month
ORDER BY month;

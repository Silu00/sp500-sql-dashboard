SELECT
    date,
    price,
    round(avg(price) OVER (
        ORDER BY date
        ROWS BETWEEN 9 PRECEDING AND CURRENT ROW
        ), 2) AS SMA_10
FROM sp500_daily
ORDER BY date;

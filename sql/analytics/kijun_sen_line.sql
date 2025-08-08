SELECT
    date,
    price,
    round((
        max(high) OVER (
            ORDER BY date
            ROWS BETWEEN 25 PRECEDING AND CURRENT ROW
            ) + min(low) OVER (
            ROWS BETWEEN 25 PRECEDING AND CURRENT ROW
            )
        ) / 2, 2) AS kijun_sen_line
FROM sp500_daily
ORDER BY date;

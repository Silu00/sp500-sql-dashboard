SELECT
    date,
    price,
    round((lag(high) OVER (ORDER BY date) +
           lag(low) OVER (ORDER BY date) +
           lag(price) OVER (ORDER BY date)) / 3, 2) AS pivot_point,

    round(2 * ((lag(high) OVER (ORDER BY date) +
                lag(low) OVER (ORDER BY date) +
                lag(price) OVER (ORDER BY date)) / 3) -
          lag(low) OVER (ORDER BY date), 2) AS resistance_first,

    round(2 * ((lag(high) OVER (ORDER BY date) +
                lag(low) OVER (ORDER BY date) +
                lag(price) OVER (ORDER BY date)) / 3) -
          lag(high) OVER (ORDER BY date), 2) AS support_first
FROM sp500_daily
ORDER BY date;

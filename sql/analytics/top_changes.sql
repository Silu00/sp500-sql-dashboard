--Największe wzrosty--

SELECT date, price, change_daily
FROM sp500_daily
WHERE change_daily IS NOT NULL
ORDER BY change_daily DESC
LIMIT 10;

--Największe spadki--

SELECT date, price, change_daily
FROM sp500_daily
WHERE change_daily IS NOT NULL
ORDER BY change_daily ASC
LIMIT 10;

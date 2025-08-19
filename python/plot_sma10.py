
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:*************@localhost:5432/postgres')

with engine.connect() as conn:
    print(pd.read_sql("SELECT version();", conn).iloc[0,0])

Table = "sp500_daily"
q = f"""
SELECT
  date::date AS date,
  price AS close,
  open,
  high,
  low,
  volume,
  change_daily AS pct_change
FROM {Table}
ORDER BY date;
"""
df = pd.read_sql(q, engine)

#Wyczyszczenie i formatowanie danych
df["date"] = pd.to_datetime(df["date"])
df = df.dropna(subset=["close"]).sort_values("date").reset_index(drop=True)

prices = pd.read_sql("SELECT * FROM sma10 ORDER BY trade_date;", engine, parse_dates = ["trade_date"])
prices = prices.set_index("trade_date")
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(prices.index, prices["price"], label="Price", color="tab:blue", linewidth=2) #Linia ceny
ax.plot(prices.index, prices["sma_10"], label="SMA(10)", color="tab:orange", linewidth=1.5, linestyle="--") #SMA

ax.set_title("S&P 500 Price with SMA(10)", fontsize=16, weight="bold")
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Price", fontsize=12)

ax.grid(True, linestyle="--", alpha=0.6)
ax.legend(fontsize=12)

plt.tight_layout()
plt.show()

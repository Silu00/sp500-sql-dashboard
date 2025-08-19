import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:***********@localhost:5432/postgres")

prices = pd.read_sql("SELECT * FROM kijun_sen ORDER BY date", engine, parse_dates=['date'])
prices = prices.set_index('date')

plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(14,7))

#Linia ceny
ax.plot(prices.index, prices["price"], label="Price", color="#4da6ff", linewidth=2.5)
ax.fill_between(prices.index, prices["price"], prices["price"].min(),
                color="#4da6ff", alpha=0.15)

#Kijun
ax.plot(prices.index, prices["kijun_sen_line"],
        label="Kijun-sen (26)", color="#ff9933", linewidth=2, linestyle="--")

#Tytuły i osie
ax.set_title("S&P 500 – Price with Kijun-sen", fontsize=18, weight="bold", pad=20)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Price", fontsize=12)

#Dodanie siatki
ax.grid(True, linestyle="--", alpha=0.3)
ax.tick_params(axis="x", rotation=45)
ax.spines["top"].set_alpha(0.0)
ax.spines["right"].set_alpha(0.0)

ax.legend(fontsize=12, loc="upper left", frameon=False)

plt.tight_layout()
plt.show()

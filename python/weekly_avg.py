import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:************@localhost:5432/postgres')

weekly = pd.read_sql("SELECT * FROM weekly_avg;", engine, parse_dates=['week'])
weekly = weekly.dropna(subset=['week'])
weekly['week'] = weekly['week'].dt.tz_localize(None)

plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(14,7))

colors = ['tab:green' if val >= 0 else 'tab:red' for val in weekly['avg_weekly_change']]

ax.bar(weekly['week'], weekly['avg_weekly_change'], color=colors, alpha=0.8, width=5)

ax.axhline(0, color='white', linewidth=1.2, linestyle='--', alpha=0.7)

ax.set_title('Średnia dzienna zmiana zmiana S&P 500(%)', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Tydzień', fontsize=12)
ax.set_ylabel('Średnia zmiana %', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(axis='x', rotation=45, labelsize=10)
ax.spines['top'].set_alpha(0.0)
ax.spines['right'].set_alpha(0.0)

plt.tight_layout()
plt.show()


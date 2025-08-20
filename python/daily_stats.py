import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:***********@localhost:5432/postgres")

stats = pd.read_sql("SELECT * FROM daily_stats;", engine)
metrics = stats.iloc[0].to_dict()

fig, axes = plt.subplots(2, 4, figsize=(16,6))
axes = axes.flatten()

def get_color(key, value):
    if "min" in key:
        return "red"
    elif "max" in key or "avg_daily_change" in key:
        return "green"
    elif "volatility" in key:
        return "orange"
    else:
        return "black"

for ax, (k, v) in zip(axes, metrics.items()):
    ax.axis("off")
    ax.set_facecolor("#f9f9f9")
    ax.add_patch(plt.Rectangle((0,0), 1, 1, transform=ax.transAxes,
                               facecolor="white", edgecolor="#cccccc", linewidth=1))
    ax.text(0.5, 0.6, f"{v}", fontsize=18, weight="bold",
            color=get_color(k, v), ha="center", va="center")
    ax.text(0.5, 0.3, k.replace("_", " ").title(),
            fontsize=10, color="#555555", ha="center", va="center")

for ax in axes[len(metrics):]:
    ax.axis("off")

plt.suptitle("Statystyki dzienne S&P500", fontsize=18, weight="bold", color="black", y=1.02)
plt.tight_layout()
plt.show()

"""
Skybrisk Data Science Internship — Week 4
Client Project: Weather Data Visualization Dashboard

Explores relationships between weather features using Matplotlib and Seaborn.
Produces individual plots in plots/ and a combined overview image
plots/dashboard.png.

Plots:
  - Scatter: temperature vs humidity (coloured by city)
  - Histograms: distribution of each numeric feature
  - Heatmap: correlation matrix
  - Pairplot: pairwise feature relationships
  - Box plot: temperature by city
  - Line plot: monthly average temperature by city

Run:
    python dashboard.py
    python dashboard.py --show        # also open interactive windows
"""

import argparse
import sys
from pathlib import Path

import matplotlib
if "--show" not in sys.argv:
    matplotlib.use("Agg")      # headless: just save files
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

NUMERIC = ["temperature_c", "humidity_pct", "rainfall_mm", "wind_speed_kmh", "pressure_hpa"]
OUT = Path("plots")
CITY_ORDER = ["Kanpur", "Mumbai", "Shimla", "Jaipur"]
PALETTE = dict(zip(CITY_ORDER, sns.color_palette("tab10", 4)))   # same colour for a city in every plot


def load_data(path):
    df = pd.read_csv(path, parse_dates=["date"])
    df["month"] = df["date"].dt.month
    return df


def scatter_temp_humidity(df, ax=None):
    save = ax is None
    if save:
        fig, ax = plt.subplots(figsize=(7, 5))
    sns.scatterplot(data=df, x="temperature_c", y="humidity_pct",
                    hue="city", hue_order=CITY_ORDER, palette=PALETTE,
                    alpha=0.6, s=25, ax=ax)
    ax.legend(title="City", fontsize=8, loc="lower left", ncol=2)
    ax.set_title("Temperature vs Humidity")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Humidity (%)")
    if save:
        fig.tight_layout(); fig.savefig(OUT / "scatter_temp_humidity.png", dpi=150); plt.close(fig)


def histograms(df, axes=None):
    save = axes is None
    if save:
        fig, axes = plt.subplots(2, 3, figsize=(13, 7))
    for ax, col in zip(axes.flat, NUMERIC):
        sns.histplot(df[col], bins=25, kde=True, ax=ax, color="steelblue")
        ax.set_title(f"Distribution: {col}")
    for ax in list(axes.flat)[len(NUMERIC):]:
        ax.axis("off")
    if save:
        fig.tight_layout(); fig.savefig(OUT / "histograms.png", dpi=150); plt.close(fig)


def correlation_heatmap(df, ax=None):
    save = ax is None
    if save:
        fig, ax = plt.subplots(figsize=(7, 5.5))
    sns.heatmap(df[NUMERIC].corr(), annot=True, fmt=".2f", cmap="coolwarm",
                vmin=-1, vmax=1, annot_kws={"size": 9}, cbar_kws={"shrink": 0.8}, ax=ax)
    ax.tick_params(axis="x", rotation=40)
    plt.setp(ax.get_xticklabels(), ha="right")
    ax.tick_params(axis="y", rotation=0)
    ax.set_title("Correlation Heatmap")
    if save:
        fig.tight_layout(); fig.savefig(OUT / "correlation_heatmap.png", dpi=150); plt.close(fig)


def pairplot(df):
    grid = sns.pairplot(df, vars=["temperature_c", "humidity_pct", "pressure_hpa", "wind_speed_kmh"],
                        hue="city", hue_order=CITY_ORDER, palette=PALETTE, corner=True, plot_kws={"alpha": 0.4, "s": 12})
    grid.figure.suptitle("Pairwise Relationships", y=1.02)
    grid.savefig(OUT / "pairplot.png", dpi=120)
    plt.close(grid.figure)


def boxplot_by_city(df, ax=None):
    save = ax is None
    if save:
        fig, ax = plt.subplots(figsize=(7, 5))
    sns.boxplot(data=df, x="city", y="temperature_c", hue="city", order=CITY_ORDER,
                palette=PALETTE, legend=False, ax=ax)
    ax.set_title("Temperature by City")
    ax.set_xlabel("")
    ax.set_ylabel("Temperature (°C)")
    if save:
        fig.tight_layout(); fig.savefig(OUT / "boxplot_temp_by_city.png", dpi=150); plt.close(fig)


def monthly_line(df, ax=None):
    save = ax is None
    if save:
        fig, ax = plt.subplots(figsize=(8, 4.5))
    monthly = df.groupby(["month", "city"], as_index=False)["temperature_c"].mean()
    sns.lineplot(data=monthly, x="month", y="temperature_c", hue="city", hue_order=CITY_ORDER, palette=PALETTE,
                 marker="o", ax=ax)
    ax.set_xticks(range(1, 13))
    ax.set_title("Monthly Average Temperature")
    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature (°C)")
    if save:
        fig.tight_layout(); fig.savefig(OUT / "monthly_avg_temperature.png", dpi=150); plt.close(fig)


def combined_dashboard(df):
    """One overview image with the main plots arranged in a grid."""
    fig = plt.figure(figsize=(19, 11))
    grid = fig.add_gridspec(2, 3, width_ratios=[1, 1.15, 0.9], hspace=0.4, wspace=0.55)
    scatter_temp_humidity(df, fig.add_subplot(grid[0, 0]))
    correlation_heatmap(df, fig.add_subplot(grid[0, 1]))
    boxplot_by_city(df, fig.add_subplot(grid[0, 2]))
    monthly_line(df, fig.add_subplot(grid[1, 0:2]))
    ax = fig.add_subplot(grid[1, 2])
    sns.histplot(df["temperature_c"], bins=25, kde=True, ax=ax, color="steelblue")
    ax.set_title("Distribution: temperature_c")
    fig.suptitle("Weather Data Dashboard", fontsize=20, fontweight="bold")
    fig.savefig(OUT / "dashboard.png", dpi=130, bbox_inches="tight")
    return fig


def print_insights(df):
    corr = df[NUMERIC].corr()
    print("\nKey relationships (Pearson correlation):")
    print(f"  temperature vs humidity: {corr.loc['temperature_c', 'humidity_pct']:+.2f}")
    print(f"  temperature vs pressure: {corr.loc['temperature_c', 'pressure_hpa']:+.2f}")
    print(f"  humidity vs rainfall:    {corr.loc['humidity_pct', 'rainfall_mm']:+.2f}")
    hottest = df.groupby("city")["temperature_c"].mean().idxmax()
    print(f"  Highest average temperature: {hottest}")


def main():
    parser = argparse.ArgumentParser(description="Build the weather visualization dashboard.")
    parser.add_argument("--input", default="sample_data/weather_data.csv")
    parser.add_argument("--show", action="store_true", help="open plot windows")
    args = parser.parse_args()

    OUT.mkdir(exist_ok=True)
    sns.set_theme(style="whitegrid")
    df = load_data(args.input)
    print(f"Loaded {len(df)} rows, {df['city'].nunique()} cities")

    scatter_temp_humidity(df)
    histograms(df)
    correlation_heatmap(df)
    pairplot(df)
    boxplot_by_city(df)
    monthly_line(df)
    fig = combined_dashboard(df)
    print(f"Plots saved in: {OUT}/")
    print_insights(df)

    if args.show:
        plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()

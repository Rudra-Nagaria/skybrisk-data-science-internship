"""
Skybrisk Data Science Internship — Week 4
Hands-On: Matplotlib Basics

Creates one example of each basic plot type and saves them to plots/.
Run:  python matplotlib_basics.py
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")          # save to files (works without a display)
import matplotlib.pyplot as plt
import numpy as np

OUT = Path("plots")
OUT.mkdir(exist_ok=True)


def line_plot():
    days = np.arange(1, 8)
    temps = [28, 30, 32, 31, 29, 27, 26]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(days, temps, marker="o", color="tab:red", linewidth=2)
    ax.set_title("Daily Temperature (Week 1)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "basics_line.png", dpi=150)
    plt.close(fig)


def bar_plot():
    cities = ["Kanpur", "Mumbai", "Shimla", "Jaipur"]
    rainfall = [820, 2400, 1500, 600]
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(cities, rainfall, color="tab:blue")
    ax.bar_label(bars, padding=3)
    ax.set_title("Illustrative Annual Rainfall by City")
    ax.set_ylabel("Rainfall (mm)")
    fig.tight_layout()
    fig.savefig(OUT / "basics_bar.png", dpi=150)
    plt.close(fig)


def scatter_plot():
    rng = np.random.default_rng(0)
    hours = rng.uniform(1, 10, 50)
    score = 40 + 5 * hours + rng.normal(0, 6, 50)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.scatter(hours, score, alpha=0.7, color="tab:green")
    ax.set_title("Study Hours vs Score (synthetic)")
    ax.set_xlabel("Hours studied")
    ax.set_ylabel("Score")
    fig.tight_layout()
    fig.savefig(OUT / "basics_scatter.png", dpi=150)
    plt.close(fig)


def histogram():
    rng = np.random.default_rng(1)
    data = rng.normal(30, 4, 500)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(data, bins=20, color="tab:purple", edgecolor="white")
    ax.axvline(data.mean(), color="black", linestyle="--", label=f"Mean = {data.mean():.1f}")
    ax.set_title("Distribution of Temperatures (synthetic)")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "basics_histogram.png", dpi=150)
    plt.close(fig)


def subplot_grid():
    x = np.linspace(0, 2 * np.pi, 100)
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))
    axes[0].plot(x, np.sin(x)); axes[0].set_title("sin(x)")
    axes[1].plot(x, np.cos(x), color="tab:orange"); axes[1].set_title("cos(x)")
    axes[2].plot(x, np.sin(x) * np.cos(x), color="tab:green"); axes[2].set_title("sin(x)·cos(x)")
    fig.suptitle("Multiple subplots in one figure")
    fig.tight_layout()
    fig.savefig(OUT / "basics_subplots.png", dpi=150)
    plt.close(fig)


def main():
    for func in (line_plot, bar_plot, scatter_plot, histogram, subplot_grid):
        func()
        print(f"Created: {func.__name__}")
    print(f"Plots saved in: {OUT}/")


if __name__ == "__main__":
    main()

# Week 4: Data Visualization with Matplotlib and Seaborn

## Topics covered
- **Matplotlib basics:** the `fig, ax = plt.subplots()` pattern; line, bar, scatter and histogram plots; titles, axis labels, legends, grids, `savefig()`.
- **Subplots and layouts:** several plots in one figure with `subplots()` and `GridSpec`; `tight_layout()` to avoid overlap.
- **Seaborn:** works directly with DataFrames; `scatterplot`, `histplot` (with KDE), `lineplot`, `boxplot`.
- **Advanced plots:** `heatmap` of a correlation matrix (`df.corr()`) and `pairplot` for pairwise relationships.
- **Using colour meaningfully:** `hue` to split by category; the same colour for the same city in every plot.
- **Choosing the right chart:** scatter for relationships, histogram for distributions, box plot for comparing groups, line for trends over time, heatmap for many correlations at once.
- **Correlation vs causation:** a correlation coefficient measures how strongly two variables move together, not why.

## Project: Weather Data Dashboard
The script loads `weather_data.csv`, creates six individual plots, and combines the main ones into a single `dashboard.png`. It also prints key correlations to the terminal. The plots show, for example, that cities form distinct clusters in temperature vs humidity and that temperature has a negative correlation with pressure in this dataset.

## Testing performed
Record your actual results in the last column after running the scripts.

| # | Test | Expected | Your result |
|---|------|----------|-------------|
| 1 | `python matplotlib_basics.py` | 5 `basics_*.png` files created in `plots/` | |
| 2 | `python dashboard.py` | Loads 1,460 rows and 4 cities; creates 7 plot files | |
| 3 | Open `plots/dashboard.png` | 5 panels, no overlapping labels | |
| 4 | Change a colour or title in `dashboard.py` and rerun | Plot updates | |
| 5 | `python dashboard.py --show` | Plot windows open | |

## Learning outcome
This week turned tables of numbers into visuals: choosing a suitable chart for each question, comparing groups and features, and combining several plots into one dashboard that communicates relationships in the data.

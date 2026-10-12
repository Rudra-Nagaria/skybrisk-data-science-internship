# Week 4 — Data Visualization: Weather Data Dashboard

## Overview
Hands-on practice with Matplotlib basic plots and Seaborn advanced plots, plus a client-style project that builds a dashboard showing relationships between weather features (temperature, humidity, rainfall, wind speed, pressure) across four cities.

## Requirements
- Python 3.9 or later
- NumPy, Pandas, Matplotlib and Seaborn:

```bash
pip install -r requirements.txt
```

## Run the project
Open a terminal in this folder.

Hands-on practice (line, bar, scatter, histogram, subplots):

```bash
python matplotlib_basics.py
```

Client project (dashboard):

```bash
python dashboard.py
python dashboard.py --show      # also opens interactive plot windows
```

Optional: regenerate the sample data (fixed random seed):

```bash
python generate_sample_data.py
```

On some Windows installations, use `py` instead of `python`.

## Output
All images are saved in `plots/`:

| File | Plot |
|---|---|
| `dashboard.png` | Combined overview dashboard |
| `scatter_temp_humidity.png` | Scatter: temperature vs humidity by city |
| `histograms.png` | Histograms with density curves for each feature |
| `correlation_heatmap.png` | Seaborn heatmap of correlations |
| `pairplot.png` | Seaborn pairplot of key features |
| `boxplot_temp_by_city.png` | Box plot: temperature by city |
| `monthly_avg_temperature.png` | Line plot: monthly average temperature |
| `basics_*.png` | Matplotlib practice plots |

## Files
- `matplotlib_basics.py` — hands-on Matplotlib exercises
- `dashboard.py` — client project: Seaborn/Matplotlib dashboard
- `generate_sample_data.py` — creates the sample dataset
- `sample_data/weather_data.csv` — 1,460 daily readings (4 cities × 365 days)
- `requirements.txt` — required libraries
- `concepts_summary.md` — Week 4 learning summary

## Notes
The weather data is synthetic, generated with built-in relationships so the plots show meaningful patterns. Any "findings" describe this practice dataset only, not real weather in these cities. Correlation shows that two features move together; it does not prove that one causes the other.

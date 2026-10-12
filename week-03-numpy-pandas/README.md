# Week 3 — NumPy and Pandas: Sales Dataset Cleaning and Aggregation

## Overview
Hands-on practice with NumPy arrays and broadcasting and with Pandas Series, DataFrames, indexing and grouping, plus a client-style project that cleans a messy sales dataset and aggregates revenue by region, product and month.

## Requirements
- Python 3.9 or later
- NumPy and Pandas:

```bash
pip install -r requirements.txt
```

## Run the project
Open a terminal in this folder.

Hands-on practice:

```bash
python numpy_pandas_practice.py
```

Client project:

```bash
python dataset_cleaner.py
python dataset_cleaner.py --input sample_data/raw_sales.csv --outdir output
```

Optional: regenerate the sample data (fixed random seed, so the result is identical):

```bash
python generate_sample_data.py
```

On some Windows installations, use `py` instead of `python`.

## Example test
Using `sample_data/raw_sales.csv` (208 rows) with default options:

| Check | Expected |
|---|---|
| Rows read | 208 |
| Duplicate rows removed | 8 |
| Rows dropped (missing essential fields) | 22 |
| Discounts filled with 0 | 10 |
| Rows kept | 178 |

## Files
- `numpy_pandas_practice.py` — hands-on exercises for NumPy and Pandas
- `dataset_cleaner.py` — client project: cleaning and aggregation script
- `generate_sample_data.py` — creates the messy sample dataset
- `sample_data/raw_sales.csv` — sample data (missing values, duplicates, inconsistent text, invalid dates)
- `requirements.txt` — required libraries
- `concepts_summary.md` — Week 3 learning summary

Running the cleaner creates an `output/` folder containing `cleaned_sales.csv`, `by_region.csv`, `by_product.csv`, `by_month.csv`, `region_product_avg.csv` and `cleaning_report.txt`.

## Notes
The sample data is synthetic, so the totals and averages are illustrative only. Missing-value rules are a business decision: here rows missing date, region, product, units or price are dropped, while a missing discount is treated as 0. Check these rules with your client before applying them to real data.

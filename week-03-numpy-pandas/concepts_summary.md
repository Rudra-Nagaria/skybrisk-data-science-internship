# Week 3: NumPy and Pandas for Data Manipulation

## Topics covered
- **NumPy arrays:** fixed-type, multi-dimensional arrays with `shape` and `dtype`; created with `np.array`, `np.arange`, `np.zeros`, `np.linspace`; reshaped with `reshape`.
- **Vectorised operations:** arithmetic and statistics (`mean`, `std`, `sum`) applied to a whole array without loops; `axis=0` for columns and `axis=1` for rows.
- **Boolean masking and slicing:** selecting elements by condition, e.g. `a[a > 25]`.
- **Broadcasting:** NumPy automatically stretches smaller arrays to match larger ones (scalar, row and column cases), e.g. weighting scores or centring each column.
- **Pandas Series:** labelled one-dimensional data with an index.
- **Pandas DataFrames:** tables of columns; `head`, `info`, `describe`, `shape`.
- **Indexing:** `df["col"]`, `loc` (by label), `iloc` (by position), and conditional filtering with `&`.
- **Missing data:** `isna()`, `dropna()`, `fillna()`.
- **Cleaning:** `drop_duplicates()`, `.str.strip()`, `.str.title()`, `pd.to_datetime(errors="coerce")`.
- **Grouping:** `groupby()` with `agg()`, and `pivot_table()` for cross-tabulated averages.

## Project: Sales Dataset Cleaning and Aggregation
The script loads `raw_sales.csv`, removes duplicates, standardises region and product names, converts dates, drops rows missing essential fields, treats a missing discount as 0, calculates `revenue = units × unit_price × (1 − discount)`, then aggregates by region, product and month. Results are saved as CSV files plus a text report.

## Testing performed
Record your actual results in the last column after running the scripts.

| # | Test | Expected | Your result |
|---|------|----------|-------------|
| 1 | `python dataset_cleaner.py` | 208 rows read, 178 kept | |
| 2 | Check `output/cleaned_sales.csv` | No empty region/product/date; `revenue` column present | |
| 3 | Open `output/by_region.csv` | 4 regions; sorted by total revenue | |
| 4 | Add a duplicate row to the raw CSV and rerun | Duplicate count increases by 1 | |
| 5 | `python numpy_pandas_practice.py` | Runs without errors; groupby shows Data and Design averages | |

## Learning outcome
This week replaced manual loops with vectorised NumPy and Pandas operations and applied them to a realistic, messy dataset: inspecting it, cleaning it, making explicit decisions about missing values, and summarising it with groupby aggregations.

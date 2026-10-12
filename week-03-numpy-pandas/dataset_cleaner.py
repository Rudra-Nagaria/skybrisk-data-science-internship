"""
Skybrisk Data Science Internship — Week 3
Client Project: Sales Dataset Cleaning and Aggregation

Loads a messy sales CSV, cleans it with Pandas, calculates revenue, and
aggregates the results by region, product and month.

Cleaning steps:
  1. Remove exact duplicate rows
  2. Standardise text (trim spaces, consistent capitalisation)
  3. Convert order_date to real dates (unparseable values become missing)
  4. Remove rows missing essential fields (date, region, product, units, unit_price)
  5. Treat a missing discount as 0 (no discount recorded)
  6. Calculate revenue = units * unit_price * (1 - discount)

Run:
    python dataset_cleaner.py
    python dataset_cleaner.py --input sample_data/raw_sales.csv --outdir output
"""

import argparse
from pathlib import Path

import pandas as pd

ESSENTIAL_COLUMNS = ["order_date", "region", "product", "units", "unit_price"]


def load_data(path):
    return pd.read_csv(path)


def clean_sales(df):
    """Clean the raw DataFrame. Returns (cleaned_df, stats dict)."""
    stats = {"rows_in": len(df)}
    df = df.copy()

    # 1. duplicates
    before = len(df)
    df = df.drop_duplicates()
    stats["duplicates_removed"] = before - len(df)

    # 2. text standardisation
    df["region"] = df["region"].str.strip().str.title()
    df["product"] = df["product"].str.strip().str.title()

    # 3. dates
    df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d", errors="coerce")

    # 4. essential fields
    stats["missing_before"] = df[ESSENTIAL_COLUMNS + ["discount"]].isna().sum().to_dict()
    before = len(df)
    df = df.dropna(subset=ESSENTIAL_COLUMNS)
    stats["rows_dropped_missing_essential"] = before - len(df)

    # 5. discount default
    stats["discount_filled_with_zero"] = int(df["discount"].isna().sum())
    df = df.assign(discount=df["discount"].fillna(0.0))

    # 6. revenue
    df = df.assign(
        units=df["units"].astype(int),
        revenue=(df["units"] * df["unit_price"] * (1 - df["discount"])).round(2),
        month=df["order_date"].dt.to_period("M").astype(str),
    )

    stats["rows_out"] = len(df)
    return df.reset_index(drop=True), stats


def aggregate(df):
    """Return a dict of summary tables."""
    by_region = (df.groupby("region")
                   .agg(orders=("order_id", "count"),
                        total_revenue=("revenue", "sum"),
                        avg_order_value=("revenue", "mean"),
                        avg_units=("units", "mean"))
                   .round(2)
                   .sort_values("total_revenue", ascending=False))

    by_product = (df.groupby("product")
                    .agg(orders=("order_id", "count"),
                         units_sold=("units", "sum"),
                         total_revenue=("revenue", "sum"),
                         avg_discount=("discount", "mean"))
                    .round(3)
                    .sort_values("total_revenue", ascending=False))

    by_month = (df.groupby("month")
                  .agg(orders=("order_id", "count"),
                       total_revenue=("revenue", "sum"))
                  .round(2))

    region_product = df.pivot_table(index="region", columns="product",
                                    values="revenue", aggfunc="mean").round(2)

    return {"by_region": by_region, "by_product": by_product,
            "by_month": by_month, "region_product_avg": region_product}


def build_report(stats, tables, df):
    lines = [
        "Sales Data Cleaning and Aggregation Report",
        "------------------------------------------",
        f"Rows read:                         {stats['rows_in']}",
        f"Duplicate rows removed:            {stats['duplicates_removed']}",
        f"Rows dropped (missing essentials): {stats['rows_dropped_missing_essential']}",
        f"Discounts filled with 0:           {stats['discount_filled_with_zero']}",
        f"Rows kept:                         {stats['rows_out']}",
        "",
        "Missing values per column (after de-duplication, before dropping):",
    ]
    lines += [f"  {col}: {n}" for col, n in stats["missing_before"].items()]
    lines += [
        "",
        f"Overall average order value: {df['revenue'].mean():,.2f}",
        f"Total revenue:               {df['revenue'].sum():,.2f}",
        "",
        "Revenue by region:",
        tables["by_region"].to_string(),
        "",
        "Revenue by product:",
        tables["by_product"].to_string(),
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Clean and aggregate a sales CSV.")
    parser.add_argument("--input", default="sample_data/raw_sales.csv")
    parser.add_argument("--outdir", default="output")
    args = parser.parse_args()

    raw = load_data(args.input)
    cleaned, stats = clean_sales(raw)
    tables = aggregate(cleaned)
    report = build_report(stats, tables, cleaned)

    outdir = Path(args.outdir)
    outdir.mkdir(exist_ok=True)
    cleaned.to_csv(outdir / "cleaned_sales.csv", index=False)
    for name, table in tables.items():
        table.to_csv(outdir / f"{name}.csv")
    (outdir / "cleaning_report.txt").write_text(report + "\n", encoding="utf-8")

    print(report)
    print(f"\nFiles saved in: {outdir}/")


if __name__ == "__main__":
    main()

"""
Skybrisk Data Science Internship — Week 2
Client Project: Customer Data Cleaner

Reads a messy customer CSV file and produces a cleaned file plus a report.
Cleaning steps:
  1. Strip extra spaces and standardise capitalisation
  2. Remove rows with a missing name or email
  3. Remove rows with a missing, non-numeric or unrealistic age
  4. Remove duplicate customers (same email address, keep the first)
  5. Optionally filter to a single city

Only the Python standard library is used (csv, argparse).

Run:
    python data_cleaner.py
    python data_cleaner.py --city Kanpur
    python data_cleaner.py --input sample_data/raw_customers.csv --output cleaned_customers.csv
"""

import argparse
import csv

MIN_AGE = 0
MAX_AGE = 120   # configurable validation rule, not a universal definition


def standardise_row(row):
    """Return a new dict with trimmed text, title-case names/cities, lowercase email."""
    return {
        "customer_id": row["customer_id"].strip(),
        "name": row["name"].strip().title(),
        "email": row["email"].strip().lower(),
        "age": row["age"].strip(),
        "city": row["city"].strip().title(),
    }


def parse_age(text):
    """Return an int age, or None if the text is not a valid age."""
    try:
        age = int(text)
    except ValueError:
        return None
    return age if MIN_AGE <= age <= MAX_AGE else None


def clean_customers(rows, city=None):
    """Clean a list of raw row dicts.

    Returns (cleaned_rows, stats) where stats counts every removal reason.
    """
    stats = {
        "input_rows": len(rows),
        "missing_name_or_email": 0,
        "invalid_age": 0,
        "duplicates": 0,
        "filtered_out_by_city": 0,
    }
    seen_emails = set()      # a set gives fast "have I seen this?" checks
    cleaned = []

    for raw in rows:
        row = standardise_row(raw)

        if not row["name"] or not row["email"]:
            stats["missing_name_or_email"] += 1
            continue

        age = parse_age(row["age"])
        if age is None:
            stats["invalid_age"] += 1
            continue
        row["age"] = age

        if row["email"] in seen_emails:
            stats["duplicates"] += 1
            continue
        seen_emails.add(row["email"])

        if city and row["city"].lower() != city.strip().lower():
            stats["filtered_out_by_city"] += 1
            continue

        cleaned.append(row)

    stats["output_rows"] = len(cleaned)
    return cleaned, stats


def summarise(cleaned):
    """Build simple summary information about the cleaned data."""
    if not cleaned:
        return "No rows remain after cleaning."
    ages = [r["age"] for r in cleaned]
    customers_per_city = {}
    for r in cleaned:
        customers_per_city[r["city"]] = customers_per_city.get(r["city"], 0) + 1

    lines = [f"Average age: {sum(ages) / len(ages):.1f}",
             f"Youngest: {min(ages)}   Oldest: {max(ages)}",
             "Customers per city:"]
    lines += [f"  {c}: {n}" for c, n in sorted(customers_per_city.items())]
    return "\n".join(lines)


def build_report(stats, summary, city):
    lines = [
        "Customer Data Cleaning Report",
        "-----------------------------",
        f"Rows read:                      {stats['input_rows']}",
        f"Removed (missing name/email):   {stats['missing_name_or_email']}",
        f"Removed (invalid/missing age):  {stats['invalid_age']}",
        f"Removed (duplicate email):      {stats['duplicates']}",
    ]
    if city:
        lines.append(f"Removed (not in {city}):".ljust(32) + str(stats["filtered_out_by_city"]))
    lines += [f"Rows kept:                      {stats['output_rows']}", "", summary]
    return "\n".join(lines)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows):
    fieldnames = ["customer_id", "name", "email", "age", "city"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Clean a customer CSV file.")
    parser.add_argument("--input", default="sample_data/raw_customers.csv")
    parser.add_argument("--output", default="cleaned_customers.csv")
    parser.add_argument("--city", default=None, help="keep only this city")
    args = parser.parse_args()

    rows = read_csv(args.input)
    cleaned, stats = clean_customers(rows, city=args.city)
    report = build_report(stats, summarise(cleaned), args.city)

    write_csv(args.output, cleaned)
    with open("cleaning_report.txt", "w", encoding="utf-8") as f:
        f.write(report + "\n")

    print(report)
    print(f"\nCleaned data saved to: {args.output}")
    print("Report saved to: cleaning_report.txt")


if __name__ == "__main__":
    main()

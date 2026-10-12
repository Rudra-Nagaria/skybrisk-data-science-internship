# Week 2 — Data Structures and Functions: Customer Data Cleaner

## Overview
Hands-on practice with Python's core data structures and functions, plus a client-style project that cleans a messy customer CSV file: standardises text, removes invalid rows, removes duplicates and optionally filters by city.

## Requirements
- Python 3.9 or later
- No third-party libraries required (uses only `csv` and `argparse`)

## Run the project
Open a terminal in this folder.

Hands-on practice (lists, tuples, dictionaries, sets, functions, lambda, recursion, comprehensions):

```bash
python data_structures_practice.py
```

Client project (data cleaning):

```bash
python data_cleaner.py
python data_cleaner.py --city Kanpur
python data_cleaner.py --input sample_data/raw_customers.csv --output cleaned_customers.csv
```

On some Windows installations, use `py` instead of `python`.

## Example test
Using `sample_data/raw_customers.csv` (18 rows) with default options:

| Check | Expected |
|---|---|
| Rows read | 18 |
| Removed (missing name/email) | 2 |
| Removed (invalid/missing age) | 4 |
| Removed (duplicate email) | 3 |
| Rows kept | 9 |

With `--city Kanpur`, 4 rows remain.

## Files
- `data_structures_practice.py` — hands-on exercises for every Week 2 topic
- `data_cleaner.py` — client project: customer data cleaning script
- `sample_data/raw_customers.csv` — messy sample data (extra spaces, mixed case, missing values, bad ages, duplicates)
- `concepts_summary.md` — Week 2 learning summary

Running the cleaner creates `cleaned_customers.csv` and `cleaning_report.txt`.

## Notes
The accepted age range of 0 to 120 is a configurable validation rule for this exercise (`MIN_AGE`, `MAX_AGE`). Duplicates are identified by email address and the first occurrence is kept; change this rule if your client defines duplicates differently.

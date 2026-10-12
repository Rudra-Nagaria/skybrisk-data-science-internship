# Week 2: Data Structures and Functions

## Topics covered
- **Lists:** ordered, changeable collections; used for readings and rows. Methods such as `append()`, `insert()`, `remove()`, slicing and `sorted()`.
- **Tuples:** ordered, immutable records such as `(city, latitude, longitude)`; supports unpacking.
- **Dictionaries:** key–value pairs; used for a record (one customer) and as a counter (word frequency, customers per city). `.get()` gives a safe lookup.
- **Sets:** unique, unordered values; used to remove duplicates and for fast "already seen?" checks. Union, intersection and difference operators.
- **Functions:** reusable blocks with parameters, default values, keyword-only arguments and `return` values. Each cleaning step is its own function.
- **Lambda functions:** small anonymous functions used with `sorted(key=...)`, `map()` and `filter()`.
- **Recursion:** a function that calls itself, with a base case (`factorial`, `fibonacci`).
- **List comprehensions:** compact way to transform or filter lists; dictionary and set comprehensions follow the same idea.

## Project: Customer Data Cleaner
The script reads `raw_customers.csv`, then for each row it:
1. trims whitespace and standardises capitalisation,
2. removes rows with a missing name or email,
3. removes rows with a missing, non-numeric or out-of-range age,
4. removes duplicate customers by email (using a set),
5. optionally keeps only one city.

It writes `cleaned_customers.csv` and a `cleaning_report.txt` showing how many rows each step removed.

## Testing performed
Record your actual results in the last column after running the scripts.

| # | Test | Expected | Your result |
|---|------|----------|-------------|
| 1 | `python data_cleaner.py` | 18 rows read, 9 kept | |
| 2 | `python data_cleaner.py --city Kanpur` | 4 rows kept | |
| 3 | Add a row with age `abc` to the CSV | Row removed as invalid age | |
| 4 | Change an email to a duplicate of another row | Row removed as duplicate | |
| 5 | `python data_structures_practice.py` | `5! = 120`, sum of squares `173` | |

## Learning outcome
This week practised choosing the right data structure for the job (list for ordered rows, dictionary for records and counts, set for uniqueness) and organising code into small, testable functions, applied to a realistic data-cleaning task.

"""
Skybrisk Data Science Internship — Week 3
Hands-On: NumPy and Pandas

Sections:
  1. NumPy arrays and operations
  2. Broadcasting
  3. Pandas Series
  4. Pandas DataFrames and indexing
  5. Grouping and aggregation

Run:  python numpy_pandas_practice.py
"""

import numpy as np
import pandas as pd


def numpy_basics():
    print("\n=== 1. NumPy arrays and operations ===")
    a = np.array([10, 20, 30, 40, 50])
    print("Array:", a, "| dtype:", a.dtype, "| shape:", a.shape)
    print("a * 2 =", a * 2)                      # vectorised: no loop needed
    print("a + a =", a + a)
    print("Mean / std / sum:", a.mean(), round(a.std(), 2), a.sum())
    print("Boolean mask a > 25:", a[a > 25])
    print("Slice a[1:4]:", a[1:4])

    matrix = np.arange(1, 13).reshape(3, 4)
    print("\nMatrix (3x4):\n", matrix)
    print("Column sums:", matrix.sum(axis=0))
    print("Row sums:", matrix.sum(axis=1))
    print("Transpose shape:", matrix.T.shape)

    print("zeros(2,3):\n", np.zeros((2, 3)))
    print("linspace(0, 1, 5):", np.linspace(0, 1, 5))


def broadcasting_demo():
    print("\n=== 2. Broadcasting ===")
    scores = np.array([[70, 80, 90],
                       [60, 75, 85],
                       [88, 92, 79]])
    print("Scores:\n", scores)

    # scalar broadcast to every element
    print("Add 5 bonus marks:\n", scores + 5)

    # a (3,) row broadcast across each row
    weights = np.array([0.2, 0.3, 0.5])
    print("Weighted scores:\n", scores * weights)
    print("Weighted total per student:", (scores * weights).sum(axis=1))

    # a (3,1) column broadcast across each column
    student_adjustment = np.array([[1], [2], [3]])
    print("Per-student adjustment:\n", scores + student_adjustment)

    # subtract each column's mean (centre the data)
    print("Column-centred:\n", scores - scores.mean(axis=0))


def series_demo():
    print("\n=== 3. Pandas Series ===")
    temps = pd.Series([28.5, 30.0, 32.5, 27.0],
                      index=["Mon", "Tue", "Wed", "Thu"], name="temp_c")
    print(temps)
    print("Wed:", temps["Wed"], "| first:", temps.iloc[0])
    print("Above 28:\n", temps[temps > 28])
    print("Fahrenheit:\n", temps * 9 / 5 + 32)
    print("describe():\n", temps.describe().round(2))


def dataframe_demo():
    print("\n=== 4. DataFrames and indexing ===")
    df = pd.DataFrame({
        "name": ["Asha", "Ravi", "Meera", "Karan", "Sana"],
        "department": ["Data", "Data", "Design", "Design", "Data"],
        "salary": [52000, 45000, 61000, 48000, 57000],
        "years": [3, 1, 5, 2, 4],
    })
    print(df)
    print("\nShape:", df.shape)
    df.info()

    print("\nColumn 'name':", df["name"].tolist())
    print("Row 0 by position (iloc):\n", df.iloc[0])
    print("Rows 1-2, cols name & salary (loc):\n", df.loc[1:2, ["name", "salary"]])
    print("Salary > 50000:\n", df[df["salary"] > 50000])
    print("Data dept AND years >= 3:\n", df[(df["department"] == "Data") & (df["years"] >= 3)])

    df["salary_per_year_exp"] = (df["salary"] / df["years"]).round(0)
    print("New column added:\n", df[["name", "salary_per_year_exp"]])
    print("Sorted by salary:\n", df.sort_values("salary", ascending=False)[["name", "salary"]])
    return df


def grouping_demo(df):
    print("\n=== 5. Grouping and aggregation ===")
    print("Mean salary by department:\n", df.groupby("department")["salary"].mean())
    summary = df.groupby("department").agg(
        employees=("name", "count"),
        avg_salary=("salary", "mean"),
        max_years=("years", "max"),
    )
    print("Multiple aggregations:\n", summary)


def main():
    numpy_basics()
    broadcasting_demo()
    series_demo()
    df = dataframe_demo()
    grouping_demo(df)


if __name__ == "__main__":
    main()

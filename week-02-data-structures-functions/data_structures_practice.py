"""
Skybrisk Data Science Internship — Week 2
Hands-On: Data Structures and Functions

Each section below practises one topic from the Week 2 theory:
lists, tuples, dictionaries, sets, functions, lambda functions,
recursion, and list comprehensions.

Run:  python data_structures_practice.py
"""


# ---------------------------------------------------------------
# 1. Lists
# ---------------------------------------------------------------
def list_demo():
    print("\n=== 1. Lists ===")
    temperatures = [28.5, 30.0, 32.5, 27.0, 31.5]
    temperatures.append(29.0)          # add to end
    temperatures.insert(0, 26.5)       # add at position
    temperatures.remove(27.0)          # remove by value
    print("Readings:", temperatures)
    print("Sorted:", sorted(temperatures))
    print("First three:", temperatures[:3])
    print("Reversed:", temperatures[::-1])


# ---------------------------------------------------------------
# 2. Tuples (immutable records)
# ---------------------------------------------------------------
def tuple_demo():
    print("\n=== 2. Tuples ===")
    location = ("Kanpur", 26.4499, 80.3319)    # name, latitude, longitude
    city, latitude, longitude = location         # tuple unpacking
    print(f"{city} is at ({latitude}, {longitude})")
    # location[0] = "Delhi"  -> would raise TypeError: tuples are immutable


# ---------------------------------------------------------------
# 3. Dictionaries
# ---------------------------------------------------------------
def dictionary_demo():
    print("\n=== 3. Dictionaries ===")
    student = {"name": "Asha", "course": "Data Science", "week": 2}
    student["score"] = 88                  # add key
    student["week"] = 3                    # update key
    print("Student:", student)
    print("Score (safe lookup):", student.get("score", "N/A"))
    print("Missing key (safe lookup):", student.get("grade", "N/A"))
    for key, value in student.items():
        print(f"  {key}: {value}")


def word_frequency(text):
    """Count how many times each word appears (dictionary as a counter)."""
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,!?")
        counts[word] = counts.get(word, 0) + 1
    return counts


# ---------------------------------------------------------------
# 4. Sets
# ---------------------------------------------------------------
def set_demo():
    print("\n=== 4. Sets ===")
    python_learners = {"Asha", "Ravi", "Meera", "Karan"}
    pandas_learners = {"Ravi", "Meera", "Sana"}
    print("Both:", python_learners & pandas_learners)       # intersection
    print("Either:", python_learners | pandas_learners)     # union
    print("Only Python:", python_learners - pandas_learners)  # difference

    with_duplicates = [3, 1, 2, 3, 3, 1, 4]
    print("Unique values:", sorted(set(with_duplicates)))


# ---------------------------------------------------------------
# 5. Functions
# ---------------------------------------------------------------
def sum_of_squares(numbers):
    """Return the sum of the squares of all numbers."""
    total = 0
    for n in numbers:
        total += n ** 2
    return total


def filter_above(values, threshold=0):
    """Return only the values strictly greater than threshold."""
    return [v for v in values if v > threshold]


def describe(numbers, *, round_to=2):
    """Return a dictionary of basic statistics (keyword-only argument)."""
    if not numbers:
        return {"count": 0, "mean": None, "min": None, "max": None}
    return {
        "count": len(numbers),
        "mean": round(sum(numbers) / len(numbers), round_to),
        "min": min(numbers),
        "max": max(numbers),
    }


# ---------------------------------------------------------------
# 6. Lambda functions
# ---------------------------------------------------------------
def lambda_demo():
    print("\n=== 6. Lambda functions ===")
    square = lambda x: x ** 2
    print("square(7) =", square(7))

    employees = [("Asha", 52000), ("Ravi", 45000), ("Meera", 61000)]
    by_salary = sorted(employees, key=lambda e: e[1], reverse=True)
    print("Sorted by salary:", by_salary)

    celsius = [0, 20, 37, 100]
    fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
    print("Celsius -> Fahrenheit:", fahrenheit)

    evens = list(filter(lambda n: n % 2 == 0, range(1, 11)))
    print("Even numbers 1-10:", evens)


# ---------------------------------------------------------------
# 7. Recursion
# ---------------------------------------------------------------
def factorial(n):
    """n! computed recursively."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n in (0, 1):          # base case
        return 1
    return n * factorial(n - 1)   # recursive case


def fibonacci(n):
    """n-th Fibonacci number (0, 1, 1, 2, 3, 5, ...), computed recursively."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:                # base cases
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ---------------------------------------------------------------
# 8. List comprehensions
# ---------------------------------------------------------------
def comprehension_demo():
    print("\n=== 8. List comprehensions ===")
    numbers = list(range(1, 11))
    print("Squares:", [n ** 2 for n in numbers])
    print("Even squares:", [n ** 2 for n in numbers if n % 2 == 0])
    print("Labels:", ["even" if n % 2 == 0 else "odd" for n in numbers[:5]])
    print("Dict comprehension:", {n: n ** 2 for n in range(1, 6)})
    print("Set comprehension:", {len(w) for w in ["data", "science", "python", "code"]})


# ---------------------------------------------------------------
# Run everything
# ---------------------------------------------------------------
def main():
    list_demo()
    tuple_demo()
    dictionary_demo()
    print("Word frequency:", word_frequency("Data is data. Clean data, then analyse data!"))
    set_demo()

    print("\n=== 5. Functions ===")
    data = [3, -1, 4, -1, 5, -9, 2, 6]
    print("Data:", data)
    print("Sum of squares:", sum_of_squares(data))
    print("Values above 0:", filter_above(data))
    print("Values above 3:", filter_above(data, threshold=3))
    print("Statistics:", describe(data))
    print("Statistics (empty list):", describe([]))

    lambda_demo()

    print("\n=== 7. Recursion ===")
    print("5! =", factorial(5))
    print("First 10 Fibonacci numbers:", [fibonacci(i) for i in range(10)])

    comprehension_demo()


if __name__ == "__main__":
    main()

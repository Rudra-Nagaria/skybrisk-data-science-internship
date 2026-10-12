# Week 1 — Python Basics: Temperature Data Processor

## Overview
A beginner-friendly Python project for the Skybrisk Data Science Internship. It collects Celsius readings, validates input, calculates summary statistics, converts readings to Fahrenheit, and saves a text report.

## Requirements
- Python 3.9 or later
- No third-party libraries required

## Run the project
Open a terminal in this folder and run:

```bash
python temperature_processor.py
```

On some Windows installations, use:

```bash
py temperature_processor.py
```

Enter one temperature per prompt. Type `done` to finish.

## Example test
Input readings: `28.5`, `30`, `32.5`

Expected summary:
- Number of readings: 3
- Average: 30.33 °C
- Highest: 32.50 °C
- Lowest: 28.50 °C

The program also prints Fahrenheit conversions and saves the report to `temperature_report.txt` when at least one valid reading is provided.

## Files
- `temperature_processor.py` — project source code
- `concepts_summary.md` — Week 1 learning summary

## Notes
The accepted range of -100°C to 70°C is a configurable validation rule for this learning exercise, not a universal definition of valid temperatures. Update the range if your dataset requires different limits.

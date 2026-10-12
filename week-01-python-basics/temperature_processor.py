"""
Skybrisk Data Science Internship — Week 1
Project: Temperature Data Processor

This script demonstrates variables, data types, input/output,
conditionals, loops, calculations, and basic error handling.
"""

MIN_CELSIUS = -100.0
MAX_CELSIUS = 70.0


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def collect_temperatures():
    """Collect valid temperature readings from the user."""
    temperatures = []

    print("Temperature Data Processor")
    print(f"Enter temperatures between {MIN_CELSIUS:g}°C and {MAX_CELSIUS:g}°C.")
    print("Type 'done' when you have entered all readings.")

    while True:
        entry = input("Temperature in °C: ").strip()

        if entry.lower() == "done":
            break

        try:
            temperature = float(entry)
        except ValueError:
            print("Invalid input. Enter a number or type 'done'.")
            continue

        if temperature < MIN_CELSIUS or temperature > MAX_CELSIUS:
            print(f"Out of configured range ({MIN_CELSIUS:g}°C to {MAX_CELSIUS:g}°C). Try again.")
            continue

        temperatures.append(temperature)
        print("Reading added.")

    return temperatures


def create_report(temperatures):
    """Create a summary report from the collected readings."""
    if not temperatures:
        return "No valid temperature readings were entered."

    average = sum(temperatures) / len(temperatures)
    highest = max(temperatures)
    lowest = min(temperatures)

    lines = [
        "",
        "Temperature Analysis Report",
        "---------------------------",
        f"Number of readings: {len(temperatures)}",
        f"Average: {average:.2f} °C",
        f"Highest: {highest:.2f} °C",
        f"Lowest: {lowest:.2f} °C",
        "",
        "Readings and Fahrenheit conversions:",
    ]

    for index, celsius in enumerate(temperatures, start=1):
        fahrenheit = celsius_to_fahrenheit(celsius)
        lines.append(f"{index}. {celsius:.2f} °C = {fahrenheit:.2f} °F")

    return "\n".join(lines)


def main():
    temperatures = collect_temperatures()
    report = create_report(temperatures)
    print(report)

    if temperatures:
        output_file = "temperature_report.txt"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(report + "\n")
        print(f"\nReport saved to: {output_file}")


if __name__ == "__main__":
    main()

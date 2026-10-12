"""
Generates sample_data/weather_data.csv — a synthetic daily weather dataset
for four cities, used for the Week 4 visualization dashboard.
The relationships (e.g. humidity falls as temperature rises) are built in
so the plots have something meaningful to show. A fixed seed keeps it reproducible.

Run:  python generate_sample_data.py
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(7)

cities = {            # base temp (°C), temperature swing, base humidity (%)
    "Kanpur": (26, 11, 55),
    "Mumbai": (28, 3, 75),
    "Shimla": (14, 9, 60),
    "Jaipur": (27, 10, 40),
}
dates = pd.date_range("2025-01-01", "2025-12-31", freq="D")
frames = []

for city, (base, swing, base_hum) in cities.items():
    day = np.arange(len(dates))
    seasonal = np.sin((day - 100) / 365 * 2 * np.pi)          # peaks around mid-year
    temp = base + swing * seasonal + rng.normal(0, 1.5, len(dates))
    humidity = base_hum - 0.9 * (temp - base) + 12 * np.clip(seasonal, 0, None) + rng.normal(0, 5, len(dates))
    rainfall = np.clip(rng.gamma(0.6, 6, len(dates)) * (1 + np.clip(seasonal, 0, None) * 2)
                       * (humidity > 55), 0, None)
    wind = np.clip(rng.normal(12, 4, len(dates)) - 0.05 * humidity + 3, 0, None)
    pressure = 1013 - 0.25 * (temp - base) + rng.normal(0, 2.5, len(dates))
    frames.append(pd.DataFrame({
        "date": dates, "city": city,
        "temperature_c": temp.round(1),
        "humidity_pct": np.clip(humidity, 10, 100).round(1),
        "rainfall_mm": rainfall.round(1),
        "wind_speed_kmh": wind.round(1),
        "pressure_hpa": pressure.round(1),
    }))

df = pd.concat(frames, ignore_index=True)
df.to_csv("sample_data/weather_data.csv", index=False)
print(f"Saved sample_data/weather_data.csv with {len(df)} rows")

import pandas as pd

df = pd.read_csv("ev_clustered_output.csv")

df['range_km'] = pd.to_numeric(df['range_km'], errors='coerce')
df['battery_capacity_kWh'] = pd.to_numeric(df['battery_capacity_kWh'], errors='coerce')

df = df.dropna(subset=['range_km', 'battery_capacity_kWh'])

df['km_per_kWh'] = df['range_km'] / df['battery_capacity_kWh']

df_sorted = df.sort_values(by='km_per_kWh', ascending=False)

value_columns = ['brand', 'model', 'range_km', 'battery_capacity_kWh', 'km_per_kWh', 'drivetrain', 'car_body_type', 'EV_Persona_Label']
df_export = df_sorted[value_columns]

df_export.to_csv("ev_value_benchmark.csv", index=False)

print("EV models ranked by km per kWh saved to ev_value_benchmark.csv")

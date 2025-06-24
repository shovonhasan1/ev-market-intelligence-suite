import pandas as pd

df = pd.read_csv("ev_clustered_output.csv")

df['range_km'] = pd.to_numeric(df['range_km'], errors='coerce')
df['fast_charging_power_kw_dc'] = pd.to_numeric(df['fast_charging_power_kw_dc'], errors='coerce')

df = df.dropna(subset=['range_km', 'fast_charging_power_kw_dc'])

df['range_per_kw'] = df['range_km'] / df['fast_charging_power_kw_dc']

df['charging_risk_flag'] = ((df['range_km'] < 300) & (df['fast_charging_power_kw_dc'] < 100)).astype(int)

df.to_csv("ev_charging_risk_flagged.csv", index=False)

risky_models = df[df['charging_risk_flag'] == 1][['brand', 'model', 'range_km', 'fast_charging_power_kw_dc', 'range_per_kw']]
print("EVs flagged as charging-risk zone:")
print(risky_models.head(10))


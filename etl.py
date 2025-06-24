import pandas as pd

df = pd.read_csv("electric_vehicles_spec_2025.csv")

df.drop(columns=["source_url"], inplace=True)

df.columns = df.columns.str.strip()

df.drop_duplicates(inplace=True)

missing_percent = df.isna().mean().round(3) * 100
print("\nMissing values (%):\n", missing_percent[missing_percent > 0])

df.dropna(inplace=True)

df.reset_index(drop=True, inplace=True)

print("\nFinal cleaned shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())

df.to_csv("cleaned_ev_data.csv", index=False)

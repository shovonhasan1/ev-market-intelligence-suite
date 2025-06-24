import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load cleaned dataset
df = pd.read_csv("cleaned_ev_data.csv")

# Drop irrelevant or non-numeric columns
non_numeric_cols = ["brand", "model", "battery_type", "fast_charge_port", "car_body_type", "segment", "drivetrain"]
df = df.drop(columns=non_numeric_cols, errors='ignore')

# Drop rows with missing or non-numeric values
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna()

# Split data
X = df.drop(columns=["efficiency_wh_per_km"])
y = df["efficiency_wh_per_km"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Get importance
importances = model.feature_importances_
feature_names = X.columns

# Save to CSV
fi_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

fi_df.to_csv("ev_feature_importance.csv", index=False)

print("Feature importance saved to ev_feature_importance.csv")

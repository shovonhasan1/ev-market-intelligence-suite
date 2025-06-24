import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_ev_data.csv")  # Make sure this is the correct path


numeric_features = [
    'acceleration_0_100_s',
    'battery_capacity_kWh',
    'efficiency_wh_per_km',
    'cargo_volume_l',
    'seats',
    'fast_charging_power_kw_dc'
]

categorical_features = ['drivetrain', 'car_body_type']
target = 'range_km'


df['cargo_volume_l'] = pd.to_numeric(df['cargo_volume_l'], errors='coerce')

df = df[numeric_features + categorical_features + [target]].dropna()

encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded = pd.DataFrame(
    encoder.fit_transform(df[categorical_features]),
    columns=encoder.get_feature_names_out(categorical_features),
    index=df.index
)

X = pd.concat([df[numeric_features], encoded], axis=1)
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


importances = pd.Series(model.feature_importances_, index=X.columns)
importances = importances.sort_values(ascending=True)

plt.figure(figsize=(10, 6))
importances.plot(kind='barh')
plt.title("Feature Importance for Predicting EV Range (km)")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.show()


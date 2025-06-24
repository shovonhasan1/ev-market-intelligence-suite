import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load cleaned data
df = pd.read_csv("cleaned_ev_data.csv")

# Convert non-numeric values to NaN
for col in ['acceleration_0_100_s', 'range_km', 'cargo_volume_l', 'efficiency_wh_per_km', 'seats']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values in relevant columns
df = df.dropna(subset=['acceleration_0_100_s', 'range_km', 'cargo_volume_l', 'efficiency_wh_per_km', 'seats'])
df = df.reset_index(drop=True)

# Select features for clustering
features = ['acceleration_0_100_s', 'range_km', 'cargo_volume_l', 'efficiency_wh_per_km', 'seats']
X = df[features]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['EV_Persona_Cluster'] = kmeans.fit_predict(X_scaled)

# Map cluster names for business context
persona_map = {
    0: 'City Commuter',
    1: 'Luxury Performance',
    2: 'Family Utility',
    3: 'Eco Efficiency'
}
df['EV_Persona_Label'] = df['EV_Persona_Cluster'].map(persona_map)

# Save the clustered data
df.to_csv("ev_clustered_output.csv", index=False)
print("Clustering complete and saved to ev_clustered_output.cs")

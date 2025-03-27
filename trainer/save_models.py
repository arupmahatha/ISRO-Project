import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Read and prepare data
df = pd.read_csv('cleaned_data.csv')

# Define features and target
X = df[['thetao', 'so', 'uo', 'vo', 'wo', 'kd', 'ph', 'spco2', 'o2', 'no3', 'po4', 'si', 'fe']]
y = df['chl']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train neural network
hidden_layers = [30, 35, 40, 45, 50, 45, 40, 35, 30]
nn = MLPRegressor(
    hidden_layer_sizes=hidden_layers,
    activation='relu',
    solver='adam',
    learning_rate_init=0.001,
    max_iter=1000,
    random_state=42
)

# Train neural network
for i in range(1000):
    nn.partial_fit(X_train_scaled, y_train)

# Initialize and train random forest
rf = RandomForestRegressor(
    n_estimators=100,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)
rf.fit(X_train_scaled, y_train)

# Save models and scaler
joblib.dump(nn, 'models/neural_network_model.joblib')
joblib.dump(rf, 'models/random_forest_model.joblib')
joblib.dump(scaler, 'models/scaler.joblib')

print("Models and scaler saved successfully!")

# Verify the saved models work
nn_loaded = joblib.load('models/neural_network_model.joblib')
rf_loaded = joblib.load('models/random_forest_model.joblib')
scaler_loaded = joblib.load('models/scaler.joblib')

# Test predictions with loaded models
X_test_scaled_loaded = scaler_loaded.transform(X_test)
nn_pred = nn_loaded.predict(X_test_scaled_loaded)
rf_pred = rf_loaded.predict(X_test_scaled_loaded)

print("\nVerification Results:")
print(f"Neural Network Test R2: {r2_score(y_test, nn_pred):.4f}")
print(f"Random Forest Test R2: {r2_score(y_test, rf_pred):.4f}") 
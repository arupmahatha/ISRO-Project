import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error, r2_score

def load_and_prepare_data():
    """
    Load and prepare the input data for prediction
    """
    # Load the processed data
    fe_data = pd.read_csv('../processed_data/fe.csv')
    uo_data = pd.read_csv('../processed_data/uo.csv')
    kd_data = pd.read_csv('../trainer/processed_data/kd.csv')  # Using kd from trainer data
    actual_chl = pd.read_csv('../processed_data/chl.csv')

    # Merge the dataframes on time, latitude, and longitude
    merged_data = fe_data.merge(uo_data, on=['time', 'latitude', 'longitude'], how='inner')
    merged_data = merged_data.merge(kd_data, on=['time', 'latitude', 'longitude'], how='inner')
    
    # Save the merged data time, lat, lon for later reference
    coords = merged_data[['time', 'latitude', 'longitude']]
    
    # Get actual chl values for comparison
    merged_data = merged_data.merge(actual_chl, on=['time', 'latitude', 'longitude'], how='left')
    
    return merged_data, coords

def prepare_features(data):
    """
    Prepare features in the same format as training data
    """
    # Select features in the same order as during training
    features = ['thetao', 'so', 'uo', 'vo', 'wo', 'kd', 'ph', 'spco2', 'o2', 'no3', 'po4', 'si', 'fe']
    X = data[features]
    return X

def main():
    # Load the saved model and scaler
    model = joblib.load('../trainer/models/neural_network_model.joblib')
    scaler = joblib.load('../trainer/models/scaler.joblib')
    
    # Load and prepare data
    data, coords = load_and_prepare_data()
    
    # Prepare features
    X = prepare_features(data)
    
    # Scale features
    X_scaled = scaler.transform(X)
    
    # Make predictions
    predictions = model.predict(X_scaled)
    
    # Create results dataframe
    results = coords.copy()
    results['predicted_chl'] = predictions
    results['actual_chl'] = data['chl']
    
    # Calculate metrics
    mse = mean_squared_error(results['actual_chl'], results['predicted_chl'])
    r2 = r2_score(results['actual_chl'], results['predicted_chl'])
    
    print(f"Prediction Results:")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R² Score: {r2:.4f}")
    
    # Save predictions
    results.to_csv('predictions.csv', index=False)
    print("\nPredictions saved to predictions.csv")

if __name__ == "__main__":
    main() 
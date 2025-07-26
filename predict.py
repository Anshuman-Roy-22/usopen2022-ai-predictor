import pandas as pd
import joblib
import json
import sys

# Load model and features
model = joblib.load("usopen_predictor_model.pkl")
with open("model_features.json") as f:
    feature_columns = json.load(f)

# Mock example
pract = {
    "elo_diff": 80,    # winner Elo - loser Elo
    "seed_diff": -2    # loser seed - winner seed
}

# Convert to DataFrame
df = pd.DataFrame([pract])[feature_columns]

# Predict win probability
proba = model.predict_proba(df)[0][1]  # probability calculated
print(f"Predicted win probability: {proba:.2%}")


import pandas as pd
import joblib
import json
import sys

# Load model and features
model = joblib.load("usopen_predictor_model.pkl")
with open("model_features.json") as f:
    feature_columns = json.load(f)

# Dummy example (normally you'd replace this with real input data)
example = {
    "elo_diff": 80,     # winner Elo - loser Elo
    "seed_diff": -2     # loser seed - winner seed
}

# Convert to DataFrame
df = pd.DataFrame([example])[feature_columns]

# Predict win probability
proba = model.predict_proba(df)[0][1]  # probability that "winner" wins
print(f"Predicted win probability: {proba:.2%}")


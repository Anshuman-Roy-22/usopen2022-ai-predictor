import argparse
import pandas as pd
import joblib
import json
from math import log10

# Load Elo model and feature names
model = joblib.load("model.joblib")
with open("model_features.json", "r") as f:
    feature_cols = json.load(f)

# Load match data
matches = pd.read_csv("data/processed/usopen_2022_matches.csv")
matches["match_date"] = pd.to_datetime(matches["start_date"], errors="coerce")
matches = matches.sort_values(["match_date", "round_order", "match_order"])

# Calculate Elo ratings
K = 32
base_elo = 1500 #Player Elo starts 1500
elo = {}

players = pd.unique(matches[["winner_name", "loser_name"]].values.ravel())
for p in players:
    elo[p] = base_elo

for _, row in matches.iterrows():
    w = row["winner_name"]
    l = row["loser_name"]

    # Handle missing players
    if pd.isna(w) or pd.isna(l):
        continue

    Ew = 1 / (1 + 10 ** ((elo[l] - elo[w]) / 400))
    El = 1 - Ew

    elo[w] += K * (1 - Ew)
    elo[l] += K * (0 - El)

# Command line args
parser = argparse.ArgumentParser()
parser.add_argument("--player1", required=True, help="Name of player 1")
parser.add_argument("--player2", required=True, help="Name of player 2")
args = parser.parse_args()

p1 = args.player1
p2 = args.player2

# Get current Elo and seed values
elo_p1 = elo.get(p1, base_elo)
elo_p2 = elo.get(p2, base_elo)

# Get seed info (100 set as default for unseeded)
def get_seed(player):
    recent = matches[
        (matches["winner_name"] == player) | (matches["loser_name"] == player)
    ].sort_values("match_date", ascending=False)

    if recent.empty:
        return 100  # default for unseeded
    row = recent.iloc[0]

    if row["winner_name"] == player:
        return row.get("winner_seed", 100) or 100
    else:
        return row.get("loser_seed", 100) or 100

seed_p1 = get_seed(p1)
seed_p2 = get_seed(p2)

# Create feature vector
elo_diff = elo_p1 - elo_p2
seed_diff = seed_p2 - seed_p1

X = pd.DataFrame([[elo_diff, seed_diff]], columns=feature_cols)

# Predict win probability
prob = model.predict_proba(X)[0][1]

# Apply sanity constraints
prob = max(min(prob, 0.95), 0.05)

# Compute baseline Elo estimate
def elo_to_win_prob(elo_diff):
    return 1 / (1 + 10 ** (-elo_diff / 400))

elo_baseline = elo_to_win_prob(elo_diff)

# Display results
print(f"\n {p1} vs {p2}")
print(f"Elo diff: {elo_diff:.1f}, Seed diff: {seed_diff}")
print(f"Model Win Probability: {prob:.1%}")
print(f"Elo-Based Estimate: {elo_baseline:.1%}\n")

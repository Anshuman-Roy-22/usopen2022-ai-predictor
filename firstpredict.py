import argparse
import json
import joblib
import pandas as pd

def main():
    # Parse command‐line args
    p = argparse.ArgumentParser(description="Predict US Open match win probability")
    p.add_argument("--elo_w",    type=float, required=True, help="Winner Elo rating")
    p.add_argument("--elo_l",    type=float, required=True, help="Loser  Elo rating")
    p.add_argument("--seed_w",   type=int,   default=100, help="Winner seed (100 if unseeded)")
    p.add_argument("--seed_l",   type=int,   default=100, help="Loser  seed (100 if unseeded)")
    args = p.parse_args()

    model = joblib.load("usopen_predictor_model.pkl")
    with open("model_features.json") as f:
        feat_cols = json.load(f)


    elo_diff  = args.elo_w - args.elo_l
    seed_diff = args.seed_l - args.seed_w
    df = pd.DataFrame([{"elo_diff": elo_diff, "seed_diff": seed_diff}])[feat_cols]

    prob = model.predict_proba(df)[0][1]  # probability that "winner" wins
    print(f"Win probability (given Elo diff {elo_diff:.1f}, seed diff {seed_diff}): {prob:.1%}")

if __name__=="__main__":
    main()

import argparse
import json
import joblib
import pandas as pd

def main():
    parser = argparse.ArgumentParser(
        description="Predict US Open match win probability"
    )
    parser.add_argument(
        "--elo_w", type=float, required=True,
        help="Winner Elo rating"
    )
    parser.add_argument(
        "--elo_l", type=float, required=True,
        help="Loser  Elo rating"
    )
    parser.add_argument(
        "--seed_w", type=int, default=100,
        help="Winner seed (100 if unseeded)"
    )
    parser.add_argument(
        "--seed_l", type=int, default=100,
        help="Loser  seed (100 if unseeded)"
    )
    args = parser.parse_args()

    # Load model and feature list
    model = joblib.load("usopen_predictor_model.pkl")  # or "model.joblib" if you didn't rename
    with open("model_features.json") as f:
        feat_cols = json.load(f)

    elo_diff  = args.elo_w - args.elo_l
    seed_diff = args.seed_l - args.seed_w
    df = pd.DataFrame([{"elo_diff": elo_diff, "seed_diff": seed_diff}])[feat_cols]

    prob = model.predict_proba(df)[0][1]
    print(
        f"Win probability (Elo diff {elo_diff:.1f}, seed diff {seed_diff}): {prob:.1%}"
    )

if __name__ == "__main__":
    main()

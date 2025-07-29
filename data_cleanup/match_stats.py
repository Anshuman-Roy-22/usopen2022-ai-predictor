import pandas as pd

pd.set_option("display.max_columns", None)

stats_raw = pd.read_csv("data/stats/match_stats_extended_2022.csv", header=None)

stat_cols = [
    "match_id",
    "tourney_slug",
    "match_stats_url_suffix",
    "winner_slug",
    "winner_serve_rating",
    "winner_aces",
    "winner_double_faults",
    "winner_first_serves_in",
    "winner_first_serves_total",
    "winner_first_serve_points_won",
    "winner_first_serve_points_total",
    "winner_second_serve_points_won",
    "winner_second_serve_points_total",
    "winner_break_points_saved",
    "winner_break_points_serve_total",
    "winner_service_games_played",
    "winner_return_rating",
    "winner_first_serve_return_won",
    "winner_first_serve_return_total",
    "winner_second_serve_return_won",
    "winner_second_serve_return_total",
    "winner_break_points_converted",
    "winner_break_points_return_total",
    "winner_return_games_played",
    "winner_service_points_won"
]
stats_raw.columns = stat_cols

stats = stats_raw.add_prefix("stats_")
stats = stats.rename(columns={"stats_match_id": "match_id"})

stats = stats[stats["match_id"].isin(usopen_matches["match_id"])]

usopen_matches = usopen_matches.merge(stats, on="match_id", how="left")

usopen_matches = usopen_matches.dropna(axis=1, how="all")

print("After merging all 25 stat fields:", usopen_matches.shape)
display(usopen_matches.head())

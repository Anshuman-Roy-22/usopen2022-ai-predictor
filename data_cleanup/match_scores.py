match_scores_path = "data/match_scores/match_scores_2020-2022.csv"

match_scores_columns = [
    "tourney_year_id",
    "tourney_order",
    "tourney_name",
    "tourney_slug",
    "tourney_url_suffix",
    "start_date",
    "start_year",
    "start_month",
    "start_day",
    "end_date",
    "end_year",
    "end_month",
    "end_day",
    "currency",
    "prize_money",
    "match_index",
    "tourney_round_name",
    "round_order",
    "match_order",
    "winner_name",
    "winner_player_id",
    "winner_slug",
    "loser_name",
    "loser_player_id",
    "loser_slug",
    "winner_seed",
    "loser_seed",
    "match_score_tiebreaks",
    "winner_sets_won",
    "loser_sets_won",
    "winner_games_won",
    "loser_games_won",
    "winner_tiebreaks_won",
    "loser_tiebreaks_won",
    "match_id",
    "match_stats_url_suffix"
]

match_scores = pd.read_csv(match_scores_path, header=None, names=match_scores_columns)
usopen_id = usopen_tourn["tourney_year_id"].iloc[0]
usopen_matches = match_scores[match_scores["tourney_year_id"] == usopen_id].copy()
print("US Open 2022 Match Scores (First 5 rows):")
display(usopen_matches.head())

import pandas as pd

column_names = [
    "tourney_year_id",
    "tourney_order",
    "tourney_type",
    "tourney_name",
    "tourney_id",
    "tourney_slug",
    "tourney_location",
    "tourney_date",
    "year",
    "tourney_month",
    "tourney_day",
    "tourney_singles_draw",
    "tourney_doubles_draw",
    "tourney_conditions",
    "tourney_surface",
    "tourney_fin_commit_raw",
    "currency",
    "tourney_fin_commit",
    "tourney_url_suffix",
    "singles_winner_name",
    "singles_winner_url",
    "singles_winner_player_slug",
    "singles_winner_player_id",
    "doubles_winner_1_name",
    "doubles_winner_1_url",
    "doubles_winner_1_player_slug",
    "doubles_winner_1_player_id",
    "doubles_winner_2_name",
    "doubles_winner_2_url",
    "doubles_winner_2_player_slug",
    "doubles_winner_2_player_id"
]

tourn_path = "data/tournaments/tournaments_2020-2022.csv"
tournaments = pd.read_csv(tourn_path, header=None, names=column_names)

usopen_tourn = tournaments[
    (tournaments["tourney_name"] == "US Open") & (tournaments["year"] == 2022)
].copy()

print("Filtered US Open 2022 Tournament:")
print(usopen_tourn[["tourney_year_id", "tourney_name", "year"]])

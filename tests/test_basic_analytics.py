from pyspark.sql import SparkSession

from src.analytics.batting_analytics import get_top_batsmen
from src.analytics.bowling_analytics import get_top_bowlers
from src.analytics.team_analytics import get_team_win_percentage
from src.analytics.venue_analytics import get_average_score, get_powerplay_analysis
from src.ranking.mvp_ranking import get_mvp_rankings


def test_basic_analytics():
    spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()

    delivery_data = [
        (1, 0, 1, "Player A", "Player B", 4, 0),
        (1, 0, 2, "Player A", "Player B", 6, 1),
        (2, 7, 1, "Player C", "Player A", 2, 0),
        (2, 7, 2, "Player C", "Player A", 3, 1),
    ]

    delivery_columns = ["match_id", "over", "ball", "batsman", "bowler", "runs", "is_wicket"]
    deliveries = spark.createDataFrame(delivery_data, delivery_columns)

    match_data = [
        (1, 2024, "Venue A", "Team A", "Team B", "Team A"),
        (2, 2024, "Venue B", "Team A", "Team C", "Team A"),
    ]

    match_columns = ["match_id", "season", "venue", "team1", "team2", "winner"]
    matches = spark.createDataFrame(match_data, match_columns)

    top_batsman = get_top_batsmen(deliveries).collect()[0]
    top_bowler = get_top_bowlers(deliveries).collect()[0]
    top_team = get_team_win_percentage(matches).collect()[0]
    top_venue = get_average_score(matches, deliveries).collect()[0]
    powerplay = get_powerplay_analysis(matches, deliveries).collect()[0]
    mvp = get_mvp_rankings(deliveries).collect()[0]

    assert top_batsman["batsman"] == "Player A"
    assert top_batsman["total_runs"] == 10

    assert top_bowler["bowler"] == "Player A"
    assert top_bowler["total_wickets"] == 1

    assert top_team["team"] == "Team A"
    assert top_team["matches_won"] == 2

    assert top_venue["venue"] == "Venue A"
    assert top_venue["average_score"] == 10

    assert powerplay["venue"] == "Venue A"
    assert powerplay["average_powerplay_score"] == 10

    assert mvp["player"] == "Player A"
    assert mvp["mvp_points"] == 35

    spark.stop()

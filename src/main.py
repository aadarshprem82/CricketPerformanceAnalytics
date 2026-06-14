import os

from pyspark.sql import SparkSession

from analytics.batting_analytics import save_orange_cap, save_top_batsmen
from analytics.bowling_analytics import save_purple_cap, save_top_bowlers
from analytics.team_analytics import save_team_win_percentage
from analytics.venue_analytics import save_average_score, save_powerplay_analysis
from ranking.mvp_ranking import save_mvp_rankings
from validation.validate_data import validate_deliveries, validate_matches


if not os.path.exists("data/matches.csv"):
    os.system("python data/generate_matches.py")

if not os.path.exists("data/deliveries.csv"):
    os.system("python data/generate_deliveries.py")

spark = SparkSession.builder.appName("CricketPerformanceAnalytics").getOrCreate()

matches = spark.read.csv("data/matches.csv", header=True, inferSchema=True)
deliveries = spark.read.csv("data/deliveries.csv", header=True, inferSchema=True)

validate_matches(matches)
validate_deliveries(deliveries)

save_top_batsmen(deliveries)
save_orange_cap(deliveries)

save_top_bowlers(deliveries)
save_purple_cap(deliveries)

save_team_win_percentage(matches)

save_average_score(matches, deliveries)
save_powerplay_analysis(matches, deliveries)

save_mvp_rankings(deliveries)

spark.stop()

print("Analytics completed successfully")

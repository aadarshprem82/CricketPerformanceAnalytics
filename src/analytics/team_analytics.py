from pyspark.sql.functions import col, count


def get_team_win_percentage(matches):
    total_matches = matches.select(col("team1").alias("team")).union(
        matches.select(col("team2").alias("team"))
    )

    total_matches = total_matches.groupBy("team").agg(count("team").alias("matches_played"))
    wins = matches.groupBy("winner").agg(count("winner").alias("matches_won"))

    result = total_matches.join(wins, total_matches.team == wins.winner, "left")
    result = result.fillna(0)
    result = result.withColumn("win_percentage", (col("matches_won") / col("matches_played")) * 100)
    result = result.select("team", "matches_played", "matches_won", "win_percentage")
    result = result.orderBy(col("win_percentage").desc())

    return result


def save_team_win_percentage(matches):
    team_win_percentage = get_team_win_percentage(matches)
    team_win_percentage.write.mode("overwrite").csv("output/team_win_percentage", header=True)

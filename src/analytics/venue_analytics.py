from pyspark.sql.functions import avg, col, sum


def get_average_score(matches, deliveries):
    scores = deliveries.groupBy("match_id").agg(sum("runs").alias("total_runs"))
    scores = scores.join(matches, "match_id")
    scores = scores.groupBy("venue").agg(avg("total_runs").alias("average_score"))
    scores = scores.orderBy(col("average_score").desc())
    return scores


def get_powerplay_analysis(matches, deliveries):
    powerplay = deliveries.filter(col("over") < 6)
    powerplay = powerplay.groupBy("match_id").agg(sum("runs").alias("powerplay_runs"))
    powerplay = powerplay.join(matches, "match_id")
    powerplay = powerplay.groupBy("venue").agg(avg("powerplay_runs").alias("average_powerplay_score"))
    powerplay = powerplay.orderBy(col("average_powerplay_score").desc())
    return powerplay


def save_average_score(matches, deliveries):
    average_score = get_average_score(matches, deliveries)
    average_score.write.mode("overwrite").csv("output/venue_analysis/average_score", header=True)


def save_powerplay_analysis(matches, deliveries):
    powerplay_analysis = get_powerplay_analysis(matches, deliveries)
    powerplay_analysis.write.mode("overwrite").csv("output/venue_analysis/powerplay_analysis", header=True)

from pyspark.sql.functions import col, sum


def get_mvp_rankings(deliveries):
    batting = deliveries.groupBy("batsman").agg(sum("runs").alias("total_runs"))
    bowling = deliveries.groupBy("bowler").agg(sum("is_wicket").alias("total_wickets"))

    batting = batting.withColumnRenamed("batsman", "player")
    bowling = bowling.withColumnRenamed("bowler", "player")

    rankings = batting.join(bowling, "player", "outer")
    rankings = rankings.fillna(0)
    rankings = rankings.withColumn("mvp_points", col("total_runs") + (col("total_wickets") * 25))
    rankings = rankings.orderBy(col("mvp_points").desc())

    return rankings


def save_mvp_rankings(deliveries):
    mvp_rankings = get_mvp_rankings(deliveries)
    mvp_rankings.write.mode("overwrite").csv("output/mvp_rankings", header=True)

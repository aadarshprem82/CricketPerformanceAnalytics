from pyspark.sql.functions import col, sum


def get_top_bowlers(deliveries):
    bowlers = deliveries.groupBy("bowler").agg(sum("is_wicket").alias("total_wickets"))
    bowlers = bowlers.orderBy(col("total_wickets").desc())
    return bowlers


def save_top_bowlers(deliveries):
    top_bowlers = get_top_bowlers(deliveries)
    top_bowlers.write.mode("overwrite").csv("output/top_bowlers", header=True)


def save_purple_cap(deliveries):
    purple_cap = get_top_bowlers(deliveries).limit(1)
    purple_cap.write.mode("overwrite").csv("output/purple_cap", header=True)

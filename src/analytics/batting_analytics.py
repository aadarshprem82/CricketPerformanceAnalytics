from pyspark.sql.functions import col, sum


def get_top_batsmen(deliveries):
    batsmen = deliveries.groupBy("batsman").agg(sum("runs").alias("total_runs"))
    batsmen = batsmen.orderBy(col("total_runs").desc())
    return batsmen


def save_top_batsmen(deliveries):
    top_batsmen = get_top_batsmen(deliveries)
    top_batsmen.write.mode("overwrite").csv("output/top_batsmen", header=True)


def save_orange_cap(deliveries):
    orange_cap = get_top_batsmen(deliveries).limit(1)
    orange_cap.write.mode("overwrite").csv("output/orange_cap", header=True)

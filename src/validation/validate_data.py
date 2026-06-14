from pyspark.sql.functions import col, count


def check_missing_values(data, columns):
    for column in columns:
        missing_count = data.filter(col(column).isNull()).count()

        if missing_count > 0:
            print(column, "has", missing_count, "missing values")
        else:
            print(column, "has no missing values")


def check_duplicate_matches(matches):
    duplicates = matches.groupBy("match_id").agg(count("match_id").alias("count"))
    duplicates = duplicates.filter(col("count") > 1)

    if duplicates.count() > 0:
        print("Duplicate match IDs found")
        duplicates.show()
    else:
        print("No duplicate match IDs found")


def validate_matches(matches):
    columns = ["match_id", "season", "venue", "team1", "team2", "winner"]
    check_missing_values(matches, columns)
    check_duplicate_matches(matches)


def validate_deliveries(deliveries):
    columns = ["match_id", "over", "ball", "batsman", "bowler", "runs", "is_wicket"]
    check_missing_values(deliveries, columns)

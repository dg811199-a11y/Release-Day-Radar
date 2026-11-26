# Add this as a NEW cell right after the existing PySpark cell (it uses `spark` and `processed_df`).
# It adds the two things the brief asks for that the first job does not do:
# cleaning the text and counting terms, plus an aggregation by film.
from pyspark.sql.functions import (col, lower, regexp_replace, split, explode,
                                   length, size, avg, count, desc, row_number)
from pyspark.sql.window import Window
from pyspark.ml.feature import StopWordsRemover

# 1. Clean: lowercase, remove <br /> tags, keep letters only, collapse spaces
clean_df = (processed_df
    .withColumn("Review_Clean", lower(col("Review")))
    .withColumn("Review_Clean", regexp_replace("Review_Clean", r"<br\s*/?>", " "))
    .withColumn("Review_Clean", regexp_replace("Review_Clean", r"[^a-z\s]", " "))
    .withColumn("Review_Clean", regexp_replace("Review_Clean", r"\s+", " "))
    .withColumn("Word_Count", size(split("Review_Clean", " "))))

print("Average words per review by label:")
clean_df.groupBy("Sentiment_Label").agg(avg("Word_Count").alias("Avg words")).show()

# 2. Count terms (drop stop words and very short tokens)
stop = StopWordsRemover.loadDefaultStopWords("english")
words = (clean_df
    .select("Sentiment_Label", explode(split("Review_Clean", " ")).alias("word"))
    .filter((length("word") > 2) & (~col("word").isin(stop))))

counts = words.groupBy("Sentiment_Label", "word").agg(count("*").alias("n"))
w = Window.partitionBy("Sentiment_Label").orderBy(desc("n"))
top_terms = counts.withColumn("rank", row_number().over(w)).filter(col("rank") <= 15)
top_terms.orderBy("Sentiment_Label", "rank").show(30, truncate=False)

# 3. Aggregate by film: the 800 YouTube comments
yt = spark.read.csv("sentiment_analysis_results.csv", header=True, inferSchema=True, multiLine=True, escape='"')
(yt.withColumn("Comment_Length", length(col("Comment text")))
   .groupBy("Movie name")
   .agg(count("*").alias("Comments"),
        avg("Comment_Length").alias("Avg length (chars)"),
        avg("Sentiment Score").alias("Avg VADER score"))
   .orderBy(desc("Avg VADER score"))
   .show(truncate=False))

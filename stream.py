# HIGH-LEVEL SAMPLE — fill in the rest yourself
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg

spark = SparkSession.builder.appName("SensorStream").getOrCreate()

df = spark.readStream.format("kafka") \
    .option("subscribe", "sensor-data") \
    .load()

# TODO:
#   1. define a schema for {sensor_id, temperature, timestamp}
#   2. parse the Kafka 'value' column (bytes -> string -> JSON) using from_json + the schema
#   3. groupBy("sensor_id") and compute avg("temperature")
#   4. writeStream to the console sink with outputMode("complete") and call awaitTermination()

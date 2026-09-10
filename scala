import org.apache.spark.sql.functions._

val dfWithKey = df.withColumn(
  "generated_asset_primary_key",
  sha2(
    concat_ws(
      "||",
      coalesce(col("profile").cast("string"), lit("")),
      coalesce(col("record_creation_timestamp").cast("string"), lit("")),
      coalesce(col("site_country").cast("string"), lit("")),
      coalesce(col("cust_id").cast("string"), lit("")),
      coalesce(col("client_id").cast("string"), lit("")),
      coalesce(col("timestamp_epoch").cast("string"), lit("")),
      coalesce(col("event_type").cast("string"), lit(""))
    ),
    256
  )
)
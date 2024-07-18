from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("ReadParquetData").getOrCreate()

# Define the path to your Parquet file or directory
dataPath = "data.parquet"  # Adjust for single file or directory

# Read the Parquet data into a DataFrame
df = spark.read.parquet(dataPath)

# Now you can work with the DataFrame 'df'
df.display() # This displays the first 20 rows of the DataFrame
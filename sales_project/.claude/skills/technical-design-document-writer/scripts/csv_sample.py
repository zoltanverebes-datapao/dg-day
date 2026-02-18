#!/usr/bin/env python3
"""
USAGE: python csv_sample.py <volume_path> <sample_size>
EXAMPLE: python csv_sample.py "/Volumes/main/default/my_vol/data.csv" 10
DESCRIPTION: Connects to Databricks via DatabricksSession to randomly sample a CSV from a Volume.
"""

import sys
from databricks.connect import DatabricksSession
from pyspark.sql import functions as F

def get_csv_sample(volume_path, n=20):
    # Initialize the remote session
    spark = DatabricksSession.builder.getOrCreate()
    
    # Load with schema inference to help Claude understand data types
    df = (spark.read.format("csv")
          .option("header", "True")
          .option("inferSchema", "True")
          .load(volume_path))
    
    # Randomly shuffle and take N rows
    # We use orderBy(rand) for a guaranteed count of N
    sample_pd = df.orderBy(F.rand()).limit(int(n)).toPandas()
    
    # Output as Markdown so Claude can parse the table easily in its terminal
    print(sample_pd.to_markdown(index=False))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__) # Prints the usage instructions if Claude forgets args
        sys.exit(1)
    
    path = sys.argv[1]
    count = sys.argv[2] if len(sys.argv) > 2 else 20
    get_csv_sample(path, count)
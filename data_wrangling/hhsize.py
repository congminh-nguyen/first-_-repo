# Import libraries
import polars as pl
import numpy as np

# Function to compute household size    
def compute_size_hh(df):
    return df.group_by("household_id").agg(
        pl.count("person").alias("size_hh")
    )



# Import libraries
import polars as pl
import numpy as np

# Function to compute mean and total income
def compute_mean_total_income(df):
    return df.group_by("household_id").agg([
        pl.col("income").mean().alias("mean_income"),
        pl.col("income").sum().alias("total_income")
    ])

# Function to compute main earner female
def compute_main_earner_female(df):
    return df.group_by("household_id").agg([
        pl.col("income").max().alias("max_income"),
        pl.col("female").filter(pl.col("income") == pl.col("income").max()).first().alias("main_earner_female")
    ]).with_columns(
        pl.when(pl.col("main_earner_female")).then(pl.lit("yes")).otherwise(pl.lit("no")).alias("main_earner_female")
    )


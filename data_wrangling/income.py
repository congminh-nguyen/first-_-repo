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
    return df.group_by("household_id").agg(
        (pl.col("income").arg_max() == pl.col("female")).alias("main_earner_female")
    ).with_column(
        pl.when(pl.col("main_earner_female")).then("yes").otherwise("no")
    )


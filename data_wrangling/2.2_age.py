# Mean age per household
def compute_mean_age(df)
    return df.group_by("household_id").agg(
        pl.col("age").mean().alias("mean_age")
    )

# Min and max age per household
def compute_min_max_age(df) 
    return df.group_by("household_id").agg([
        pl.col("age").min().alias("min_age"),
        pl.col("age").max().alias("max_age")
    ])

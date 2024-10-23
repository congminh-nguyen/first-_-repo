# Number of females per household
def compute_nr_female(df):
    return df.group_by("household_id").agg(
        pl.col("female").sum().alias("nr_female")
    )

# Number of children per household
def compute_nr_children(df):
    return df.group_by("household_id").agg(
        (pl.col("age") < 18).sum().alias("nr_children")
    )

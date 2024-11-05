# Import libraries
import polars as pl


def compute_mean_age(df: pl.DataFrame) -> pl.DataFrame:
    """
    Calculate the mean age for each household.

    Args:
        df (pl.DataFrame): Input DataFrame containing household_id and age
        columns

    Returns:
        pl.DataFrame: DataFrame with household_id and mean_age columns
    """
    return df.group_by("household_id").agg(
        pl.col("age").mean().alias("mean_age")
    )


def compute_min_max_age(df: pl.DataFrame) -> pl.DataFrame:
    """
    Calculate the minimum and maximum age for each household.

    Args:
        df (pl.DataFrame): Input DataFrame containing household_id and age
        columns

    Returns:
        pl.DataFrame: DataFrame with household_id, min_age and max_age columns
    """
    return df.group_by("household_id").agg([
        pl.col("age").min().alias("min_age"),
        pl.col("age").max().alias("max_age")
    ])

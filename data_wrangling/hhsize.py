# Import libraries
import polars as pl


def compute_size_hh(df: pl.DataFrame) -> pl.DataFrame:
    """
    Calculate the number of people in each household.

    Args:
        df (pl.DataFrame): Input DataFrame containing household_id and person
        columns

    Returns:
        pl.DataFrame: DataFrame with household_id and size_hh columns
    """
    return df.group_by("household_id").agg(
        pl.count("person").alias("size_hh")
    )

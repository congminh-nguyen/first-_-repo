# Import libraries
import polars as pl


def compute_nr_female(df: pl.DataFrame) -> pl.DataFrame:
    """
    Calculate the number of females in each household.

    Args:
        df (pl.DataFrame): Input DataFrame containing household_id and female
        columns

    Returns:
        pl.DataFrame: DataFrame with household_id and nr_female columns
    """
    return df.group_by("household_id").agg(
        pl.col("female").sum().alias("nr_female")
    )


def compute_nr_children(df: pl.DataFrame) -> pl.DataFrame:
    """
    Calculate the number of children (age < 18) in each household.

    Args:
        df (pl.DataFrame): Input DataFrame containing household_id and age
        columns

    Returns:
        pl.DataFrame: DataFrame with household_id and nr_children columns
    """
    return df.group_by("household_id").agg(
        (pl.col("age") < 18).sum().alias("nr_children")
    )

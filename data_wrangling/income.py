# Import libraries
import polars as pl


def compute_mean_total_income(df: pl.DataFrame) -> pl.DataFrame:
    """
    Calculate the mean and total income for each household.

    Args:
        df (pl.DataFrame): Input DataFrame containing household_id and income
        columns

    Returns:
        pl.DataFrame: DataFrame with household_id, mean_income and total_income
        columns
    """
    return df.group_by("household_id").agg([
        pl.col("income").mean().alias("mean_income"),
        pl.col("income").sum().alias("total_income")
    ])


def compute_main_earner_female(df: pl.DataFrame) -> pl.DataFrame:
    """
    Determine if the main income earner in each household is female.
    The main earner is the person with the highest income in the household.

    Args:
        df (pl.DataFrame): Input DataFrame containing household_id, income and
        female columns

    Returns:
        pl.DataFrame: DataFrame with household_id, max_income and
        main_earner_female columns. main_earner_female is "yes" if the main
        earner is female, "no" otherwise.
    """
    return df.group_by("household_id").agg([
        pl.col("income").max().alias("max_income"),
        pl.col("female").filter(
            pl.col("income") == pl.col("income").max()
        ).first().alias("main_earner_female")
    ]).with_columns(
        pl.when(pl.col("main_earner_female")).then(
            pl.lit("yes")
        ).otherwise(pl.lit("no")).alias("main_earner_female")
    )

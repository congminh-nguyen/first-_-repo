# Import libraries
import polars as pl
from age import compute_mean_age, compute_min_max_age
from income import compute_mean_total_income, compute_main_earner_female
from hhsize import compute_size_hh
from fem_child import compute_nr_children, compute_nr_female


def compute_household_features(df: pl.DataFrame) -> pl.DataFrame:
    """
    Integrate all household features by joining
    the results of various computations.

    Args:
        df (pl.DataFrame): Input DataFrame containing
        household data with columns:
            - household_id: Unique identifier for each household
            - person: Person number within household
            - age: Age of person
            - income: Income value
            - female: Boolean indicating if person is female

    Returns:
        pl.DataFrame: DataFrame with household_id and computed features:
            - size_hh: Number of people in household
            - mean_age: Average age in household
            - min_age: Minimum age in household
            - max_age: Maximum age in household
            - nr_children: Number of children (age < 18) in household
            - nr_female: Number of females in household
            - mean_income: Mean income in household
            - total_income: Total income in household
            - max_income: Maximum income in household
            - main_earner_female: Whether highest earner is female ("yes"/"no")
    """
    size_hh = compute_size_hh(df)
    mean_age = compute_mean_age(df)
    min_max_age = compute_min_max_age(df)
    nr_children = compute_nr_children(df)
    nr_female = compute_nr_female(df)
    mean_total_income = compute_mean_total_income(df)
    main_earner_female = compute_main_earner_female(df)

    return (size_hh.join(mean_age, on="household_id")
            .join(min_max_age, on="household_id")
            .join(nr_children, on="household_id")
            .join(nr_female, on="household_id")
            .join(mean_total_income, on="household_id")
            .join(main_earner_female, on="household_id"))

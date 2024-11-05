# Import libraries
import polars as pl
import numpy as np


def generate_random_data(n_households: int, seed: int) -> pl.DataFrame:
    """
    Generate random household data with multiple people per household.

    Args:
        n_households (int): Number of households to generate
        seed (int): Random seed for reproducibility

    Returns:
        pl.DataFrame: DataFrame containing simulated
        household data with columns:
            - household_id: Unique identifier for each household
            - person: Person number within household (1 to 4)
            - age: Age of person (1 to 99)
            - income: Income value (0 to 99, with ~10% NaN values)
            - female: Boolean indicating if person is female
    """
    np.random.seed(seed)  # Set seed for reproducibility
    # 1 to 4 people per household
    n_people = np.random.randint(1, 5, size=n_households)
    # Create household ids
    household_id = np.repeat(np.arange(1, n_households + 1), n_people)
    # Create person ids
    person = np.concatenate([np.arange(1, n + 1) for n in n_people])
    age = np.random.randint(1, 100, size=len(person))  # Create ages
    # Create incomes
    income = np.random.randint(0, 100, size=len(person)).astype(float)
    # Add some NaN values in income
    # Add ~10% NaN values randomly
    mask = np.random.rand(len(income)) < 0.1
    income[mask] = np.nan
    female = np.random.choice([0, 1], size=len(person))  # Gender
    df = pl.DataFrame({
        "household_id": household_id,
        "person": person,
        "age": age,
        "income": income,
        "female": female
    })
    return df

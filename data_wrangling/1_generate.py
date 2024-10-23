# Function to generate random data
def generate_random_data(n_households, seed):
    np.random.seed(seed) # Set seed for reproducibility
    n_people = np.random.randint(1, 5, size=n_households)  # 1 to 4 people per household
    household_id = np.repeat(np.arange(1, n_households + 1), n_people) # Create household ids
    person = np.concatenate([np.arange(1, n + 1) for n in n_people]) # Create person ids
    age = np.random.randint(1, 100, size=len(person)) # Create ages
    income = np.random.randint(0, 100, size=len(person)).astype(float) # Create incomes
    income[np.random.rand(len(income)) < 0.1] = np.nan # Add some NaN values in income
    female = np.random.choice([True, False], size=len(person)) # Create genders
    df = pl.DataFrame({
        'household_id': household_id,
        'person': person,
        'age': age,
        'income': income,
        'female': female
    })
    return df


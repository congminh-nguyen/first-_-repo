# Import libraries
import numpy as np
import generate, age, income, hhsize, fem_child

# Function to integrate all features
def compute_household_features(df):
    size_hh = hhsize.compute_size_hh(df)
    mean_age = age.compute_mean_age(df)
    min_max_age = age.compute_min_max_age(df)
    nr_children = fem_child.compute_nr_children(df)
    nr_female = fem_child.compute_nr_female(df)
    mean_total_income = income.compute_mean_total_income(df)
    main_earner_female = income.compute_main_earner_female(df)
    
    return size_hh.join(mean_age, on="household_id")\
                  .join(min_max_age, on="household_id")\
                  .join(nr_children, on="household_id")\
                  .join(nr_female, on="household_id")\
                  .join(mean_total_income, on="household_id")\
                  .join(main_earner_female, on="household_id")





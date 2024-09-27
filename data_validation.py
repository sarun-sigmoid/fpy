# Description: This file processes the data.csv file and validates the data

import pandas as pd

# Read the data.csv file
data = pd.read_csv('data.csv')

# write a function to validate the salary column
def validate_salary(salary):
    try:
        salary = float(salary)
        if salary < 0:
            return False
        return True
    except:
        return False
    
# write a function to validate the age column
def validate_age(age):
    try:
        age = int(age)
        if age < 0:
            return False
        return True
    except:
        return False

# write a function to validate the experience column
def validate_experience(experience):
    try:
        experience = int(experience)
        if experience < 0:
            return False
        return True
    except:
        return False
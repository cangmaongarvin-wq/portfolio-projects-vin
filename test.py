
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)

employees = {
    "name": ["Ana", "Ben", "Cara", "David", "Ella", "Finn"],
    "department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "salary": [50000, 32000, 48000, 41000, 29000, 55000],
    "performance_score": [92, 75, 88, 95, 68, 81],
    "years_experience": [5, 2, 4, 6, 1, 7]
}

employees_df = pd.DataFrame(employees)

# 1.
print(employees_df[np.logical_and(employees_df['salary']>40000,
                                  employees_df['performance_score']>85)]
                                  )
# 2.
print(employees_df[np.logical_or(employees_df['department'] == "HR",
                                 employees_df['salary'] < 30000)]
                                 )
# 3. 
print(employees_df[~
                   (employees_df['department'] == "Sales")])
# 4.
score = 88
if score >= 90:
    print('Outstanding')
elif score < 90 or score >= 80:
    print('Good')
else:
    print('Needs Improvement')
# 5.
experience = 4
if experience >= 5:
    print('Senior')
elif experience >= 3:
    print('Mid')
else:
    print('Junior')
# 6.
employees_df['performance_level'] = np.where(
    employees_df['performance_score'] >= 90, "Outstanding", 
    np.where(employees_df["performance_score"] >= 80, 
             'Good', 'Needs Improvement')
             )
# 7.
employees_df['salary_level'] = np.where(
    employees_df['salary'] >= 50000, "High",
    np.where(employees_df['salary'] >= 40000,
             'Medium', 'Low')
             )
# 8
employees_df['experience_level'] = np.where(
    employees_df['years_experience'] >= 5, 'Senior',
    np.where(employees_df['years_experience'] >= 3,
             'Mid Level', 'Junior')
             )
# 9
print(employees_df[np.logical_and(employees_df['salary_level'] == "High",
                                  employees_df['performance_level'] == "Outstanding")]
                                  )
# 10
print(employees_df[np.logical_and(
    np.logical_or(employees_df['experience_level'] == "Mid Level", employees_df['experience_level'] == "Senior"),
                                  employees_df['performance_score'] >= 80)]
                                  )
# 11.
candidate_salary = 51000
candidate_score = 80
print()
if candidate_salary <= 50000 and candidate_score >= 90:
    print('Hire Immediately')
elif candidate_score >= 80:
    print('Consider')
else:
    print('Reject')

print(employees_df)
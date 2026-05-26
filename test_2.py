
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

students = {
    "name": ["Alex", "Bianca", "Carlos", "Diana", "Ethan", "Faith"],
    "subject": ["Math", "Science", "Math", "English", "Science", "English"],
    "score": [92, 76, 84, 67, 95, 81],
    "study_hours": [15, 8, 12, 5, 18, 10],
    "attendance": [96, 82, 88, 70, 99, 91]
}

students_df = pd.DataFrame(students)

print(students_df)
# 1.
print(students_df[np.logical_and(students_df['score'] > 80,
                                 students_df['attendance'] >=90)])
# 2.
print(students_df[np.logical_or(students_df['subject'] == "Science",
                                students_df['study_hours'] < 10)])
# 3.
print(students_df[~(students_df['subject'] == "English")])
# 4.
score = 80
if score >= 90:
    print("Excellent")
elif score <90 and score >= 80:
    print("Good")
else:
    print("Needs Work")
# 5.
attendance = 79
if attendance >= 95:
    print("Perfect")
elif attendance < 95 and attendance >= 80:
    print("Acceptable")
else:
    print("Low")
# 6.
students_df['score_level'] = np.where(
    students_df['score'] >= 90, 'Excellent',
    np.where(students_df['score'] >=80, 'Good', 'Needs Work')
)
# 7.
students_df['attendance_level'] = np.where(
    students_df['attendance'] >= 95, "High",
    np.where(students_df['attendance'] >= 80, "Medium", "Low")
)
# 8.
students_df['study_level'] = np.where(
    students_df['study_hours'] >= 15, "Heavy",
    np.where(students_df['study_hours'] >=10, "Moderate", "Light")
)
print(students_df)
# 9.
excel_students = students_df[np.logical_and(
    students_df['score_level'] == "Excellent",
    students_df['attendance_level'] == "High"
)]
print(excel_students)
# 10.
heavy_studs = students_df[np.logical_and(
    np.logical_or(
    students_df['study_level'] == "Moderate", students_df['study_level'] == "Heavy"),
    students_df['score'] >= 80)]
print(heavy_studs)
# 11.
exam_score = 95
attendance_rate = 75

if exam_score >= 90 and attendance_rate >= 95:
    print('Pass with Honors')
elif exam_score >= 75:
    print('Pass')
else:
    print('Fail')

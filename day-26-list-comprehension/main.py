import random

numbers = [1, 2, 3]
new_number = [n + 1 for n in numbers]

# print(new_number)

# List Comprehension Example
# Great example of a list comprehension. This creates a new list based on values from another list
# [state for state in all_states if state not in guessed states]


# Dictionary Comprehension
#

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_score = {student: random.randint(1, 100) for student in names}
print(student_score)

passed_student = {student: score for (student, score) in student_score.items() if score >= 60}
print(passed_student)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow"
# result = {n:len(n) for n in sentence.split()}
# print(result)
# print(sentence.split())

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_c = {day: (value * 9 / 5 + 32) for (day, value) in weather_c.items()}
print(weather_c)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# for (key, value) in student_dict.items():
#     print(value)
for (index, row) in student_data_frame.iterrows():
    print(row.student)

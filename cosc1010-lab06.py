# Ireeann Anderson
# UWYO COSC 1010
# Submission Date: 10/15/2024
# HW 01
# Lab Section: 16
# Sources, people worked with, help given to:
# your
# comments
# here
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student and their scores
# in different subjects.

# Student Data
students = [
    {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
    {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
    {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
    {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
]

# Dictionary to store the average scores
average_scores = {}

# Calculate the average score for each student
for student in students:
    scores = student["scores"].values()  # Get the scores for the student
    average = sum(scores) / len(scores)  # Calculate the average
    average_scores[student["name"]] = average  # Store in the dictionary

# Print the names of students whose average score is greater than 80
for name, avg in average_scores.items():
    if avg > 80:
        print(f"{name} has an average score of {avg:.2f}, which is greater than 80.")

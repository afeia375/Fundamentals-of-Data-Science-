1. Scenario: You are working on a project that involves analyzing student performance data for a class of 32 students. The data is stored in a NumPy array named student_scores, where each row represents a student and each column represents a different subject. The subjects are arranged in the following order: Math, Science, English, and History. Your task is to calculate the average score for each subject and identify the subject with the highest average score. Question: How would you use NumPy arrays to calculate the average score for each subject and determine the subject with the highest average score? Assume 4x4 matrix that stores marks of each student in given order.
   import numpy as np
student_scores = np.array([
    [85, 78, 92, 88],
    [90, 82, 85, 79],
    [76, 88, 89, 91],
    [95, 84, 94, 86]
])
subjects = ["Math", "Science", "English", "History"]
subject_averages = np.mean(student_scores, axis=0)

print("Average scores:")
for subject, average in zip(subjects, subject_averages):
    print(subject, ":", average)
highest_index = np.argmax(subject_averages)
highest_subject = subjects[highest_index]
print("\nSubject with highest average:", highest_subject)
print("Highest average score:", subject_averages[highest_index])

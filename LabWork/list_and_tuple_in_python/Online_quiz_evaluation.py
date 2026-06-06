"""
7. Online Quiz Evaluation
Problem Statement
Correct answers:
correct = ['A', 'C', 'B', 'D', 'A']
Student answers:
student = ['A', 'B', 'B', 'D', 'C']
Write a program to:
•
Calculate score.
•
Display incorrectly answered question numbers.
•
Count correct and wrong answers.
•
Determine pass/fail (minimum 60%).
"""

# Correct answers
correct = ['A', 'C', 'B', 'D', 'A']

# Student answers
student = ['A', 'B', 'B', 'D', 'C']

score = 0
correct_count = 0
wrong_count = 0

print("Incorrectly Answered Questions:")

for i in range(len(correct)):

    if correct[i] == student[i]:
        score += 1
        correct_count += 1
    else:
        wrong_count += 1
        print(i + 1)

percentage = (score * 100) / len(correct)

print("\nScore:", score)
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)

if percentage >= 60:
    print("Pass")
else:
    print("Fail")
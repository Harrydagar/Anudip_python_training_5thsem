"""
2.Cricket Tournament Scorecard
Problem Statement
A batsman's scores in different matches are stored in a list.
scores = [45, 78, 12, 100, 67, 8, 90, 55]
Write a program to:
• Count half-centuries and centuries.
• Find the highest score.
• Display all scores below 20.
• Calculate the average score
"""

# Scores of batsman in different matches
scores = [45, 78, 12, 100, 67, 8, 90, 55]

# Counters for half-centuries and centuries
half_century = 0
century = 0

# Assume first score is highest
highest_score = scores[0]

# Variable to calculate total runs
total_runs = 0

print("Scores Below 20:")

# Process all scores
for score in scores:

    # Count centuries
    if score >= 100:
        century += 1

    # Count half-centuries
    elif score >= 50:
        half_century += 1

    # Find highest score
    if score > highest_score:
        highest_score = score

    # Display scores below 20
    if score < 20:
        print(score)

    # Add score to total
    total_runs += score

# Calculate average score
average = total_runs / len(scores)

print("\nHalf-Centuries:", half_century)
print("Centuries:", century)
print("Highest Score:", highest_score)
print("Average Score:", average)

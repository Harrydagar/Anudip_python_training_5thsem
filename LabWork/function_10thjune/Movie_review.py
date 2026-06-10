"""
3. Movie Review Sentiment Analyzer
Problem Statement
Movie reviews are stored as follows:
reviews = [ "excellent movie", "average story", "excellent acting", "poor direction", "excellent visuals", "poor screenplay", "good music", "excellent climax", "average performance", "good cinematography" ]
Requirements
Create the following functions:
1. count_sentiments(reviews)
Counts:
•
Excellent
•
Good
•
Average
•
Poor reviews
2. most_common_word(reviews)
Returns the most frequently occurring word.
3. longest_review(reviews)
Returns the review containing the maximum number of characters.
4. reviews_with_keyword(reviews, keyword)
Displays all reviews containing a given keyword.
Sample Output
Excellent Reviews: 4 Good Reviews: 2 Average Reviews: 2 Poor Reviews: 2 Most Common Word: excellent Longest Review: good cinematography Reviews containing 'excellent': excellent movie excellent acting excellent visuals excellent climax"""

# Movie Review Sentiment Analyzer

reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# Function to count sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for review in reviews:
        if "excellent" in review:
            excellent += 1
        elif "good" in review:
            good += 1
        elif "average" in review:
            average += 1
        elif "poor" in review:
            poor += 1

    return excellent, good, average, poor

# Function to find most common word
def most_common_word(reviews):
    word_count = {}

    for review in reviews:
        words = review.split()

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    max_word = ""
    max_count = 0

    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word

    return max_word

# Function to find longest review
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review

    return longest

# Function to display reviews containing keyword
def reviews_with_keyword(reviews, keyword):
    print("Reviews containing", keyword, ":")

    for review in reviews:
        if keyword.lower() in review.lower():
            print(review)

# Main Program
excellent, good, average, poor = count_sentiments(reviews)

print("Excellent Reviews:", excellent)
print("Good Reviews:", good)
print("Average Reviews:", average)
print("Poor Reviews:", poor)

print("Most Common Word:", most_common_word(reviews))
print("Longest Review:", longest_review(reviews))

reviews_with_keyword(reviews, "excellent")
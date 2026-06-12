# Student Resume Analyzer

import re

resume = """
Name: Harry Sharma

Email: harry@gmail.com
Phone: 9876543210

Education:
B.Tech Computer Science

Skills:
Python, Java, SQL, React, Python, Communication,
Java, Python, SQL, React, Leadership

Projects:
Student Management System using Python and SQL.
E-commerce Website using React and Java.

Achievements:
Won Coding Competition.
Completed AI Certification.
"""

words = resume.split()

total_words = len(words)
total_characters = len(resume)

emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', resume)
phones = re.findall(r'\b\d{10}\b', resume)

skill_list = [
    "Python", "Java", "SQL", "React",
    "Communication", "Leadership"
]

skill_freq = {}

for skill in skill_list:
    count = resume.lower().count(skill.lower())
    if count > 0:
        skill_freq[skill] = count

most_frequent_skill = max(skill_freq, key=skill_freq.get)

word_freq = {}

for word in words:
    word = word.lower().strip(",.:")
    word_freq[word] = word_freq.get(word, 0) + 1

repeated_keywords = [w for w, c in word_freq.items() if c > 1]
most_frequent_word = max(word_freq, key=word_freq.get)

duplicate_skills = [
    skill for skill, count in skill_freq.items()
    if count > 1
]

print("RESUME ANALYSIS REPORT")
print("-" * 50)

print("Total Words:", total_words)
print("Total Characters:", total_characters)

print("\nEmail IDs Found:")
for email in emails:
    print(email)

print("\nPhone Numbers Found:")
for phone in phones:
    print(phone)

print("\nSkills Mentioned:", len(skill_freq))
print("Most Frequent Skill:", most_frequent_skill)

print("\nRepeated Keywords:")
print(repeated_keywords)

print("\nMost Frequently Used Word:")
print(most_frequent_word)

print("\nSKILL FREQUENCY REPORT")
for skill, count in skill_freq.items():
    print(skill, ":", count)

print("\nDuplicate Skills:")
print(duplicate_skills)

print("\nSUMMARY DASHBOARD")
print("Total Words:", total_words)
print("Total Characters:", total_characters)
print("Email Found:", len(emails))
print("Phone Numbers Found:", len(phones))
print("Most Frequent Skill:", most_frequent_skill)

print("\nTop 5 Keywords:")
top_keywords = sorted(
    word_freq.items(),
    key=lambda x: x[1],
    reverse=True
)[:5]

for word, count in top_keywords:
    print(word, "-", count)
# News Article Text Analyzer

article = """
Artificial intelligence is changing the world rapidly. Many industries are
using artificial intelligence to improve efficiency and productivity.
Education, healthcare, transportation, banking, and agriculture are all
benefiting from modern technologies. Students use online learning platforms
to gain knowledge and improve skills. Teachers use technology to create
interactive lessons. Hospitals use intelligent systems to analyze medical
records and assist doctors in diagnosis. Farmers use weather forecasts and
data analysis to improve crop production.

Technology also creates new opportunities for businesses. Companies analyze
customer preferences and market trends to make better decisions. Digital
communication allows people to connect instantly across the world. Social
media platforms provide information, entertainment, and business promotion.
At the same time, experts discuss issues related to privacy, cybersecurity,
and responsible technology use.

Governments invest in research and innovation to support economic growth.
Universities encourage students to participate in scientific projects and
develop creative solutions to real-world problems. Artificial intelligence
and machine learning are expected to play an important role in future
development. Organizations continue to adopt digital tools to remain
competitive and improve customer satisfaction. Technology continues to evolve
and influence nearly every aspect of modern life. People who develop strong
technical and communication skills will have greater opportunities in the
future. Continuous learning and adaptation are essential for success in a
rapidly changing world.
"""

import string

total_characters = len(article)
words = article.split()
total_words = len(words)

sentences = article.count('.') + article.count('!') + article.count('?')

vowels = 0
consonants = 0

for ch in article.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

clean_words = [
    word.strip(string.punctuation).lower()
    for word in words
]

freq = {}

for word in clean_words:
    freq[word] = freq.get(word, 0) + 1

longest_word = max(clean_words, key=len)
shortest_word = min(clean_words, key=len)
most_frequent = max(freq, key=freq.get)

once_words = [w for w, c in freq.items() if c == 1]
more_than_five = [w for w, c in freq.items() if c > 5]

alphabet_count = {}

for word in clean_words:
    first = word[0].upper()
    alphabet_count[first] = alphabet_count.get(first, 0) + 1

unique_words = sorted(set(clean_words))

avg_word_length = sum(len(w) for w in clean_words) / len(clean_words)

print("NEWS ARTICLE ANALYSIS")
print("-" * 50)

print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Total Sentences:", sentences)
print("Vowels:", vowels)
print("Consonants:", consonants)

print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Most Frequent Word:", most_frequent)

print("\nWords Appearing Once:")
print(once_words)

print("\nWords Appearing More Than 5 Times:")
print(more_than_five)

print("\nWord Frequencies:")
for k, v in freq.items():
    print(k, ":", v)

print("\nWords Starting With Each Alphabet:")
for k, v in sorted(alphabet_count.items()):
    print(k, ":", v)

print("\nUnique Words:")
print(unique_words)

print("\nTEXT SUMMARY")
print("Total Words:", total_words)
print("Total Sentences:", sentences)
print("Average Word Length:", round(avg_word_length, 2))
print("Most Frequent Word:", most_frequent)
print("Vocabulary Size:", len(unique_words))
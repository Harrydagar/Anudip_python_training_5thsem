msg = "Python is awesome and Python is easy to learn"

words = msg.split()

longest = words[0]
shortest = words[0]

python_count = 0
vowels = 0
consonants = 0
vowel_list = "aeiouAEIOU"

more4 = []

for w in words:
    if len(w) > len(longest):
        longest = w
    if len(w) < len(shortest):
        shortest = w
    if w == "Python":
        python_count += 1
    if len(w) > 4:
        more4.append(w)

for ch in msg:
    if ch.isalpha():
        if ch in vowel_list:
            vowels += 1
        else:
            consonants += 1

vowel_words = []
for w in words:
    if w[0] in vowel_list:
        vowel_words.append(w)

print("Total Characters:", len(msg))
print("Total Words:", len(words))
print("Longest Word:", longest)
print("Shortest Word:", shortest)
print("Occurrences of Python:", python_count)
print("Words > 4 chars:", more4)
print("Vowels:", vowels)
print("Consonants:", consonants)
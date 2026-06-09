review = "This product is excellent excellent excellent and very useful"

words = review.split()

freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

most = ""
maxc = 0

once = []
more5 = []

for w in freq:
    if freq[w] > maxc:
        maxc = freq[w]
        most = w
    if freq[w] == 1:
        once.append(w)
    if len(w) > 5:
        more5.append(w)

unique = list(freq.keys())

rev_words = []
for i in range(len(words)-1, -1, -1):
    rev_words.append(words[i])

print("Total Words:", len(words))
print("Word Frequencies:", freq)
print("Most Frequent Word:", most)
print("Words Appearing Once:", once)
print("Unique Words:", unique)
print("Reversed Words:", rev_words)
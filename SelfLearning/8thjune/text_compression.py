text = "AAABBBCCCDDDAAA"

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

most = ""
maxc = 0
unique = []

for ch in freq:
    unique.append(ch)
    if freq[ch] > maxc:
        maxc = freq[ch]
        most = ch

compressed = ""
i = 0

while i < len(text):
    count = 1
    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1
    compressed += text[i] + str(count)
    i += 1

print("Original Text:", text)
print("Frequencies:", freq)
print("Unique Characters:", unique)
print("Most Frequent:", most)
print("Compressed:", compressed)
print("Original Length:", len(text))
print("Compressed Length:", len(compressed))
print("Compression Ratio:", (len(compressed)/len(text))*100)
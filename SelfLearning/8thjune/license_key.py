key = "ABCD-EFGH-IJKL-MNOP"

groups = key.split("-")

letters = 0
vowels = 0
vowel_set = "AEIOU"

valid = True

if len(groups) != 4:
    valid = False

for g in groups:
    if len(g) != 4:
        valid = False

for ch in key:
    if ch.isalpha():
        letters += 1
        if ch in vowel_set:
            vowels += 1

merged = ""
for g in groups:
    merged += g

print("Groups:", groups)
print("Number of Groups:", len(groups))
print("Total Letters:", letters)
print("Total Vowels:", vowels)
print("Merged Key:", merged)

if valid:
    print("License Key Status: Valid")
else:
    print("License Key Status: Invalid")
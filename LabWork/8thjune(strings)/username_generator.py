name = "Rahul Sharma"

year = "2026"

username = ""
vowels = "aeiou"
v = c = 0

for ch in name:
    if ch != " ":
        username += ch.lower()

username += year

if len(username) > 12:
    username = username[:12]

for ch in username:
    if ch in vowels:
        v += 1
    else:
        c += 1

print("Original Name:", name)
print("Generated Username:", username)
print("Username Length:", len(username))
print("Vowels:", v)
print("Consonants:", c)
# Password Security Analyzer

passwords = []

for i in range(15):
    pwd = input(f"Enter Password {i+1}: ")
    passwords.append(pwd)

strong = 0
medium = 0
weak = 0

for pwd in passwords:
    print("\n----------------------------")
    print("Password:", pwd)

    upper = 0
    lower = 0
    digits = 0
    special = 0
    vowels = 0
    consonants = 0

    frequency = {}

    for ch in pwd:
        if ch.isupper():
            upper += 1

        elif ch.islower():
            lower += 1

        elif ch.isdigit():
            digits += 1

        else:
            special += 1

        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

        frequency[ch] = frequency.get(ch, 0) + 1

    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)
    print("Digits:", digits)
    print("Special Characters:", special)

    print("Minimum Length Check:", len(pwd) >= 8)
    print("Contains Space:", " " in pwd)

    if len(pwd) >= 8 and upper > 0 and lower > 0 and digits > 0 and special > 0:
        strength = "Strong"
        strong += 1
    elif len(pwd) >= 8:
        strength = "Medium"
        medium += 1
    else:
        strength = "Weak"
        weak += 1

    print("Password Strength:", strength)

    print("Repeated Characters:")
    for ch, count in frequency.items():
        if count > 1:
            print(ch, "->", count)

    print("Vowels:", vowels)
    print("Consonants:", consonants)

    max_char = max(frequency, key=frequency.get)
    print("Most Frequent Character:", max_char)

print("\n===== SECURITY REPORT =====")
print("Total Passwords Analyzed:", len(passwords))
print("Strong Passwords:", strong)
print("Medium Passwords:", medium)
print("Weak Passwords:", weak)
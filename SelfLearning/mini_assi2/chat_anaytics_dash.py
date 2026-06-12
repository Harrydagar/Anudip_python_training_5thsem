# Chat Message Analytics Dashboard

messages = []

for i in range(20):
    msg = input(f"Enter Message {i+1}: ")
    messages.append(msg)

for msg in messages:

    print("\n==============================")
    print("Message:", msg)

    words = msg.split()

    print("Total Words:", len(words))
    print("Total Characters:", len(msg))

    vowels = 0
    consonants = 0

    for ch in msg:
        if ch.isalpha():

            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

    if len(words) > 0:

        longest = max(words, key=len)
        shortest = min(words, key=len)

        print("Longest Word:", longest)
        print("Shortest Word:", shortest)

        frequency = {}

        for word in words:
            word = word.lower()
            frequency[word] = frequency.get(word, 0) + 1

        print("\nWord Frequencies:")
        print(frequency)

        print("\nRepeated Words:")
        for word, count in frequency.items():
            if count > 1:
                print(word, "->", count)

        print("\nWords Starting With Vowels:")
        for word in words:
            if word[0].lower() in "aeiou":
                print(word)

        print("\nWords Longer Than 5 Characters:")
        for word in words:
            if len(word) > 5:
                print(word)

print("\nChat Analysis Completed Successfully.")
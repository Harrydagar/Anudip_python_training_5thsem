# File Content Analyzer

filename = input("Enter File Name: ")

try:
    file = open(filename, "r")

    content = file.read()

    # Count vowels
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for ch in content:
        if ch in vowels:
            vowel_count += 1

    # Count characters
    character_count = len(content)

    # Count lines
    file.seek(0)
    lines = file.readlines()
    line_count = len(lines)

    file.close()

    print("\nFile Analysis Report")
    print("Total Number of Vowels     :", vowel_count)
    print("Total Number of Characters :", character_count)
    print("Total Number of Lines      :", line_count)

except FileNotFoundError:
    print("File does not exist.")
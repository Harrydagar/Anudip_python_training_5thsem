# Input
name = input("Enter Full Name: ")
email = input("Enter Email ID: ")

# 1. Uppercase name
print(name.upper())

# 2. Title case name
print(name.title())

# 3. Total characters (including spaces)
count_chars = 0
for i in name:
    count_chars += 1
print("Total Characters:", count_chars)

# 4. Count spaces
space_count = 0
for i in name:
    if i == " ":
        space_count += 1
print("Spaces:", space_count)

# 5. Check "@"
has_at = False
for i in email:
    if i == "@":
        has_at = True
        break

if has_at:
    print("Valid Email: Yes")
else:
    print("Valid Email: No")

# 6. Check ".com"
if email[-4:] == ".com":
    print("Ends With .com: Yes")
else:
    print("Ends With .com: No")

# 7. Extract company name
company = ""
found_at = False

for i in email:
    if i == "@":
        found_at = True
        continue
    if found_at:
        if i == ".":
            break
        company += i

print("Company Name:", company)

# 8. Replace spaces with underscore
new_name = ""
for i in name:
    if i == " ":
        new_name += "_"
    else:
        new_name += i

print("Name with Underscore:", new_name)

# 9. Starts with A
if name[0].lower() == "a":
    print("Starts With A: True")
else:
    print("Starts With A: False")

# 10. Count letter 'a'
count_a = 0
for i in name:
    if i.lower() == "a":
        count_a += 1

print("Count of 'a':", count_a)
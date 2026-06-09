email = "rahul.sharma2026@gmail.com"

username = ""
domain = ""
ext = ""

at_seen = False
dot_seen = False

digits = 0
special = 0

for ch in email:
    if ch == "@":
        at_seen = True
        continue
    if not at_seen:
        username += ch
    else:
        domain += ch

for ch in username:
    if ch.isdigit():
        digits += 1
    if not ch.isalnum():
        special += 1

if "@" in domain:
    pass

parts = domain.split(".")
if len(parts) >= 2:
    domain_name = parts[0]
    ext = parts[1]
else:
    domain_name = domain
    ext = ""

valid = ("@" in email and email.count("@") == 1 and "." in email)

print("Username:", username)
print("Domain:", domain_name)
print("Extension:", ext)
print("Digits Found:", digits)
print("Special Characters Found:", special)

if valid:
    print("Email Status: Valid")
else:
    print("Email Status: Invalid")
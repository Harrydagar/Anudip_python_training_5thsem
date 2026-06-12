# Email Validation & Domain Analytics System

emails = []

for i in range(20):
    email = input(f"Enter Email {i+1}: ")
    emails.append(email)

domain_count = {}

print("\n===== EMAIL ANALYSIS =====")

for email in emails:

    print("\nEmail:", email)

    valid = True

    if email.count("@") != 1:
        valid = False

    if "." not in email:
        valid = False

    if " " in email:
        valid = False

    if valid:

        username = email.split("@")[0]
        domain = email.split("@")[1]

        extension = domain.split(".")[-1]

        digits = 0
        special = 0

        for ch in username:
            if ch.isdigit():
                digits += 1

            elif not ch.isalnum():
                special += 1

        print("Username:", username)
        print("Domain:", domain)
        print("Extension:", extension)
        print("Digits in Username:", digits)
        print("Special Characters:", special)

        domain_count[domain] = domain_count.get(domain, 0) + 1

    else:
        print("Invalid Email")

print("\n===== DOMAIN REPORT =====")

for domain, count in domain_count.items():
    print(domain, "->", count, "users")
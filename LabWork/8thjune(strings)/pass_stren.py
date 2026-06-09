password = "Python@2026!"

u = l = d = s = 0
digits_list = []
special_list = []

for ch in password:
    if ch.isupper():
        u += 1
    elif ch.islower():
        l += 1
    elif ch.isdigit():
        d += 1
        digits_list.append(ch)
    else:
        s += 1
        special_list.append(ch)

if len(password) >= 8 and u > 0 and l > 0 and d > 0 and s > 0:
    strength = "Strong"
elif len(password) >= 6:
    strength = "Medium"
else:
    strength = "Weak"

print("Uppercase Letters:", u)
print("Lowercase Letters:", l)
print("Digits:", d)
print("Special Characters:", s)
print("Digits Found:", digits_list)
print("Special Characters Found:", special_list)
print("Password Strength:", strength)
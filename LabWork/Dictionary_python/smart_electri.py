units = {
    "House101": 320, "House102": 180, "House103": 510,
    "House104": 275, "House105": 150, "House106": 430,
    "House107": 220, "House108": 390, "House109": 145,
    "House110": 600
}

print("Above 400:")
for h in units:
    if units[h] > 400:
        print(h)

# Highest
maxu = -1
high = ""
for h in units:
    if units[h] > maxu:
        maxu = units[h]
        high = h
print("Highest:", high, maxu)

# Lowest
minu = units["House101"]
low = "House101"
for h in units:
    if units[h] < minu:
        minu = units[h]
        low = h
print("Lowest:", low, minu)

# Total
total = 0
for h in units:
    total += units[h]
print("Total:", total)

# Categories
lowc = []
med = []
highc = []

for h in units:
    u = units[h]
    if u < 200:
        lowc.append(h)
    elif u <= 400:
        med.append(h)
    else:
        highc.append(h)

print("Low:", lowc)
print("Medium:", med)
print("High:", highc)

# Campaign count
count = 0
for h in units:
    if units[h] > 300:
        count += 1
print("Energy Campaign:", count)
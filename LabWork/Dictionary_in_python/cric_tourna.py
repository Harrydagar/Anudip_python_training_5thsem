runs = {
    "Virat": 645, "Rohit": 512, "Gill": 698, "Rahul": 435,
    "Hardik": 278, "Pant": 534, "Surya": 389, "Jadeja": 301,
    "Iyer": 455, "KL": 410
}

print("Above 500:")
for p in runs:
    if runs[p] > 500:
        print(p)

# Orange cap
maxr = -1
orange = ""
for p in runs:
    if runs[p] > maxr:
        maxr = runs[p]
        orange = p
print("Orange Cap:", orange, maxr)

# Lowest
minr = runs["Virat"]
low = "Virat"
for p in runs:
    if runs[p] < minr:
        minr = runs[p]
        low = p
print("Lowest:", low, minr)

# Total
total = 0
for p in runs:
    total += runs[p]
print("Total Runs:", total)

# Below 400
below = []
for p in runs:
    if runs[p] < 400:
        below.append(p)
print("Below 400:", below)

# 400–600 count
count = 0
for p in runs:
    if runs[p] >= 400 and runs[p] <= 600:
        count += 1
print("Between 400 and 600:", count)
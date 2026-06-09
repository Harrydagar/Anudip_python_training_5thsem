performance = {
    "EMP101": 92, "EMP102": 78, "EMP103": 45, "EMP104": 88,
    "EMP105": 97, "EMP106": 56, "EMP107": 81, "EMP108": 64,
    "EMP109": 39, "EMP110": 73
}

print("Above 80:")
for e in performance:
    if performance[e] > 80:
        print(e)

# Improvement count
count = 0
for e in performance:
    if performance[e] < 60:
        count += 1
print("Needing improvement:", count)

# Top performer
top = ""
maxv = -1
for e in performance:
    if performance[e] > maxv:
        maxv = performance[e]
        top = e
print("Top Performer:", top, maxv)

# Average
total = 0
n = 0
for e in performance:
    total += performance[e]
    n += 1
print("Average:", total / n)

# Categories
excellent = []
good = []
average = []
poor = []

for e in performance:
    s = performance[e]
    if s >= 90:
        excellent.append(e)
    elif s >= 75:
        good.append(e)
    elif s >= 60:
        average.append(e)
    else:
        poor.append(e)

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)
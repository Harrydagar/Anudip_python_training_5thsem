temperature = {
    "Delhi": 41, "Mumbai": 33, "Chennai": 37, "Kolkata": 39,
    "Bengaluru": 28, "Pune": 30, "Jaipur": 42, "Lucknow": 40,
    "Hyderabad": 35, "Ahmedabad": 43
}

print("Above 40°C:")
for c in temperature:
    if temperature[c] > 40:
        print(c)

# Hottest
max_temp = -1
hot = ""
for c in temperature:
    if temperature[c] > max_temp:
        max_temp = temperature[c]
        hot = c
print("Hottest:", hot, max_temp)

# Coolest
min_temp = temperature["Delhi"]
cold = "Delhi"
for c in temperature:
    if temperature[c] < min_temp:
        min_temp = temperature[c]
        cold = c
print("Coolest:", cold, min_temp)

# Average
total = 0
n = 0
for c in temperature:
    total += temperature[c]
    n += 1
print("Average:", total / n)

# Pleasant cities
pleasant = []
for c in temperature:
    if temperature[c] < 35:
        pleasant.append(c)
print("Pleasant:", pleasant)

# 35–40 count
count = 0
for c in temperature:
    if temperature[c] >= 35 and temperature[c] <= 40:
        count += 1
print("Between 35 and 40:", count)
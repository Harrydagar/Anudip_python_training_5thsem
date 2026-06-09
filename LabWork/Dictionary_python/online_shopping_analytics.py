sales = {
    "Laptop": 15, "Mouse": 45, "Keyboard": 32, "Monitor": 12,
    "Headphones": 28, "Printer": 8, "Webcam": 20, "Speaker": 18,
    "Tablet": 10, "Router": 25
}

print("Products sold > 20:")
for p in sales:
    if sales[p] > 20:
        print(p)

# Best selling
max_sale = -1
best = ""
for p in sales:
    if sales[p] > max_sale:
        max_sale = sales[p]
        best = p

print("Best Selling:", best, max_sale)

# Least selling
min_sale = sales["Laptop"]
least = "Laptop"
for p in sales:
    if sales[p] < min_sale:
        min_sale = sales[p]
        least = p

print("Least Selling:", least, min_sale)

# Total
total = 0
for p in sales:
    total += sales[p]
print("Total Sold:", total)

# Promotion list
promo = []
for p in sales:
    if sales[p] < 15:
        promo.append(p)
print("Promotion Products:", promo)

# Count 10–30
count = 0
for p in sales:
    if sales[p] >= 10 and sales[p] <= 30:
        count += 1
print("Between 10 and 30:", count)
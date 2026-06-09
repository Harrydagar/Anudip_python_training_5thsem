att = "PPAPPPAAPPPPAPP"

p = a = 0
max_p = max_a = 0
curr_p = curr_a = 0

for ch in att:
    if ch == "P":
        p += 1
        curr_p += 1
        curr_a = 0
        if curr_p > max_p:
            max_p = curr_p
    else:
        a += 1
        curr_a += 1
        curr_p = 0
        if curr_a > max_a:
            max_a = curr_a

percent = (p / len(att)) * 100

print("Present Days:", p)
print("Absent Days:", a)
print("Attendance %:", percent)
print("Longest Present Streak:", max_p)
print("Longest Absent Streak:", max_a)

if percent < 75:
    print("Status: Below 75%")
else:
    print("Status: Good")
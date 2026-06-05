# Accept N numbers one by one and find the length of the longest continuous increasing sequence. 
# Example: 
# Input: 
# 5 8 10 12 3 4 5 6 1 
 
# Output: 
# Longest Sequence Length = 4 



n = int(input("Enter no of elements: "))

prev = int(input("Input: "))   # first element
curr_len = 1                   # current count
max_len = 1                    # best count

for i in range(1, n):
    curr = int(input())

    if curr > prev:
        curr_len += 1         # increasing count
    else:
        curr_len = 1          # reset count

    if curr_len > max_len:
        max_len = curr_len    # update max

    prev = curr               # move forward

print("Longest Sequence Length =", max_len)
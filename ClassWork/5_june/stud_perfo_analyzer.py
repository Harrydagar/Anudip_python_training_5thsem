# --- Step 1: Initialize the dataset and tracking variables ---
marks = [78, 45, 92, 35, 88, 40, 99, 56]

passed_students = []
merit_list = []
failed_count = 0

# Set initial highest and lowest bounds to the very first item in the list
# This is a classic programming strategy when min() and max() are forbidden
highest_marks = marks[0]
lowest_marks = marks[0]

# --- Step 2: Loop through the marks list to evaluate each score ---
for score in marks:
    
    # 1. Check for passing status (marks >= 40)
    if score >= 40:
        passed_students.append(score)
    else:
        # 2. Count failures if score falls below 40
        failed_count += 1
        
    # 3. Filter scores to build the merit list (marks > 75)
    if score > 75:
        merit_list.append(score)
        
    # 4. Manual tracking calculation for highest score
    if score > highest_marks:
        highest_marks = score
        
    # 5. Manual tracking calculation for lowest score
    if score < lowest_marks:
        lowest_marks = score

# --- Step 3: Display the final analytics summary ---
print(f"Passed Students: {passed_students}")
print(f"Failed Count: {failed_count}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Merit List: {merit_list}")
""""""
""" #Calculate the total marks and percentage.
Determine the performance category:
20% to 50% → Average Student
Above 50% to 90% → Good Student
Above 90% → Excellent Student
Below 20% → Poor Student
Display the effect of individual subjects on the total:
Calculate and display the percentage contribution of Hindi marks to the total.
Calculate and display the percentage contribution of English marks to the total. """


try:
    # Input marks
    hindi = float(input("Enter Hindi Marks: "))
    english = float(input("Enter English Marks: "))

    # Validate marks
    if hindi < 0 or english < 0:
        raise ValueError("Marks cannot be negative.")

    if hindi > 100 or english > 100:
        raise ValueError("Marks cannot exceed 100.")

    # Calculate total and percentage
    total = hindi + english
    percentage = (total / 200) * 100

    print("\nTotal Marks:", total)
    print("Percentage:", round(percentage, 2), "%")

    # Performance Category
    if percentage < 20:
        print("Performance Category: Poor Student")
    elif percentage <= 50:
        print("Performance Category: Average Student")
    elif percentage <= 90:
        print("Performance Category: Good Student")
    else:
        print("Performance Category: Excellent Student")

    # Subject Contributions
    if total > 0:
        hindi_contribution = (hindi / total) * 100
        english_contribution = (english / total) * 100

        print("\nHindi Contribution to Total:",
              round(hindi_contribution, 2), "%")

        print("English Contribution to Total:",
              round(english_contribution, 2), "%")
    else:
        print("\nCannot calculate contributions because total marks are zero.")

except ValueError as e:
    print("\nError:", e)

except Exception:
    print("\nError: Please enter valid numeric values only.")

finally:
    print("\nStudent performance analysis completed.")
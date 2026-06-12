def high_enrollment(data):
    print("Courses with More Than 40 Enrollments:")

    for course, students in data.items():
        if students > 40:
            print(course)


def popular_courses(data):
    highest = max(data, key=data.get)
    lowest = min(data, key=data.get)

    print(f"\nMost Popular Course:\n{highest} ({data[highest]} students)")
    print(f"\nLeast Popular Course:\n{lowest} ({data[lowest]} students)")


def total_enrollment(data):
    print("\nTotal Enrollments:", sum(data.values()))


def demand_categories(data):
    high = []
    medium = []
    low = []

    for course, students in data.items():
        if students > 40:
            high.append(course)
        elif students >= 30:
            medium.append(course)
        else:
            low.append(course)

    print("\nHigh Demand:")
    print(high)

    print("\nMedium Demand:")
    print(medium)

    print("\nLow Demand:")
    print(low)


def promotional_courses(data):
    count = 0

    for students in data.values():
        if students < 35:
            count += 1

    print("\nCourses Requiring Promotion:", count)


enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}

high_enrollment(enrollment)
popular_courses(enrollment)
total_enrollment(enrollment)
demand_categories(enrollment)
promotional_courses(enrollment)
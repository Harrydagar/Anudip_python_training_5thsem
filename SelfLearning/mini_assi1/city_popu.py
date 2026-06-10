"""5. City Population & Development Dashboard
Problem Statement
The government wants to analyze city data.
Store details of at least 30 cities.
Example Structure
cities = { "Delhi": { "population": 32000000, "area": 1484, "literacy": 89 } }
Requirements
1.
Display all city details.
2.
Find the most populated city.
3.
Find the least populated city.
4.
Calculate average population.
5.
Display cities with literacy rate above 90%.
6.
Display cities with literacy below average.
7.
Calculate population density.
8.
Find city with highest density.
9.
Categorize cities:
o
Small
o
Medium
o
Large
10.
Create a development-priority list.
11.
Generate separate dictionaries for:
o
High Literacy Cities
o
Low Literacy Cities
12.
Generate a national summary report.
Challenge
Rank all cities based on population density.
"""
# ==========================================
# CITY POPULATION & DEVELOPMENT DASHBOARD
# ==========================================

cities = {
"Delhi":{"population":32000000,"area":1484,"literacy":89},
"Mumbai":{"population":21000000,"area":603,"literacy":91},
"Bangalore":{"population":13000000,"area":741,"literacy":88},
"Hyderabad":{"population":11000000,"area":650,"literacy":87},
"Chennai":{"population":10000000,"area":426,"literacy":90},
"Kolkata":{"population":15000000,"area":205,"literacy":88},
"Pune":{"population":7500000,"area":331,"literacy":92},
"Ahmedabad":{"population":8500000,"area":505,"literacy":86},
"Jaipur":{"population":4500000,"area":467,"literacy":84},
"Lucknow":{"population":4000000,"area":631,"literacy":82},
"Kanpur":{"population":3200000,"area":403,"literacy":80},
"Nagpur":{"population":2900000,"area":227,"literacy":89},
"Indore":{"population":3500000,"area":530,"literacy":87},
"Bhopal":{"population":2500000,"area":463,"literacy":85},
"Patna":{"population":3000000,"area":250,"literacy":81},
"Chandigarh":{"population":1200000,"area":114,"literacy":91},
"Surat":{"population":7000000,"area":461,"literacy":89},
"Vadodara":{"population":2500000,"area":235,"literacy":88},
"Ranchi":{"population":1500000,"area":175,"literacy":84},
"Raipur":{"population":1800000,"area":226,"literacy":86},
"Dehradun":{"population":1100000,"area":308,"literacy":90},
"Shimla":{"population":900000,"area":35,"literacy":94},
"Agra":{"population":2000000,"area":188,"literacy":82},
"Meerut":{"population":1700000,"area":305,"literacy":79},
"Varanasi":{"population":1600000,"area":112,"literacy":83},
"Amritsar":{"population":1300000,"area":139,"literacy":85},
"Jodhpur":{"population":1400000,"area":233,"literacy":81},
"Guwahati":{"population":1200000,"area":216,"literacy":88},
"Mysore":{"population":1100000,"area":156,"literacy":91},
"Coimbatore":{"population":2200000,"area":246,"literacy":92}
}

# ==========================================
# FUNCTIONS
# ==========================================

def display_cities():

    print("\nCITY DETAILS")
    print("-" * 70)

    for city in cities:

        print(
            city,
            "| Population:", cities[city]["population"],
            "| Area:", cities[city]["area"],
            "| Literacy:", cities[city]["literacy"]
        )


def most_populated():

    max_pop = -1
    city_name = ""

    for city in cities:

        if cities[city]["population"] > max_pop:

            max_pop = cities[city]["population"]
            city_name = city

    print("\nMost Populated City")
    print(city_name, "-", max_pop)


def least_populated():

    min_pop = 999999999
    city_name = ""

    for city in cities:

        if cities[city]["population"] < min_pop:

            min_pop = cities[city]["population"]
            city_name = city

    print("\nLeast Populated City")
    print(city_name, "-", min_pop)


def average_population():

    total = 0

    for city in cities:
        total += cities[city]["population"]

    avg = total / len(cities)

    print("\nAverage Population =", round(avg))

    return avg


def literacy_above_90():

    print("\nCities With Literacy Above 90%")

    for city in cities:

        if cities[city]["literacy"] > 90:

            print(city,
                  cities[city]["literacy"])


def literacy_below_average():

    total = 0

    for city in cities:
        total += cities[city]["literacy"]

    avg = total / len(cities)

    print("\nAverage Literacy =", round(avg,2))

    print("\nCities Below Average Literacy")

    for city in cities:

        if cities[city]["literacy"] < avg:

            print(city,
                  cities[city]["literacy"])


def population_density():

    print("\nPopulation Density Report")

    for city in cities:

        density = (
            cities[city]["population"] /
            cities[city]["area"]
        )

        print(city,
              round(density,2))


def highest_density():

    max_density = -1
    city_name = ""

    for city in cities:

        density = (
            cities[city]["population"] /
            cities[city]["area"]
        )

        if density > max_density:

            max_density = density
            city_name = city

    print("\nHighest Density City")
    print(city_name,
          round(max_density,2))


def categorize_cities():

    print("\nCITY CATEGORIES")

    for city in cities:

        population = cities[city]["population"]

        if population > 10000000:
            category = "Large"

        elif population > 3000000:
            category = "Medium"

        else:
            category = "Small"

        print(city, "-", category)


def development_priority():

    print("\nDEVELOPMENT PRIORITY LIST")

    for city in cities:

        if cities[city]["literacy"] < 85:

            print(
                city,
                "Literacy:",
                cities[city]["literacy"]
            )


def high_literacy_cities():

    high = {}

    for city in cities:

        if cities[city]["literacy"] >= 90:

            high[city] = cities[city]

    print("\nHIGH LITERACY CITIES")

    for city in high:
        print(city, high[city])


def low_literacy_cities():

    low = {}

    for city in cities:

        if cities[city]["literacy"] < 85:

            low[city] = cities[city]

    print("\nLOW LITERACY CITIES")

    for city in low:
        print(city, low[city])


def rank_by_density():

    print("\nCITY RANKING BY DENSITY")

    temp = {}

    for city in cities:
        temp[city] = cities[city]

    rank = 1

    while len(temp) > 0:

        best_city = ""
        best_density = -1

        for city in temp:

            density = (
                temp[city]["population"] /
                temp[city]["area"]
            )

            if density > best_density:

                best_density = density
                best_city = city

        print(
            rank,
            best_city,
            round(best_density,2)
        )

        del temp[best_city]

        rank += 1


def national_report():

    print("\n")
    print("=" * 60)
    print("NATIONAL SUMMARY REPORT")
    print("=" * 60)

    most_populated()
    least_populated()
    average_population()
    highest_density()

    print("\nTotal Cities =", len(cities))


# ==========================================
# MENU
# ==========================================

while True:

    print("\n")
    print("=" * 60)
    print("CITY POPULATION & DEVELOPMENT DASHBOARD")
    print("=" * 60)

    print("1. Display All Cities")
    print("2. Most Populated City")
    print("3. Least Populated City")
    print("4. Average Population")
    print("5. Literacy Above 90%")
    print("6. Literacy Below Average")
    print("7. Population Density")
    print("8. Highest Density City")
    print("9. Categorize Cities")
    print("10. Development Priority List")
    print("11. High Literacy Cities")
    print("12. Low Literacy Cities")
    print("13. Rank Cities By Density")
    print("14. National Summary Report")
    print("0. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_cities()

    elif choice == "2":
        most_populated()

    elif choice == "3":
        least_populated()

    elif choice == "4":
        average_population()

    elif choice == "5":
        literacy_above_90()

    elif choice == "6":
        literacy_below_average()

    elif choice == "7":
        population_density()

    elif choice == "8":
        highest_density()

    elif choice == "9":
        categorize_cities()

    elif choice == "10":
        development_priority()

    elif choice == "11":
        high_literacy_cities()

    elif choice == "12":
        low_literacy_cities()

    elif choice == "13":
        rank_by_density()

    elif choice == "14":
        national_report()

    elif choice == "0":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
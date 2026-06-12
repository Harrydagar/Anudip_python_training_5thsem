def high_consumers(data):
    print("Houses Consuming More Than 3000 Litres:")

    for house, litres in data.items():
        if litres > 3000:
            print(house)


def highest_lowest(data):
    highest = max(data, key=data.get)
    lowest = min(data, key=data.get)

    print(f"\nHighest Consumption:\n{highest} ({data[highest]} litres)")
    print(f"\nLowest Consumption:\n{lowest} ({data[lowest]} litres)")


def total_consumption(data):
    print("\nTotal Consumption:", sum(data.values()), "litres")


def categories(data):
    low = []
    medium = []
    high = []

    for house, litres in data.items():
        if litres < 2000:
            low.append(house)
        elif litres <= 3500:
            medium.append(house)
        else:
            high.append(house)

    print("\nLow Consumption:")
    print(low)

    print("\nMedium Consumption:")
    print(medium)

    print("\nHigh Consumption:")
    print(high)


def eligible_houses(data):
    count = 0

    for litres in data.values():
        if litres > 2500:
            count += 1

    print("\nEligible Households:", count)


water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

high_consumers(water_usage)
highest_lowest(water_usage)
total_consumption(water_usage)
categories(water_usage)
eligible_houses(water_usage)
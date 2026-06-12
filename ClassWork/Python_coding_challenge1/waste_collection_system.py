def high_waste(data):
    print("Sectors Generating More Than 400 kg Waste:")

    for sector, waste in data.items():
        if waste > 400:
            print(sector)


def max_min_waste(data):
    maximum = max(data, key=data.get)
    minimum = min(data, key=data.get)

    print(f"\nMaximum Waste Generation:\n{maximum} ({data[maximum]} kg)")
    print(f"\nMinimum Waste Generation:\n{minimum} ({data[minimum]} kg)")


def total_waste(data):
    print("\nTotal Waste Collected:", sum(data.values()), "kg")


def categorize(data):
    low = []
    medium = []
    high = []

    for sector, waste in data.items():
        if waste < 200:
            low.append(sector)
        elif waste <= 400:
            medium.append(sector)
        else:
            high.append(sector)

    print("\nLow Waste:")
    print(low)

    print("\nMedium Waste:")
    print(medium)

    print("\nHigh Waste:")
    print(high)


def awareness_campaign(data):
    campaign = []

    for sector, waste in data.items():
        if waste > 300:
            campaign.append(sector)

    print("\nSectors Requiring Awareness Campaign:")
    for sector in campaign:
        print(sector)

    file = open("campaign_sectors.txt", "w")

    for sector in campaign:
        file.write(sector + "\n")

    file.close()

    print("\nCampaign Report Generated Successfully.")


waste = {
    "Sector1": 320,
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}

high_waste(waste)
max_min_waste(waste)
total_waste(waste)
categorize(waste)
awareness_campaign(waste)
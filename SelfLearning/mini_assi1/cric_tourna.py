"""4. Cricket Tournament Analytics System
Problem Statement
Store statistics of at least 30 cricket players.
Example Structure
players = { "Virat": { "runs": 645, "matches": 12, "wickets": 0 } }
Requirements
1.
Display all player statistics.
2.
Find highest run scorer.
3.
Find lowest run scorer.
4.
Calculate average runs.
5.
Find player with maximum wickets.
6.
Find all-rounders (runs > 300 and wickets > 5).
7.
Display players scoring above average.
8.
Create categories:
o
Star Performer
o
Good Performer
o
Average Performer
o
Poor Performer
9.
Generate team statistics.
10.
Display top 5 batsmen.
11.
Display top 5 bowlers.
12.
Create a separate dictionary for award winners.
Challenge
Generate a tournament report."""
# ==========================================
# CRICKET TOURNAMENT ANALYTICS SYSTEM
# ==========================================

players = {
"Virat":{"runs":645,"matches":12,"wickets":0},
"Rohit":{"runs":510,"matches":12,"wickets":1},
"Gill":{"runs":590,"matches":12,"wickets":0},
"Rahul":{"runs":420,"matches":11,"wickets":0},
"Hardik":{"runs":350,"matches":10,"wickets":8},
"Jadeja":{"runs":310,"matches":12,"wickets":14},
"Bumrah":{"runs":50,"matches":12,"wickets":22},
"Shami":{"runs":30,"matches":11,"wickets":19},
"Siraj":{"runs":40,"matches":12,"wickets":16},
"Kuldeep":{"runs":75,"matches":10,"wickets":18},
"Axar":{"runs":220,"matches":10,"wickets":10},
"Ishan":{"runs":290,"matches":9,"wickets":0},
"Surya":{"runs":410,"matches":11,"wickets":0},
"Rinku":{"runs":330,"matches":9,"wickets":1},
"Sanju":{"runs":375,"matches":10,"wickets":0},
"Chahal":{"runs":25,"matches":8,"wickets":15},
"Ashwin":{"runs":180,"matches":9,"wickets":12},
"Arshdeep":{"runs":20,"matches":8,"wickets":13},
"Washington":{"runs":260,"matches":9,"wickets":9},
"Tilak":{"runs":300,"matches":10,"wickets":1},
"Prithvi":{"runs":280,"matches":8,"wickets":0},
"Dhawan":{"runs":390,"matches":10,"wickets":0},
"Pant":{"runs":430,"matches":10,"wickets":0},
"Shreyas":{"runs":470,"matches":11,"wickets":0},
"Gaikwad":{"runs":520,"matches":11,"wickets":0},
"Bishnoi":{"runs":45,"matches":9,"wickets":14},
"Harshal":{"runs":60,"matches":10,"wickets":17},
"Deepak":{"runs":95,"matches":9,"wickets":11},
"Umesh":{"runs":35,"matches":8,"wickets":9},
"Mukesh":{"runs":25,"matches":7,"wickets":8}
}

# ==========================================
# FUNCTIONS
# ==========================================

def display_players():

    print("\nPLAYER STATISTICS")
    print("-" * 60)

    for player in players:

        print(
            player,
            "| Runs:", players[player]["runs"],
            "| Matches:", players[player]["matches"],
            "| Wickets:", players[player]["wickets"]
        )


def highest_run_scorer():

    highest = -1
    best_player = ""

    for player in players:

        if players[player]["runs"] > highest:

            highest = players[player]["runs"]
            best_player = player

    print("\nHighest Run Scorer")
    print(best_player, "-", highest)


def lowest_run_scorer():

    lowest = 999999
    player_name = ""

    for player in players:

        if players[player]["runs"] < lowest:

            lowest = players[player]["runs"]
            player_name = player

    print("\nLowest Run Scorer")
    print(player_name, "-", lowest)


def average_runs():

    total = 0

    for player in players:
        total += players[player]["runs"]

    avg = total / len(players)

    print("\nAverage Runs =", round(avg, 2))

    return avg


def max_wickets():

    max_wicket = -1
    bowler = ""

    for player in players:

        if players[player]["wickets"] > max_wicket:

            max_wicket = players[player]["wickets"]
            bowler = player

    print("\nMaximum Wickets")
    print(bowler, "-", max_wicket)


def all_rounders():

    print("\nALL ROUNDERS")

    for player in players:

        if (
            players[player]["runs"] > 300 and
            players[player]["wickets"] > 5
        ):

            print(
                player,
                "Runs:", players[player]["runs"],
                "Wickets:", players[player]["wickets"]
            )


def players_above_average():

    total = 0

    for player in players:
        total += players[player]["runs"]

    avg = total / len(players)

    print("\nPLAYERS ABOVE AVERAGE")
    print("Average =", round(avg,2))

    for player in players:

        if players[player]["runs"] > avg:

            print(
                player,
                players[player]["runs"]
            )


def categories():

    print("\nPERFORMANCE CATEGORIES")

    for player in players:

        runs = players[player]["runs"]

        if runs >= 500:
            category = "Star Performer"

        elif runs >= 300:
            category = "Good Performer"

        elif runs >= 150:
            category = "Average Performer"

        else:
            category = "Poor Performer"

        print(player, "-", category)


def team_statistics():

    total_runs = 0
    total_wickets = 0
    total_matches = 0

    for player in players:

        total_runs += players[player]["runs"]
        total_wickets += players[player]["wickets"]
        total_matches += players[player]["matches"]

    print("\nTEAM STATISTICS")
    print("Total Runs :", total_runs)
    print("Total Wickets :", total_wickets)
    print("Total Matches :", total_matches)


def top_5_batsmen():

    print("\nTOP 5 BATSMEN")

    temp = players.copy()

    for i in range(5):

        best_player = ""
        highest = -1

        for player in temp:

            if temp[player]["runs"] > highest:

                highest = temp[player]["runs"]
                best_player = player

        print(
            i + 1,
            best_player,
            "-",
            highest
        )

        del temp[best_player]


def top_5_bowlers():

    print("\nTOP 5 BOWLERS")

    temp = players.copy()

    for i in range(5):

        best_player = ""
        wickets = -1

        for player in temp:

            if temp[player]["wickets"] > wickets:

                wickets = temp[player]["wickets"]
                best_player = player

        print(
            i + 1,
            best_player,
            "-",
            wickets
        )

        del temp[best_player]


def award_winners():

    awards = {}

    for player in players:

        if (
            players[player]["runs"] >= 500 or
            players[player]["wickets"] >= 15
        ):

            awards[player] = players[player]

    print("\nAWARD WINNERS")

    for player in awards:

        print(
            player,
            awards[player]
        )


def tournament_report():

    print("\n")
    print("=" * 60)
    print("TOURNAMENT REPORT")
    print("=" * 60)

    highest_run_scorer()
    lowest_run_scorer()
    max_wickets()
    average_runs()

    print("\nTotal Players =", len(players))


# ==========================================
# MENU DRIVEN PROGRAM
# ==========================================

while True:

    print("\n")
    print("=" * 60)
    print("CRICKET TOURNAMENT ANALYTICS SYSTEM")
    print("=" * 60)

    print("1. Display All Players")
    print("2. Highest Run Scorer")
    print("3. Lowest Run Scorer")
    print("4. Average Runs")
    print("5. Maximum Wickets")
    print("6. All Rounders")
    print("7. Players Above Average")
    print("8. Performance Categories")
    print("9. Team Statistics")
    print("10. Top 5 Batsmen")
    print("11. Top 5 Bowlers")
    print("12. Award Winners")
    print("13. Tournament Report")
    print("0. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_players()

    elif choice == "2":
        highest_run_scorer()

    elif choice == "3":
        lowest_run_scorer()

    elif choice == "4":
        average_runs()

    elif choice == "5":
        max_wickets()

    elif choice == "6":
        all_rounders()

    elif choice == "7":
        players_above_average()

    elif choice == "8":
        categories()

    elif choice == "9":
        team_statistics()

    elif choice == "10":
        top_5_batsmen()

    elif choice == "11":
        top_5_bowlers()

    elif choice == "12":
        award_winners()

    elif choice == "13":
        tournament_report()

    elif choice == "0":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
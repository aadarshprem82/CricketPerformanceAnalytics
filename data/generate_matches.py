import csv
import random

teams = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Gujarat Titans",
    "Kolkata Knight Riders",
    "Mumbai Indians",
    "Punjab Kings",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad",
]

venues = [
    "M. A. Chidambaram Stadium",
    "Arun Jaitley Stadium",
    "Narendra Modi Stadium",
    "Eden Gardens",
    "Wankhede Stadium",
    "M. Chinnaswamy Stadium",
]


def create_matches():
    matches = []

    for match_id in range(1, 21):
        team1, team2 = random.sample(teams, 2)
        winner = random.choice([team1, team2])

        match = {
            "match_id": match_id,
            "season": 2024,
            "venue": random.choice(venues),
            "team1": team1,
            "team2": team2,
            "winner": winner,
        }

        matches.append(match)

    return matches


def save_matches(matches):
    with open("data/matches.csv", "w", newline="") as file:
        columns = ["match_id", "season", "venue", "team1", "team2", "winner"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(matches)


matches = create_matches()
save_matches(matches)
print("matches.csv created successfully")

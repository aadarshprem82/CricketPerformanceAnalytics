import csv
import random


batsmen = [
    "Virat Kohli",
    "Rohit Sharma",
    "MS Dhoni",
    "Shubman Gill",
    "Ruturaj Gaikwad",
    "Sanju Samson",
    "KL Rahul",
    "Suryakumar Yadav",
]

bowlers = [
    "Jasprit Bumrah",
    "Rashid Khan",
    "Mohammed Shami",
    "Yuzvendra Chahal",
    "Ravindra Jadeja",
    "Trent Boult",
    "Bhuvneshwar Kumar",
    "Kuldeep Yadav",
]


def create_deliveries():
    deliveries = []

    for match_id in range(1, 21):
        for over in range(20):
            for ball in range(1, 7):
                batsman = random.choice(batsmen)
                bowler = random.choice(bowlers)
                runs = random.choice([0, 1, 2, 3, 4, 6])
                is_wicket = random.choice([0, 0, 0, 0, 1])

                delivery = {
                    "match_id": match_id,
                    "over": over,
                    "ball": ball,
                    "batsman": batsman,
                    "bowler": bowler,
                    "runs": runs,
                    "is_wicket": is_wicket,
                }

                deliveries.append(delivery)

    return deliveries


def save_deliveries(deliveries):
    with open("data/deliveries.csv", "w", newline="") as file:
        columns = ["match_id", "over", "ball", "batsman", "bowler", "runs", "is_wicket"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(deliveries)


deliveries = create_deliveries()
save_deliveries(deliveries)
print("deliveries.csv created successfully")

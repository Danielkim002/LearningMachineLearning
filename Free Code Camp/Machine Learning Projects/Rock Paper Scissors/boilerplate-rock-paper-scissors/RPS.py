# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
import csv
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess

def make_dataset(prev_play, opponent_history = []):
    opponent_history.append(prev_play)

    if len(opponent_history) == 200000:
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(opponent_history)
    
    return random.choice(['R', 'P', 'S'])

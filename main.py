import random
import csv


players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

game_results = []
for player in players:
    for i in range(10):
        score = random.randint(0, 100)
        game_results.append([player, score])
random.shuffle(game_results)


with open("game_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", "Score"])
    writer.writerows(game_results)

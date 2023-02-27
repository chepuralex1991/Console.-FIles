import csv

with open('game_results.csv', 'r') as data:
    reader = csv.reader(data)
    next(reader)
    player_scores = {}
    for row in reader:
        player = row[0]
        score = int(row[1])
        if player not in player_scores or score > player_scores[player]:
            player_scores[player] = score

sorted_data = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
        
       
with open("highest_game_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", "Highest Score"])
    writer.writerows(sorted_data)

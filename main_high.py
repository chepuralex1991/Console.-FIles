import csv

with open('game_results.csv', 'r') as data:
    reader = csv.reader(data)
    next(reader)
    sorted_data = sorted(reader, key=lambda row: int(row[1]), reverse=True)[:5]
        
       
with open("highest_game_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", "Highest Score"])
    writer.writerows(sorted_data)

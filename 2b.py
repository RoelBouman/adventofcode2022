import pandas as pd

#define points:
loss = 0
tie = 3
win = 6

move_points = {"A":1, "B":2, "C":3}

#Define which moves beats which:
#[key] beats [value]
win_move = {"A":"C", "B":"A","C":"B"}
lose_move = {"A":"B", "B":"C","C":"A"}

match_goal = {"X":"lose", "Y":"tie", "Z":"win"}


strategy = pd.read_csv("data/2a.txt", sep=" ", names=["input", "response"])

total_points = 0

for i, row in strategy.iterrows():
    if match_goal[row["response"]] == "win": #win
        total_points += win
        total_points += move_points[lose_move[row["input"]]]
    elif match_goal[row["response"]] == "lose": #lose
        total_points += loss
        total_points += move_points[win_move[row["input"]]]
    elif match_goal[row["response"]] == "tie": #tie
        total_points += tie
        total_points += move_points[row["input"]]
        
print("This strategy yields {} points over {} rounds, averaging {} points per move".format(total_points, strategy.shape[0], total_points/strategy.shape[0]))
        
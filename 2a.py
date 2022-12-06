import pandas as pd

#define points:
loss = 0
tie = 3
win = 6

move_points = {"X":1, "Y":2, "Z":3}

#Define which moves beats which:
#[key] beats [value]
win_move = {"X":"C", "Y":"A","Z":"B"}
lose_move = {"X":"B", "Y":"C","Z":"A"}


strategy = pd.read_csv("data/2a.txt", sep=" ", names=["input", "response"])

total_points = 0

for i, row in strategy.iterrows():
    total_points += move_points[row["response"]]
    
    if row["input"] == win_move[row["response"]]: #win with listed move
        total_points += win
    elif row["input"] == lose_move[row["response"]]: #lose with listed move
        total_points += loss
    else:
        total_points += tie
        
        
print("This strategy yields {} points over {} rounds, averaging {} points per move".format(total_points, strategy.shape[0], total_points/strategy.shape[0]))
        
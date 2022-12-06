with open("data/1a.txt", "r") as f:
    #lines = f.readlines()
    
    max_calories = 0
    current_calories = 0
    for line in f: #use file iterator rather than readlines for O(n) < O(2n)
        try:
            current_calories+= int(line)
        except ValueError:
            if current_calories > max_calories:
                max_calories = current_calories
            #reset current calories to moe to next elf
            current_calories = 0
print("The elf carrying the most calories worth of starfruit has a total of {} calories".format(max_calories))
        
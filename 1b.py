import bisect

top_n_elves = 3 #how many elves should we look at?

with open("data/1a.txt", "r") as f:
    #lines = f.readlines()
    
    max_calories = [0]*top_n_elves
    current_calories = 0
    
    for line in f: #use file iterator rather than readlines for O(n) < O(2n)
        try:
            current_calories+= int(line)
        except ValueError:
            if current_calories > max_calories[0]:
                
                #remove previous n-th highest elf
                max_calories.pop(0)
                
                #use bisection insort for O(n) insertion of higher elf
                bisect.insort(max_calories, current_calories)
                
                
            #reset current calories to move to next elf
            current_calories = 0
            
print("The {} elves carrying the most calories worth of starfruit have a total of {} calories".format(top_n_elves, sum(max_calories)))
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("Enter number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be betwee 2 to 4")
    else:
        print("Invalid, try again!")

max_score = 100
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer number {player_idx+1} turn has just started!\n")
        print(f"You total score is: {player_score}")
        current_score = 0
        
        while True:
            
            should_roll = input("Would you like to roll?(y/n)")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1. Turn Done!!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a : {value} ")
        
            print(f"Your score is: {current_score}")
        player_score[player_idx] == current_score
        print(f"You total score is: {player_score[player_idx]}")
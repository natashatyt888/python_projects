import random

def main():
    game()


def game():
    list = ["Rock", "Paper", "Scissors"]
    user = int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors: "))
    #rock beats scissors, paper beats rock, scissors beat paper
    ai = random.randint(0,3)
    if user == ai:
        print("User chose " + list[user] + " and AI chose " + list[ai])
        print("Draw")
    elif (user == 0 and ai == 2) or (user == 1 and ai == 0) or (user == 2 and ai == 1):
        print("User chose " + list[user] + " and AI chose " + list[ai])
        print("User wins!")
    else: 
        print("User chose " + list[user] + " and AI chose " + list[ai])
        print("AI wins!")
    restart = input("Continue? Y/N: ").upper()
    if restart == "Y":
        game()
        
main()
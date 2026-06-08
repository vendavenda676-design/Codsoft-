import random

while True:
    user=input("enter rock, paper,or scissors: ").lower()
    computer=random.choice(["rock", "paper", "scissors"])
    print("you:", user)
    print("computer:", computer)
    if user == computer:
        print("It's tie!")
    elif(user =="rock" and computer == "scissors") or \
        (user =="paper" and computer == "rock") or \
        (user =="scissors" and computer == "paper"):
        print("you win!")
    else:
        print("you lose!")
    
    again =input("play again? (yes/no):").lower()
    if again !="yes":
        print("game over")
        break
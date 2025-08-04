import random

options = ["stone", "paper", "scissors"]
user = input("Choose stone, paper or scissors: ").lower()
computer = random.choice(options)

print(f"Computer chose: {computer}")

if user == computer:
    print("Draw!")
elif (user == "stone" and computer == "scissors") or \
     (user == "paper" and computer == "stone") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")

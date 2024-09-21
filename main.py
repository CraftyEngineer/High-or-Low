import random

EASY_LEVEL_TURNS=5
HARD_LEVEL_TURNS=10

def setting_turns(choice):
  if choice=="easy":
    return EASY_LEVEL_TURNS
  elif choice=="hard":
    return HARD_LEVEL_TURNS

print("Welcome to the number guessing name!")
print("I'm thinking of a number between 1 to 100")
choice=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
global turns
turns=setting_turns(choice)
# print(turns)

def checking_guess(guess, number):
  if guess>number:
    print("\nToo High! Guess again.")
    turns-=1
    print(f"You have {turns} guesses remaining\n")

  elif guess<number:
    print("\nToo Low! Guess again.")
    turns-=1
    print(f"You have {turns} guesses remaining\n")

  else:
    print("\nYou guessed the correct number! You win")
    turns=-1



number=random.randint(1,100)
print(number)
while turns>0:
  guess=int(input("\nMake a guess: "))
  checking_guess(guess, number)
if turns==0:
  print(f"\nThe number was {number}")

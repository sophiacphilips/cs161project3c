# Sophia Philips
# GitHub Username: sophiacphilips
# Date: 10/12/2022
# This program is a integer guessing game.

#ask user for chosen number
print("Enter the integer for the player to guess:")
chosen_int=int(input())
#set initial tries to zero
tries=0

print("Enter your guess.")
while(True):
    guess=int(input())
    tries=tries+1
    if (guess > chosen_int):
        print("Too high - try again:")
        continue
    elif (guess < chosen_int):
        print("Too low - try again:")
        continue
    else:
        break

print("You guessed it in", tries, "tries.")


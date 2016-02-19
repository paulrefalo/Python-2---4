#!/usr/local/bin/python3
# 
# guess.py - guess an integer between 1 and 20

# globals
target = 12
guess = 0
tries = 0

while True:
    guess = int(input("Guess an integer 1 to 20 inclusive: "))
    
    tries = tries + 1	# increment attempts

    if ( guess < 1 or guess > 20 ):
        print("Behave yourself")
        continue
        
    if guess == target:
        print("Correct, Nostrodomus!  The number is", target)
        break
    elif tries >= 5:
        print("Sorry, the number was", target)
        break
    elif guess > target:
        print ("Guess lower...")
        continue
    elif guess < target:
        print ("Guess higher..")
        continue       
    else:
        print ("That's probably not a valid guess")
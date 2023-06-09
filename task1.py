#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''

n = 67

for i in range(10,0,-1):
    g = int(input(f"{i} guesses remaining: "))
    if g > n:
        print(f"{g} is too high!")
    elif g < n:
        print(f"{g} is too low!")
    else:
        print(f"Good job! The number is {n}")
        break
print("YOU FAILED.")
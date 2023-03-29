#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]

while True:
    u = input("\nEnter Username: ")
    if u in users:
        n = users.index(u)
        for i in range(3,0,-1):
            p = input(f"{u} ({n}), Enter Password ({i}): ")
            if p == passwords[n]:
                print(f"Welcome, {u}!")
                break
            elif p == "quit":
                print("Goodbye!")
                break
        else:
            print(f"Wrong Password for {u}. Try again? Or type \"quit\" to exit.")
            continue
    if u == "quit":
        print("Goodbye!")
        break
    elif u not in users:
        print(f"User \"{u}\" not found. Try again? Or type \"quit\" to exit.")
        continue
    else:
        break
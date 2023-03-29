#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''


expectedUsername = "systemadmin"
expectedPassword = "master"


u = input("Enter Username: ")

if u == expectedUsername:
    for i in range(3,0,-1):
        p = input(f"({i}) Enter Password: ")
        if p == expectedPassword:
            print(f"Welcome, {expectedUsername}!")
            break
        else:
            print(f"Wrong Password. Idiot.")
    print("You died.")
else:
    print(f"User \"{u}\" not found!")
import random

options = ["rock", "paper", "scissors"]

user_option =  input("Choose between rock, paper, and scissors: ")

computer_option = options[random.randint(0,3)]

print("computer : ",computer_option)
print("user : ",user_option)

if(computer_option == user_option):
    print("it's a tie")
elif(computer_option == "rock"):
    if (user_option == "paper"):
        print("you won")
    elif (user_option == "scissors"):
        print("you lost")
elif(computer_option == "paper"):
    if (user_option == "scissors"):
        print("you won")
    elif (user_option == "rock"):
        print("you lost")
elif(computer_option == "scissors"):
    if (user_option == "rock"):
        print("you won")
    elif (user_option == "paper"):
        print("you lost")
        

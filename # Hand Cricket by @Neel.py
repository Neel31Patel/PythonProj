# Hand Cricket by @Neel

import random

# Welcome
print("Welcome to Hand Cricket by @Neel!")
print("We will first do the toss!")

# Toss
toss = random.randint(1,2)
flip = input("Heads or Tails? ")

if flip.lower() == "heads" and toss == 1:
    choice = input("You won the toss, what do you choose to do? Bat or Bowl: ")
    if choice.lower() == "bat":
        user_choice = "bat"
    elif choice.lower() == "bowl":
        user_choice = "bowl"    


elif flip.lower() == "heads" and toss == 2:
    program_choice = random.randint(1,2)
    if program_choice == 1:
        user_choice = "bowl"
        print("Sorry you lost the toss and I choose to bat!")
    elif program_choice == 2:
        user_choice = "bat"
        print("Sorry you lost the toss and I choose to bowl!")

if flip.lower() == "tails" and toss == 1:
    choice = input("You won the toss, what do you choose to do? Bat or Bowl: ")
    if choice.lower() == "bat":
        user_choice = "bat"
    elif choice.lower() == "bowl":
        user_choice = "bowl"    

elif flip.lower() == "tails" and toss == 2:
    program_choice = random.randint(1,2)
    if program_choice == 1:
        user_choice = "bowl"
        print("Sorry you lost the toss and I choose to bat!")
    elif program_choice == 2:
        user_choice = "bat"
        print("Sorry you lost the toss and I choose to bowl!")

# Let's play
print("Lets play! You", user_choice, "first!")

# Rules
print("""
1.) We both pick numbers from 1 to 6.
2.) If both of our numbers match, a wicket is lost and we swap turns.
3.) If our numbers dont match, runs are added to the batsmen.     
4.) At the end, whoever has the most runs wins.
5.) If we both end the game with the same amount of runs, it is a tie.      
""")

# Runs
runs_player = 0
runs_computer = 0

# Main game loop
while user_choice == "bat":         # User bats
    number_computer = random.randint(1,6) # Computer generates random number
    number_player = int(input("Enter a number from 1 to 6: ")) # User inputs a number

    # User's guess invalid
    if number_player >= 7 or number_player <= 0:
        print("Sorry, you can't choose a number greater than 6 or less than 1!")

    # Computer's guess(bowler) not equals to User's guess(batter)
    elif number_computer != number_player:
        runs_player += number_player
        print("Runs:", runs_player)

    # Computer's guess(bowler) equals to User's guess(batter)
    elif number_computer == number_player:
        print("Sorry, we both picked:", number_computer)
        print("You scored", runs_player, "runs.")
        print("Now it's my turn to bat!")
        user_choice = "bowl"
        
        while user_choice == "bowl":         # User bowls
            number_computer = random.randint(1,6) # Computer generates random number
            number_player = int(input("Enter a number from 1 to 6: ")) # User inputs a number

            # User's guess invalid
            if number_player >= 7 or number_player <= 0:
                print("Sorry, you can't choose a number greater than 6 or less than 1!")

            # User's guess(Bowler) not equals to Computer's guess(Batter)
            elif number_player != number_computer:
                runs_computer += number_computer
                print("Runs:", runs_computer)
                # Computer wins
                if runs_player < runs_computer:
                    print("Unlucky! I win. Try again next time!")
                    exit()

            # User's guess(Bowler) equals Computer's guess(Batter) & User wins
            elif number_player == number_computer and runs_player > runs_computer:
                print("Well done, I also picked", number_computer)
                print("I scored", runs_computer, "runs.")
                print("Congratulations! You win!")
                exit()

            # Tie
            elif number_player == number_computer and runs_player == runs_computer:
                print("It's a Tie!")
                exit()



while user_choice == "bowl":         # User bowls
    number_computer = random.randint(1,6) # Computer generates random number
    number_player = int(input("Enter a number from 1 to 6: ")) # User inputs a number

    # User's guess invalid
    if number_player >= 7 or number_player <= 0:
        print("Sorry, you can't choose a number greater than 6 or less than 1!")

    # User's guess(Bowler) not equals to Computer's guess(Batter)
    elif number_player != number_computer:
        runs_computer += number_computer
        print("Runs:", runs_computer)

    # User's guess(Bowler) equals to Computer's guess(Batter)
    elif number_player == number_computer:
        print("Well done, I also picked", number_player)
        print("I scored", runs_computer, "runs.")
        print("Now it's my turn to bowl!")
        user_choice = "bat"
    
        while user_choice == "bat":         # User bats
            number_computer = random.randint(1,6) # Computer generates random number
            number_player = int(input("Enter a number from 1 to 6: ")) # User inputs a number

            # User's guess invalid
            if number_player >= 7 or number_player <= 0:
                print("Sorry, you can't choose a number greater than 6 or less than 1!")

            # Computer's guess(Bowler) not equals User's guess(Batter)
            elif number_computer != number_player:
                runs_player += number_player
                print("Runs:", runs_player)
                # User wins
                if runs_computer < runs_player:
                    print("Congratulations! You win!")
                    exit()
            
            # Computer's guess(Bowler) equals User's guess(Batter) & Computer wins
            elif number_computer == number_player and runs_computer > runs_player:
                print("Sorry, we both picked:", number_computer)
                print("You scored", runs_player, "runs.")
                print("Unlucky! I win. Try again next time!")
                exit()

            # Tie
            elif number_computer == number_player and runs_computer == runs_player:
                print("It's a Tie!")
                exit()
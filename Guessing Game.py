from random import randint

print("Welcome to the game")
player_name = input("\n\nWhat's your name? ")
print("Okay {}, I'm guessing a random number beetween 1 and 10. Can you guess it? ".format(player_name))

machine_number = randint(1, 10)
tries = 3

for tries in range(1, tries + 1):
    guessed_number = int(input("Guess a number: "))
    if guessed_number == machine_number:
        print("You win in {} roll.".format(tries))
        break
    elif guessed_number > machine_number:
        print("Guess a lower number!")
    else:
        print("Guess a upper number!")
print("\nThe number was {}. Thanks for playing!!!".format(machine_number))

import random
from Logo import logo


def hard():
    count = 0
    while count < 5:
        guess = int(input("Please guess the number: "))
        if guess == random_number:
            print(f"The guess was correct")
            break
        rem = 4 - count
        count = count + 1
        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too High")
        print(f"Your guess was incorrect. You have {rem} attempt remaining.")
    print(f"The correct ans is: {random_number}")


def easy():
    count = 0
    while count < 10:
        guess = int(input("Please guess the number: "))
        if guess == random_number:
            print(f"The guess was correct")
            break
        rem = 9 - count
        count = count + 1
        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too High")
        print(f"Your guess was incorrect. You have {rem} attempt remaining")
    print(f"The correct ans is: {random_number}")


play = "y"
while play == "y":
    print(logo)
    random_number = random.randint(1, 100)
    print("Welcome to the game!!")
    level = input("Please Choose hard or easy level. h for hard ans e for easy: ").lower()
    if level == "h":
        hard()
    elif level == "e":
        easy()
    play = input("Do you want to play again: y for yes and n for no: ").lower()
print("\nThank you for playing....")






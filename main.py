import random


def main():
    target_num = random.randint(1, 100)
    attempts = 0
    nerves_left = 3

    while True:
        if nerves_left <= 0:
            print("\n All I require are numbers, NUMBERS!! IS THAT TOO MUCH TO ASK? \n")
            break
            
        
        guess = input("Guess the number: ")

        if not guess.isdigit():
            print("Enter a valid number.")
            nerves_left -= 1
            continue

        guess = int(guess)
        attempts += 1

        if guess < target_num:
            print("Too low")
        elif guess > target_num:
            print("Too high")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break
        
    decision = input("Play again?: ")

    if "".join(decision.strip().split()).lower() in ["yes", "yea", "yup", "ye", "not no", "absolutely", "maybe"]:
        main()
main()

import random

attempts_list = []


#def show_score():    
 #   print("There is currently no high score, it's yours for the taking!" if len(attempts_list) <= 0 else f"The current high score is {min(attempts_list)} attempts")


def menu():
    print(" 1 - Play")
    print(" 2 - instruction")
    print(" 0 - Exist")


def start_game():
    random_number = random.randint(1, 10)

    print(random_number)
    menu()
    wanna_play = input("Enter the menu : ")

    attempts = 0
    

    while int(wanna_play) == 1:

        try:
            guess = input("Pick a number between 1 and 10 ")

            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")

            elif int(guess) == random_number:
                print("Nice! You got it!")

                attempts += 1
                attempts_list.append(attempts)

                print(f"It took you {attempts} attempts")

                


            elif int(guess) < random_number:
                print("your number is lower")
                attempts += 1

            elif int(guess) > random_number:
                print("your number is higher")
                attempts += 1

        except ValueError as err:
            print(err) 



if __name__ == '__main__':
    start_game()
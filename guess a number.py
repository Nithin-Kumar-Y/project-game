import random as r
def guess_number():
    print("Welcome to 'Guess A Number'")
    number = r.randint(1, 100)  #1- 100
    user_numb = -1
    while number != user_numb:
        user_numb = int(input("Enter a numb: "))
        if user_numb < number:
            print("Its too low")
        elif user_numb > number:
            print("Its too high")
        elif user_numb == number:
            print(" Congrats! You guessed right")

def play_again():
    play = int(input("Enter 0 to play again OR 1 to end: "))
    if play == 0:
        guess_number()
    elif play ==1:
        print("THANK YOU. You exited")
    else:
        print("Please enter valid option")

guess_number()
play_again()

## ALL FINE
## ADD EXCEPT TRY FINALLY TO FIX IT FIALLY
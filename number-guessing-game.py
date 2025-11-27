import random as rdm

def guess_number(min_num, max_num):
  computer_number = rdm.randrange(min_num,max_num + 1)
  user_guess = None

  while user_guess != computer_number:
    user_guess = int(input("guess the number between 1-10:"))

    if user_guess > computer_number:
      print("Too high")

    elif user_guess < computer_number:
      print("Too low")

    else:
      print("Correct! You guessed the number")
      break
guess_number(1,10)


  
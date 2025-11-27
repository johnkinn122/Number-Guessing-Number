PSEUDOCODE: Number Guessing Game (With Loop + High/Low):
START

GENERATE a random number between 1 and 10 → call this COMPUTER_NUMBER

SET USER_GUESS to nothing (or empty)

WHILE USER_GUESS is NOT EQUAL to COMPUTER_NUMBER:

    ASK the user to "Enter a number between 1 and 100"
    GET the number → store in USER_GUESS

    IF USER_GUESS is GREATER than COMPUTER_NUMBER:
        DISPLAY "Too high!"

    ELSE IF USER_GUESS is LESS than COMPUTER_NUMBER:
        DISPLAY "Too low!"

    ELSE:
        DISPLAY "Correct! You guessed the number!"

END WHILE

END

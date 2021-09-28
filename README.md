# 5-Python-Projects-for-Beginners
These projects should take a maximum of of 15 minutes each to understand and then about half an hour to try yourself.


## Number Guessing Game:
- The user selects a range, let’s say from 1 to 50.
- Then the compiler randomly selects  an integer in the range.
- The minimum number of guesses depends upon range. And the compiler must calculate the minimum number of guessing depends upon the range, on its own. For this, we have a formula:-
<p align=center> Minimum number of guessing = log2(Upper bound – lower bound + 1) </p>

- Now the user guesses till he/she gets it right or Minimum number of guessing = 0
- If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
- Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
- And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
- Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.

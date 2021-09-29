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
- You will require to install Random and math libraries in Python, it is pre-installed in the Python programming language.

## Random Password Generator:
- In this project we ask the user to input the desired lenght of password to be created
- Then we generate a password of given lenght and print it for the user.

## URL Shortener
- This program takes your existing long URL and encodes it into a shorter version of itself using an API.
- To run the program in your CMD type - Python filename.py URL

## Weather Forecaster:
- This weather application gets real-time weather conditions for any city using Python. 
- Instead of using an API, the program takes the name of a city and returns the weather information for that city by scratching the web.
- You will require to install Beautifulsoup and requests libraries in Python to extract the data directly from Google.
- The requests library comes preinstalled in the Python programming language.
- You can install the Beautifulsoup library by using a pip command; pip install beautifulsoup4. Remember that this library is imported by the name of bs4 in your Python code.
- The time generated in the output may not be same as the exact real-time. It will show the lower bound of the hour of your real-time.













#!/usr/local/bin/python3

from cgitb import enable
enable()

from os import environ
from http.cookies import SimpleCookie

outcome = "GET LOST!"
welcome = 0
cookie = SimpleCookie()
http_cookie_header = environ.get('HTTP_COOKIE')
if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'Welcome' in cookie:
            welcome = int(cookie['Welcome'].value)
            if welcome > 4:
                    outcome = ""

from cgi import FieldStorage
import random

print('Content-type: text/html')
print()

form_data = FieldStorage()
guess = form_data.getlist('guess')
computer = random.randint(0,2)
legal_values = ['Rock', 'Paper', 'Scissors']
if len(form_data) != 0 and welcome > 4:
    if len(guess) != 1:
        outcome = "Error!"
    elif guess[0] not in legal_values:
        outcome = "Error! - Please use the form!"
    else:
        if computer == 0:
            computer = 'Rock'
        elif computer == 1:
            computer = "Scissors"
        elif computer == 2:
            computer = "Paper"
        if guess[0] == computer:
            outcome = "Computers %s Ties with Your %s" %(computer, guess[0])
        elif guess[0] == 'Rock':
            if computer == 'Paper':
                outcome = 'Computers Paper Beats Your Rock'
            elif computer == 'Scissors':
                outcome = 'Your Rock Beats Computers Scissors'
        elif guess[0] == 'Scissors':
            if computer == 'Rock':
                outcome = 'Computers Rock Beats Your Scissors'
            elif computer == 'Paper':
                outcome = "Your Scissors Beats Computers Rock"
        elif guess[0] == 'Paper':
            if computer == 'Rock':
                outcome = 'Your Paper Beats Computers Rock'
            elif computer == 'Scissors':
                outcome = 'Computers Scissors Beats Your Paper'



print("""
<!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Bonus Game</title>
            <script src="rps.js"></script>
            <link rel="stylesheet" href="rps.css" />
        </head>
        <body>
            <header>
                <h1>Bonus Game</h1>
                <p>
                    ROCK PAPER SCISSORS
                </p>
            </header>
            <main>
                <form action="rsp.py" method="get">
                    <p>Take Your Pick</p>

                    
                    <input type="radio" name="guess" value="Rock" id="rock" />
                    <label for="rock"><img src="images/rock.jpg" alt="Rock" /></label>

                    
                    <input type="radio" name="guess" value="Scissors" id="scissors" />
                    <label for="scissors"><img src="images/scissors.jpg" alt="Scissors" /></label>

                    
                    <input type="radio" name="guess" value="Paper" id="paper" />
                    <label for="paper"><img src="images/paper.jpg" alt="Paper" /></label>

                    
                    <input type="submit" id="result" value="Play!" />
                </form>
                <p id="outcome">
                    %s
                </p>
                <a href="http://cs1.ucc.ie/~dr13/cgi-bin/lab7/rsp.py">Play Again</a>
                <a href="http://cs1.ucc.ie/~dr13/cgi-bin/lab7/index.py">Home</a>
            </main>    
        </body>
    </html>""" %(outcome))




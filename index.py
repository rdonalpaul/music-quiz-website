#!/usr/local/bin/python3

from cgitb import enable 
enable()
from os import environ
from http.cookies import SimpleCookie
import pymysql as db

cookie = SimpleCookie()
http_cookie_header = environ.get('HTTP_COOKIE')
if not http_cookie_header:
    cookie['Welcome'] = 1
else:
    cookie.load(http_cookie_header)
    if 'Welcome' not in cookie:
        cookie['Welcome'] = 1
    else:
        cookie['Welcome'] = int(cookie['Welcome'].value) + 1
cookie['Welcome']['expires'] = 604800
print(cookie)
            
print('Content-Type: text/html')
print()
bonus = ''
welcome_msg = "Welcome"
result = ''
if int(cookie['Welcome'].value) > 1:
    welcome_msg = "Welcome Back"
if int(cookie['Welcome'].value) > 4:
    welcome_msg = "Don't Forget to Leave a Comment!"
if int(cookie['Welcome'].value) > 4:
    welcome_msg = "Don't Forget to Leave a Comment!"
    bonus = "<a href='http://cs1.ucc.ie/~dr13/cgi-bin/lab7/rsp.py'>Bonus Game</a>"
    

    
    
try:
    connection = db.connect('cs1.ucc.ie','dr13','chujohqu','csdipact2017_dr13')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT DISTINCT qID, QuizName
                      FROM questions """)
    if cursor.rowcount == 0:
        result = '<p>Undergoing scheduled mainenance. Please call back later</p>'
    else:
        result = ''
        for row in cursor.fetchall():
            
            result += """<tbody>
                        <tr>
                         <td>%s</td>
                         <td><a href="http://cs1.ucc.ie/~dr13/cgi-bin/lab7/%s.py">%s</a></td>
                        </tr>
                    </tbody>"""%(row['qID'], row['QuizName'],row['QuizName'] )

     
    cursor.close()  
    connection.close()
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'



print("""<!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="home.css" />
            <title>Home</title>
        </head>
        <header>
            <h1>Test Your Knowlege!</h1>
            <p>
                Select a Quiz below
            </p>
        </header>
        <body>
            <h1>
                <h2>%s</h2>
                <h2>%s</h2>
            </h1>
                 <table>
                    <thead>
                        <tr>
                            <th >Quiz No.</th>
                            <th >Quiz Name</th>
                        </tr>
                    </thead>
                    %s
                </table>
        </body>
        
    </html>
    """%(welcome_msg, bonus, result))

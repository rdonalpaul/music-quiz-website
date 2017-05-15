#!/usr/local/bin/python3

from cgitb import enable 
enable()

import pymysql as db
from comments import show_comments
            
print('Content-Type: text/html')
print()

result = ''
question_number = 0
try:
    connection = db.connect('cs1.ucc.ie','dr13','chujohqu','csdipact2017_dr13')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT *
                      FROM questions
                      WHERE qID = '1' """)
    if cursor.rowcount == 0:
        result = '<p>Undergoing scheduled mainenance. Please call back later</p>'
    else:
        result = ''
        for row in cursor.fetchall():
            question_number += 1
            result += """<p class='question'>%s - %s</p>
                         <input type='radio' name='%s' value='%s' onclick='init(event,\"%s\" )' id='%s' class='%s'/>
                         <label for='%s'>%s</label>
                         <input type='radio' name='%s' value='%s' onclick='init(event,\"%s\" )' id='%s' class='%s'/>
                         <label for='%s'>%s</label>
                         <input type='radio' name='%s' value='%s' onclick='init(event,\"%s\" )' id='%s' class='%s'/>
                         <label for='%s'>%s</label>
                         <div id='%s' class = 'results'></div>"""\
                         %(question_number, row['Question'], row['ID'],row['Answer1'], row['ID'], row['Answer1'],row['ID'], row['Answer1'], row['Answer1'], row['ID'], row['Answer2'],row['ID'],row['Answer2']\
                           ,row['ID'], row['Answer2'],row['Answer2'],row['ID'], row['Answer3'],row['ID'] ,row['Answer3'],row['ID'],row['Answer3'],row['Answer3'], row['ID'])

     
    cursor.close()  
    connection.close()
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""<!DOCTYPE html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="quiz.css" />
            <script src="quiz.js"></script>
            <meta charset="utf-8" />
            <title>Quiz</title>
        </head>
        <body>
            <header>
                <h1>Millionaire Quiz</h1>
                <p>
                    Are you as smart as a Millionaire?
                </p>
                
            </header>
            <main>
                <h1> Millionaires Quiz </h1>
                <p class = "description">
                    These are some of the million dollar/pound questions from both the US and British
                    versions of Who Wants to be a Millionaire.
                    Do you have what it takes to get all questions correct?
                </p>
                <form method="get">
                    %s
                    <input type="submit" value="Total Score" id="final_result" />
                    <div id="finalResult"></div>
                </form>
                <a href="http://cs1.ucc.ie/~dr13/cgi-bin/lab7/index.py">Home</a>
                <a href="http://cs1.ucc.ie/~dr13/cgi-bin/lab7/Millionaire.py">Play Again</a>
            </main>
           %s
        </body>
    </html>""" %(result, show_comments()))



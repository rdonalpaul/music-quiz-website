#!/usr/local/bin/python3

from cgitb import enable 
enable()

from os import environ

from cgi import FieldStorage, escape
import pymysql as db


          
print('Content-Type: text/plain')
print()

name = environ['QUERY_STRING']
name2 = name.split("=")
name3 = name2[0]

form_data = FieldStorage()
selection = form_data.getlist(name3)

try:    
    connection = db.connect('cs1.ucc.ie','dr13','chujohqu','csdipact2017_dr13')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT *
                      FROM questions WHERE ID = %s""" %(name3))
    try:
        if cursor.rowcount == 0:
            print('Undergoing scheduled mainenance. Please call back later')
        else:

            for row in cursor.fetchall():
                if selection[0] != row['CorrectAnswer']:
                    print("Incorrect")
                else:
                    print('Correct' )
    except IndexError:
        print('Error!!')
    cursor.close()  
    connection.close()
except db.Error:
    print('Sorry. We are experiencing technical difficulties. Please Try Again Later')
   
    


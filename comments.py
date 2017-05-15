#!/usr/local/bin/python3

from cgitb import enable 
enable()

def show_comments():
    from cgi import FieldStorage
    import pymysql as db
    from os import environ

    user_comments = ''
    url = environ.get('SCRIPT_NAME')
    try:
        connection = db.connect('cs1.ucc.ie','dr13','chujohqu','csdipact2017_dr13')
        cursor = connection.cursor(db.cursors.DictCursor)
        form_data = FieldStorage()
        if len(form_data) != 0:   
            username = form_data.getfirst('username')
            new_comment = form_data.getfirst('new_comment')
            cursor.execute("""INSERT INTO user_comments (username, url, comment)
                              VALUES (%s, %s, %s)""", (username, url, new_comment))
            connection.commit()
        cursor.execute("""SELECT * FROM user_comments 
                          WHERE url = %s
                          ORDER BY comment_id DESC""", (url))
        for row in cursor.fetchall(): 
            user_comments += '<article><h1>%s</h1><p>%s</p></article>' % (row['username'], row['comment'])
        cursor.close()  
        connection.close()
    except db.Error:
        user_comments = '<p>User Comments cannot be displayed. Please try again later.</p>'

    return """
        <section>
            <h1>Did you like the Quiz? Have you ideas for a quiz?</h1>
            <form action="%s" method="post">
                <fieldset>
                    <legend>Tell us below</legend>
                    <label for="username">Name:</label>
                    <input type="text" name="username" id="username" />
                    <label for="new_comment">Comment:</label>
                    <textarea name="new_comment" id="new_comment" rows="5" cols="50">
                    </textarea>
                    <input type="submit" id="x"/>
                </fieldset>
            </form>
        </section>
        <section id="comments">
        <h1>User Comments</h1>
            %s
        </section>""" % (url, user_comments)
    


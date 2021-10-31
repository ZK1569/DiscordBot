import sqlite3

#Create a database if not exist or connect if exist
db = sqlite3.connect('HomeWork.db')

#Create a curser :
c = db.cursor()


#Create a table
c.execute("""CREATE TABLE schoolwork (
    statue int,
    subject text,
    date_add text,
    date_end text,
    work text,
    force text,
    groupe text
)""")



# Commit our command 
db.commit()

#Close our connection
db.close()
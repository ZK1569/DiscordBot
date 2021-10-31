#il y a tout a faire dans ce truque de merde je sais meme pas par ou commencer 

import sqlite3

#Create a database if not exist or connect if exist
db = sqlite3.connect('HomeWork.db')
#Create a curser :
c = db.cursor()

c.execute("""INSERT INTO schoolwork VALUES (
    0,
    'Francais',
    'auj',
    'demain',
    'faire un test',
    1,
    'tous'
)""")

# Commit our command 
db.commit()

#Close our connection
db.close()
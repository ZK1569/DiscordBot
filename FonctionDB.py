import sqlite3
import os
import datetime

#Create a database if not exist or connect if exist
db = sqlite3.connect('HomeWork.db')

#Create a curser :
c = db.cursor()

def addHomeWork(subject, date_end, work):
    success = True
    date_add = datetime.datetime.now()
    try:
        date_end = datetime.datetime.strptime(date_end, '%d/%m/%y')

        print("WORK ADD : {}, {} to {}, Work: {}, for ALL".format(subject, date_add, date_end, work))

        c.execute("""INSERT INTO schoolwork VALUES (
            0,
            ?,
            ?,
            ?,
            ?,
            '4',
            'ALL')""",[subject,date_add,date_end,work]
            )
        # Commit our command 
        db.commit()
    except:
        success = False

    return success

#Close our connection
#db.close()
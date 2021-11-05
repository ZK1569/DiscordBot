import datetime
import schedule
import sqlite3 
import time

#Create a database if not exist or connect if exist
db = sqlite3.connect('HomeWork.db')
print("Connected to database")

#Create a curser :
c = db.cursor()

def changeStatue():

    today = datetime.datetime.now() # Get the day 
    today = today.strftime("%Y-%m-%d 00:00:00")# Convert in the same format as the database

    c.execute("""SELECT rowid FROM schoolwork WHERE statue=0 AND date_end=?""",[today])
    items = c.fetchall()
    if len(items) != 0:
        for i in items:
            c.execute("""
            UPDATE schoolwork SET statue = 1
            WHERE rowid = ?
            """,[i[0]])
            db.commit()
            print("AUTO CHANGE :",i[0], "Statue changed into 1")
    else:
        print ("AUTO CHANGE : No homework for {}.".format(today))


schedule.every().days.at('23:55').do(changeStatue)


while 1:
    schedule.run_pending()
    time.sleep(60)
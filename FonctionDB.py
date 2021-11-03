import sqlite3
import os
import datetime

#Create a database if not exist or connect if exist
db = sqlite3.connect('HomeWork.db')

#Create a curser :
c = db.cursor()

def addHomeWork(subject, date_end, groupe, work):
    success = True
    date_add = datetime.datetime.now()
    try:
        date_end = datetime.datetime.strptime(date_end, '%d/%m/%y')

        c.execute("""INSERT INTO schoolwork VALUES (
            0,
            ?,
            ?,
            ?,
            ?,
            '4',
            ?)""",[subject, date_add, date_end, work, groupe]
            )
        # Commit our command 
        db.commit()
        print("WORK ADD : {}, {} to {}, Work: {}, for ALL".format(subject, date_add, date_end, work))
    except:
        success = False

    return success


def getHomeworkWithDate(date):
    
    try:
        date = datetime.datetime.strptime(date, '%d/%m/%y')

        c.execute("""SELECT subject, work FROM schoolwork WHERE date_end=?""",[date])
        items = c.fetchall()

    except:
        items = "ERREUR : Can't access to database."
    
    return items

def getHomeworkWithSubject(subject):
    
    c.execute("""SELECT date_end, subject, work FROM schoolwork WHERE subject=? and statue=0""",[subject])
    items = c.fetchall()
    end = []


    for colOne in range(0,len(items)-1):
        date = items[colOne][0][0:10] , items[colOne][1], items[colOne][2]
        end.append(date)

    return end

    #************** Voir si possible de faire plus solie 
    # Pour le moment focntionnelle 
    # Changer aussi la mise dans l'ordre des dates


    

#Close our connection
#db.close()
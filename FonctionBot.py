import FonctionDB as FDB 
import datetime

#--------------------------------------------------------------------

def botAdd(subject, date_end, groupe, work):

    # List of all the subject autorised by the bot
    lsSubjects = ["francais", "anglais", "dev"]
    lsGroupe = ["all", "slam", "sisr"]

    # If the command send by the user is correct 
    if subject.lower() in lsSubjects: # Subject 
        if groupe.lower() in lsGroupe:# Groupe
            # Add to database and send a message
            success = FDB.addHomeWork(subject.lower(), date_end, groupe.lower(), work)
            if success:
                reply  = "Devoir de {} ajouté pour le {}".format(subject, date_end)
            else:
                reply = "ERREUR : La sauvegarde impossible."
        else:
            reply = "ERREUR : Le groupe n'est pas reconnu."
    else:
        reply = "ERREUR : La matiere n'est pas reconnu."

    return reply

#--------------------------------------------------------------------

def botGetWithDate(date):

    info = FDB.getHomeworkWithDate(date)
    info = reorder(info)

    return info

#--------------------------------------------------------------------

def botGetWithSubject(subject):
    
    info = FDB.getHomeworkWithSubject(subject)
    final = []
    end = []

    for colOne in range(0,len(info)-1):
        year = info[colOne][0][0:4] #get the year in the string from the database
        month = info[colOne][0][5:7]
        day = info[colOne][0][8:10]
        date = "{}/{}/{}".format(day, month, year) # Reogranise this
        date = date, info[colOne][1], info[colOne][2] #Add the informations
        end.append(date) 

    if len(end) != 0:
        for first in end:
            work = []
            for i in first:
                work.append(i)
            work = ' ==> '.join(work)
            final.append(work)
        
        final = "\n".join(final)

    else:
        final = "No homework for this subject"

    return final

#--------------------------------------------------------------------

def everyTime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    current_day = datetime.datetime.now().weekday()

    # Change the satatue of the homework every day
    if current_time == '08:53':
        FDB.everyDay(now)

    # Send a message whith the homework for the week
    if current_day == 0: 
        if current_time == "09:00":
            now = now.strftime("%d/%m/%y")
            info = FDB.getHomeworkWithDate(now)
            done = reorder(info)

            return done

#--------------------------------------------------------------------




#--------------------------------------------------------------------
def reorder(info):
    final = []

    if type(info) == list: # If it return the list and not an error message 
        if len(info) != 0: # If there is a work to do for this day
            for first in info: #Do the proccess
                work = []
                for i in first:
                    work.append(i)
                work = ' : '.join(work)# Convert le list into a string and put a ' ' between the element if the list
                final.append(work)
            
            final = "\n".join(final)# Same as work but add a '\n' between
        else:
            final = 'No homework for this day.'
    else:
        final = info

    return final


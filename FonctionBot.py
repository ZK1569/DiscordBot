import FonctionDB as FDB 


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


def botGetWithDate(date):

    info = FDB.getHomeworkWithDate(date)
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

def botGetWithSubject(subject):
    
    info = FDB.getHomeworkWithSubject(subject)
    final = []

    if len(info) != 0:
        for first in info:
            work = []
            for i in first:
                work.append(i)
            work = ' ==> '.join(work)
            final.append(work)
        
        final = "\n".join(final)

    else:
        final = "No homework for this subject"

    return final

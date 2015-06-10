#6/10/2015
#Michael Kohlmann
#devCodeCamp - Personal Project

"""
This program will be a small widget that will sit on your desktop. It will have a note field, where you can
track what project you are working on, or what function you are working on. A start button will start the tracking
of time. A pause button will pause the timer without closing and logging the entry. And a stop button will take
the running time, and log it to a file.

Future Iterations: 
1. I'd like to tweak it to save it to a database.
2. I'd like to make it more like a project management tracking tool, so it incorporates these times, and logs it
   for a specific project. (ie. if a project has 40 hours available to it, it will track how close you are to being
   within your budget, etc.)
3. It would be nice to have a server/client set-up, so that users can log in remotely, and the manager can
   review progress and budgets.
4. If I extend it to a project management tool, hardware costs, and other costs may be incorporated.

"""
from datetime import *
from DataEntryClass import *


def main():
    #Debug Area
    DEBUG = True
    now = datetime.now()
    then = now.replace(hour=8)
    
    logEntry = DataEntry()
    logEntry.setProjectNumber("0001")
    logEntry.setTaskComment("Generic Task Comment")
    logEntry.setStartTime(then)
    logEntry.setStopTime(now)

    
    logEntry.debugPrintEntry()
    logEntry.calculateCumulativeTime()
    logEntry.debugPrintEntry()
    
    logEntry.exportToLogFile()
    logEntry.setProjectNumber("0002")
    logEntry.exportToLogFile()
    return

def debug(message):
    DEBUG = True
    if DEBUG:
        print(message)
    return
     
     
if __name__ == "__main__":
    main()

    

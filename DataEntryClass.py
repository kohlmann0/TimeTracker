#6/10/2015
#Michael Kohlmann
#devCodeCamp - Personal Project

from datetime import *
import os


class DataEntry:
    def __init__(self):
        self.projectNumber = ""
        self.taskComment = ""
        self.startTime = time
        self.stopTime = time
        self.cumulativeTime = timedelta(0)

########    
# SETS #    
########
    def setProjectNumber(self,value):
        self.projectNumber = str(value)
        return
        
    def setTaskComment(self,value):
        self.taskComment = str(value)
        return

    def setStartTime(self,value):
        self.startTime = value
        return

    def setStopTime(self,value):
        self.stopTime = value
        return

########
# GETS #
########        
    def getProjectNumber(self):
        return self.projectNumber
        
    def getTaskComment(self):
        return self.taskComment

    def getStartTime(self):
        return self.startTime

    def getStopTime(self):
        return str(self.stopTime)

    def getCumulativeTime(self):
        return str(self.cumulativeTime)

###################        
# DEBUG FUNCTIONS #
###################
    def debugPrintEntry(self):
        print(">DEBUG: Log Entry Contains")
        print(">-------------------------")
        print(">Project number  = " + str(self.projectNumber))
        print(">Task Comment    = " + str(self.taskComment))
        print(">Start Time      = " + str(self.startTime))
        print(">Stop Time       = " + str(self.stopTime))
        print(">Cumulative Time = " + str(self.cumulativeTime))
        
        
####################
# HELPER FUNCTIONS #
####################
    def calculateCumulativeTime(self):
        self.cumulativeTime = (self.stopTime - self.startTime) + self.cumulativeTime
        return

    def exportToLogFile(self, fileName="time_log.txt"):
        timeStamp = datetime.now()
        logFile = open(fileName, "a+")
        entry = (str(timeStamp) + "\t" + 
                 self.projectNumber + "\t" + 
                 str(int(round(self.cumulativeTime.total_seconds())))+ "\t" + 
                 self.taskComment + "\n")
        logFile.writelines(entry)
        logFile.close()
    
    def resetAll(self):
        self.projectNumber = ""
        self.taskComment = ""
        self.startTime = time
        self.stopTime = time
        self.cumulativeTime = timedelta(0)
    
    def startTimer(self):
        self.startTime = datetime.now()
        return
        
    def stopTimer(self):
        self.stopTime = datetime.now()
        self.calculateCumulativeTime()
        return
        
    def pauseTimer(self):
        self.stopTimer()
        return
    
    def unpauseTimer(self):
        self.startTimer()
        return
    
    
    
        

    
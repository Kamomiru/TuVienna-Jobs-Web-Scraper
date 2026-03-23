import json
import os
from datetime import datetime

JOBFILE = "seenJobs.json"
DATEFILE = "dates.json"


def resetLogger():
    with open(JOBFILE, "w") as f:
        json.dump([], f, indent=2)
    with open(DATEFILE, "w") as f:
        json.dump([], f, indent=2)


#----------Jobs----------
def loadSeenJobs():
    if not os.path.exists(JOBFILE):
        return []

    with open(JOBFILE, "r") as f:
        JOB = json.load(f)
        return JOB

def saveSeenJobs(seenJobs):
    with open(JOBFILE, "w") as f:
        json.dump(seenJobs, f, indent=2)


#----------Date----------
def loadCheckedDates():
    if not os.path.exists(DATEFILE):
        return []

    with open(DATEFILE, "r") as f:
        checkedDates = json.load(f)
        return checkedDates

def logDate():
    checkedDates = loadCheckedDates()
    checkedDates.append(getDate())

    with open(DATEFILE, "w") as f:
        json.dump(checkedDates, f, indent=2)

def getDate():
    return datetime.now().strftime("%H:%M %d-%m-%Y")

def getLastUpdateTime():
    dates = loadCheckedDates()
    return dates[-1]


    


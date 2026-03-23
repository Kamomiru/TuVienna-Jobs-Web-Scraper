#Tu Wien Job scraper for Studentjobs

#scrapes Tuwien Job page and sorts them according to EXCEMPTION_KEYWORDS and INSTITUTES
#you can set those keywords by accessing WebScraperModule.py

from WebScraperModule import Scraper
from TkinterApplicationModule import ApplicationWindow
import DataLoggerModule as logger



testData= [
  {
    "Title": "Universit\u00e4tsassistent_in Laufbahnstelle",
    "Location": "BWF: 26.03.2026 | Institut f\u00fcr Diskrete Mathematik und Geometrie",
    "Link": "https://jobs.tuwien.ac.at/Job/263243",
    "Color": "grey"
  },
  {
    "Title": "Studentische_r Mitarbeiter_in",
    "Location": "BWF: 09.04.2026 | Geb\u00e4ude und Technik",
    "Link": "https://jobs.tuwien.ac.at/Job/265075",
    "Color": "grey"
  },
  {
    "Title": "Studentische_r Mitarbeiter_in",
    "Location": "BWF: 09.04.2026 | Institut f\u00fcr Managementwissenschaften",
    "Link": "https://jobs.tuwien.ac.at/Job/265157",
    "Color": "grey"
  },
  {
    "Title": "Studentische_r Mitarbeiter_in",
    "Location": "BWF: 02.04.2026 | Arbeitskreis f\u00fcr Gleichbehandlungsfragen (AKG)",
    "Link": "https://jobs.tuwien.ac.at/Job/265148",
    "Color": "grey"
  }]

#gets jobs through WebScraperModule then sorts them.
def updateJobs(scraper, logger):
    #load JobData
    newJobData = scraper.getJobData()
    seenJobData = logger.loadSeenJobs()

    #sort new JobData
    sortedJobData = scraper.sortOutJobsKeywords(newJobData)
    instituteJobData = scraper.sortOutJobsInstitutes(sortedJobData)

    #Get links for comparison
    seenJobLinks = []
    for job in seenJobData:
        seenJobLinks.append(job["Link"])

    instituteJobLinks = []
    for job in instituteJobData:
        instituteJobLinks.append(job["Link"])

    #
    for job in sortedJobData:
        if job["Link"] in seenJobLinks:
            job["Color"] = "grey"
        if job["Link"] in instituteJobLinks:
            job["Color"] = "green"

    logger.saveSeenJobs(sortedJobData)
    logger.logDate()

    return sortedJobData

#arranges jobs so your most desired jobs are shown up top
def arrangeJobs(jobs):
    greenJobs = []
    blackJobs = []
    greyJobs = []

    for job in jobs:
        if job["Color"] == "green":
            greenJobs.append(job)
        elif job["Color"] == "black":
            blackJobs.append(job)
        elif job["Color"] == "grey":
            greyJobs.append(job)

    jobs = greenJobs + blackJobs + greyJobs
    return jobs
    

if __name__ == "__main__":

    #start scraper
    scraper = Scraper()

    #get jobs
    currentJobs = updateJobs(scraper, logger)
    currentJobs = arrangeJobs(currentJobs)

    #pass jobs to application
    app = ApplicationWindow()
    app.updateData(currentJobs)
    app.run()







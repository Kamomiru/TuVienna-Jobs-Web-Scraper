#Webscraper imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


URL = "https://jobs.tuwien.ac.at/Jobs"

#Any jobs short description that has one of these words in it will be excluded from your found jobs
EXCEMPTION_KEYWORDS = ["Doc",
                       "Lehrling",
                       "prof",
                       "fachkraft",
                       "manager",
                       "spezial"]


#Add any institutes here where you'd like to work at. they will be highlighted in the application
#Probably better to use keywords here too! since most jobs are posted in mix of german and english
INSTITUTES = ["Energietechnik und Thermodynamik",
              "Konstruktionswissenschaften und Produktentwicklung",
              "Werkstoffwissenschaft und Werkstofftechnologie",
              "Fertigungstechnik und Photonische Technologien",
              "Fahrzeugantriebe und Automobiltechnik",
              "Leichtbau und Struktur-Biomechanik",
              "Strömungsmechanik und Wärmeübertragung",
              "Mechanik und Mechatronik",
              "Managementwissenschaften"]

class Scraper:
    def __init__(self):
        self.driver = None

        #Set Selenium browser options
        options = Options()
        options.add_argument("--headless")  # run without opening browser

        # Start browser
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
            )

        # Open website
        driver.get(URL)

        print("Started selenium web scraper. Connecting to:", URL)

        self.driver = driver

    def getJobData(self):

        jobData = []

        # Find elements
        jobTitles = self.driver.find_elements(By.CLASS_NAME, "job-title")
        jobLocations = self.driver.find_elements(By.CLASS_NAME, "location")
        #first found element with class name "location" is a header so it has to be removed
        jobLocations.pop(0)

        for job, location in zip(jobTitles, jobLocations):
            #find only the link element in <div>
            linkElement = job.find_element(By.TAG_NAME, "a")

            #extract data
            jobTitle = linkElement.get_attribute("textContent").strip()
            jobLink = linkElement.get_attribute("href")
            jobLocation = location.get_attribute("textContent").strip()

            #save data
            jobData.append({"Title":jobTitle, "Location":jobLocation, "Link":jobLink, "Color":"black"}) #Color entry is for keeping track of job status (new/seen/...)

        print("Fetched website data with", len(jobData), "entries")
        return jobData

    def sortOutJobsKeywords(self, jobData):

        sortedJobData = []

        for job in jobData:
            if any(keyword.lower() in job["Title"].lower() for keyword in EXCEMPTION_KEYWORDS): #checks if any of the keywords is in jobtitle
                continue

            sortedJobData.append(job)
    
        print("Sorted out", len(jobData) - len(sortedJobData), "Jobs due to excemption keywords")
    
        return sortedJobData

    def sortOutJobsInstitutes(self, jobData):

        sortedJobData = []
        
        for job in jobData:
            if any(institute.lower() in job["Location"].lower() for institute in INSTITUTES):
                sortedJobData.append(job)

        print(len(jobData) - len(sortedJobData), "Jobs dont fit any given institute")
        if len(sortedJobData) == 0:
            print("NO JOB IN GIVEN INSTITUTES!")
        
        return sortedJobData

    def printData(self, jobData):
        print()
        print("-------------- FOUND", len(jobData), "JOBS --------------")
        for job in jobData:
            print(job["Title"], "          ", job["Location"])
        print()

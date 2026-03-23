TuWienJobsWebScraper

A simple Python scraper for job postings from the TU Wien website.
It allows filtering jobs by keywords, highlighting preferred institutes, and optionally running automatically on Windows startup.

⚠️ Disclaimer
This project is for educational purposes only.
Make sure you respect the Terms of Service of the website you scrape.
The author is not responsible for misuse.

Features
Scrapes job postings from the TU Wien jobs website
Filter jobs using exclusion keywords
Highlight jobs from preferred institutes
Previously seen jobs are shown in grey
Optional Windows autostart notification setup

You can configure filters in:

WebScraperModule.py

EXCLUSION_KEYWORDS

Jobs containing any of these keywords will not be shown.

INSTITUTES

If a job description contains one of these names, it will be highlighted.

Example:

EXCLUSION_KEYWORDS = ["Doc", "Prof"]

INSTITUTES = [
"Institut für Energietechnik und Thermodynamik",
"Institut für Mechanik und Mechatronik"
]

Installation
Install Python (3.10+ recommended)
Clone the repository

git clone https://github.com/Kamomiru/TuVienna-Jobs-Web-Scraper.git

Go into the project folder

cd TuWienJobsWebScraper

Run the scraper

python TuWienJobsWebScraper.py

Run automatically on Windows startup

You can configure the scraper to run when Windows starts.

1. Customize Batch File

@echo off
REM Insert path where you have python installed below
cd "C:\PYTHON PATH"
REM Insert path where you saved TuWienJobsWebScraper.py
python "C:\SCRAPER PATH\TuWienJobsWebScraper.py"

2. Open startup folder

Press Win + R and enter:

shell:startup

3. Copy the batch file

Copy autostart.bat into the startup folder.

4. Enable in Task Manager

Open Task Manager → Startup
Enable the batch file if it is disabled.

Now the scraper will run every time you start your PC.

Notes
Only scrape publicly available data
Do not overload the website with requests
Use responsibly




import requests
from datetime import datetime
import configparser
import os


class Scraper:
    def __init__(self, url):
        self.currentTime = datetime.now().strftime("%m-%d-%y %H-%M-%S")  # gets current time to name file
        self.url = url
        self.lines = ""  # initializing to empty string temporarily

    def getText(self):
        self.lines = requests.get(self.url).text  # scrapes the text from the raw url link and assigns it to lines

    def filterText(self):
        for index in range(100):
            if self.lines[0][0] == '#':
                self.lines.pop(0)
                # checks if the first item of the list has a #, then pops it from list if true to remove comments
            else:
                break  # breaks upon reaching first IP
            self.lines = [line + '\n' for line in self.lines.split('\n') if line]
            # splits the file into individual lines, then adds back the \n delimiter to preserve formatting
            # uses list comprehension

    def createFile(self):
        filename = f"IPList {self.currentTime}.txt"  # creates a dynamic filename using time
        with open(filename, "w+") as output:
            output.write(''.join(self.lines))  # converts the array to string so it can be written to file


def getUrl(path):  # grabs the URL from the config file
    config = configparser.ConfigParser()
    config.read(path)
    return config.get('Main', 'url')


configPath = os.path.join(os.getcwd(), 'config.init')

if os.path.exists(configPath):  # checks if config file exists and sets a default url if not
    scrape = Scraper(getUrl(configPath))
else:
    scrape = Scraper("https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset")

    
scrape.getText()
scrape.filterText()
scrape.createFile()

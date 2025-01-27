from os import link
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common import service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import pandas as pd



wantFree = input("Want free? Y/N ")
whatWant = input("What you want? ")
browser = webdriver.Firefox()

if wantFree == "Y":
    
        browser.get('https://losangeles.craigslist.org/search/sfv/zip?')
        
        searchForm = browser.find_element_by_id("query")
        searchForm.click()
        
        searchForm.send_keys(whatWant)
        sendClick = browser.find_element_by_class_name("searchbtn")
        sendClick.click()

        

else:
    
        browser.get('https://losangeles.craigslist.org/search/sfv/sss?')

        searchForm = browser.find_element_by_id("query")
        searchForm.click()
        
        searchForm.send_keys(whatWant)
        sendClick = browser.find_element_by_class_name("searchbtn")
        sendClick.click()

        ulSelector = browser.find_element_by_class_name("rows")
        liClass = ulSelector.find_elements_by_tag_name("li")
        with open('craigsheet.csv', 'w', newline='') as file:
                for links in liClass:
                        linkyLinks = [links.find_element_by_xpath('./a').get_attribute('href')]
                        print(linkyLinks)
                        
                        mywriter = csv.writer(file, delimiter=' ')
                        mywriter.writerows(linkyLinks)
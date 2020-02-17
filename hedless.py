# import libraries
from selenium import webdriver
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from multiprocessing import Process
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time, os, requests, ssl, socket
import pandas as pd
# specify the url
urlpage = 'https://cat.fidelity.se'
print(urlpage)
binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options = Options()
options.headless = True
options.binary = binary
cap = DesiredCapabilities().FIREFOX.copy()
cap["marionette"] = True #optional
driver = webdriver.PhantomJS(executable_path="C:\\Work\\broken_links\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get(urlpage)

time.sleep(30)

results = driver.find_elements_by_xpath("//*[@id='header-region']/div/div/div/a")
res1 = driver.find_elements_by_tag_name('a')
print('Number of results', len(results))
print('Number of results', len(res1))
def get_all_links(driver):
    links =[]
    elements = driver.find_elements_by_tag_name('a')
    for ele in elements:
        href = ele.get_attribute('href')
        links.append(href)
    return links
list_of_links = get_all_links(driver)
for link in list_of_links:
    print(link)
def get_broken_links(a):
    broken_links = []
    for link in a:
        try:
            resp = requests.get(link)
            statuscode = resp.status_code
            if statuscode != 200:
                broken_links.append(link)
        except Exception as e:
            broken_links.append(link)
    if len(broken_links) == 0:
        return 'No Broken Links'
    else:
        return broken_links

print('Looking for Broken Links... This will take some time...')
print(get_broken_links(list_of_links))


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
options.binary = binary
# options.add_argument('-headless')
cap = DesiredCapabilities().FIREFOX.copy()
cap["marionette"] = True #optional
driver = webdriver.Firefox(options=options, capabilities=cap, executable_path="C:\\Work\\broken_links\\geckodriver-master\\geckodriver.exe")


time.sleep(30)

results = driver.find_elements_by_xpath("//*[@id='header-region']/div/div/div/a")
res1 = driver.find_elements_by_tag_name('a')
print('Number of results', len(results))
print('Number of results', len(res1))
links = []


def get_links(url):
    global links
    global driver
    driver.get(url)
    time.sleep(30)
    elements = driver.find_elements_by_tag_name('a')
    for ele in elements:
        href = ele.get_attribute('href')
        links.append(href)
        print('appended to links[]', href)
    return links


print((get_links(urlpage)))
#
# def get_all_links(url):
#     global driver
#     for ele in get_links(url):
#         get_all_links(ele)
#
#
# def get_broken_links(a):
#     broken_links = []
#     for link in a:
#         try:
#             resp = requests.get(link)
#             statuscode = resp.status_code
#             if statuscode != 200:
#                 broken_links.append(link)
#                 links = set(links)
#         except Exception as e:
#             broken_links.append(link)
#             links = set(links)
#     if len(broken_links) == 0:
#         return 'No Broken Links'
#     else:
#         return broken_links
#
# get_all_links(urlpage)
#
# for link in links:
#     print(link)
# #
# # print('Looking for Broken Links... This will take some time...')
# # print(get_broken_links(links))
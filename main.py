from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def passencrypt():
    new = ''
    word = ';=<;=>4[Vok|x'
    for i in range(len(word)):
        new = new + chr( ord(word[i]) - 10 )
    return new

nusnet = 'vimuthmendis@gmail.com'
password = passencrypt()

#from selenium.webdriver.chrome.options import Options
#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(executable_path=r'C:/Users/vimut/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(10)

driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(nusnet)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button").click()

time.sleep(10)

driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a").click()

time.sleep(10)

driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
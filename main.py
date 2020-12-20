from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = 'vimuthmendis@gmail.com'
password = passencrypt()

#from selenium.webdriver.chrome.options import Options
#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(executable_path=r'C:/Users/vimut/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(10)

driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(user)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button").click()

time.sleep(10)

# home
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a").click()

time.sleep(10)

# notifications
driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()

time.sleep(10)

# open profile
driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a").click()

time.sleep(10)

# open story
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/div/div/span").click()

time.sleep(4)

# pause story
driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/header/div[2]/div[2]/button[1]").click()

time.sleep(10)

# open viewer list
driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/div[3]/div[2]/button").click()

time.sleep(10)

# extract
details = driver.find_elements_by_xpath("/html/body/div[5]/div/div/div/div[2]")

print(details[0].text)
data = details[0].text.split('\n')

print(data)

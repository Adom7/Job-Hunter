from json import load
from lib2to3.pgen2 import driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv
from selenium.webdriver import ChromeOptions, Chrome
opts = ChromeOptions()
opts.add_experimental_option("detach", True)


load_dotenv()

Indeed_Email = os.getenv('INDEED_EMAIL')
Indeed_Password = os.getenv('INDEED_PASSWORD')


driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)

driver.get('https://fr.indeed.com/emplois?q=developpeur%20node&l=Vitry-sur-Seine%20(94)&from=searchOnHP&vjk=b1d97eb3fca2cf42&advn=2715648309700515&from=smart-apply')
time.sleep(1)
Connexion_button = driver.find_element_by_class_name('gnav-header-o4sfaq')
Connexion_button.click()
Email_Input = driver.find_element_by_id('ifl-InputFormField-3')
Email_Input.send_keys(Indeed_Email)
Email_Input.send_keys(Keys.ENTER)
time.sleep(1)
Log_With_Password = driver.find_element_by_id(
    'auth-page-google-password-fallback')
Log_With_Password.click()
time.sleep(1)
Password_Input = driver.find_element_by_id('ifl-InputFormField-111')
time.sleep(1)
Password_Input.send_keys(Indeed_Password)
Password_Input.send_keys(Keys.ENTER)
time.sleep(1)

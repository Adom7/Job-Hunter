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
Connexion_button = driver.find_element_by_class_name('gnav-header-o4sfaq')
Connexion_button.click()
time.sleep(3)
Email_Input = driver.find_element_by_id('ifl-InputFormField-3')
Email_Input.send_keys(Indeed_Email)
time.sleep(2)
Email_Input.send_keys(Keys.ENTER)
'''
Tring to avoid the ReCaptcha control
Does'nt seem to be based on time of inputs . Maybe on time between tries ?
'''
time.sleep(2)
Log_With_Password = driver.find_element_by_id(
    'auth-page-google-password-fallback')
Log_With_Password.click()
time.sleep(1)
Password_Input = driver.find_element_by_id('ifl-InputFormField-111')
time.sleep(1)
Password_Input.send_keys(Indeed_Password)
time.sleep(1)
Password_Input.send_keys(Keys.ENTER)
time.sleep(60)
# Can't find a way to resolve the captcha or avoid it , so it's the time to reply to the captcha Myself before letting the bot take control
# ANCHOR
# I Should try to connect via google ?
Close_Pop_Up = driver.find_element_by_class_name('popover-x-button-close')
Close_Pop_Up.click()
time.sleep(1)


All_Jobs = driver.find_elements_by_class_name('job_seen_beacon')
print(len(All_Jobs))

'''
🇫🇷
Sur indeed Il y a 2 grand types de candidatures
    Les Candidatures à remplir Sur un site externe -- Que nous ne couverons pas (Peux - être dans une futur MAJ)
    Les Candidatures à remplir sur Indeed -- 

🇬🇧
On Indeed 2 major types of job propositions 
    The One that send us to another website -- We Will not cover this jobs
    The One that continues on Indeed --
'''

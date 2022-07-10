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

LinkedIn_EmailAddress = os.getenv("LINKEDIN_EMAIL")
LinkedIn_Password = os.getenv("LINKEDIN_PASSWORD")
Lettre_Motivation = os.getenv("LETTRE_MOTIVATION")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)


driver.get('https://www.welcometothejungle.com/fr/jobs?page=1&groupBy=job&sortBy=mostRelevant&query=Developpeur%20Web&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Alternance&aroundQuery=Paris%2C%20France&aroundLatLng=48.85718%2C2.34141&aroundRadius=20000&range%5Bexperience_level_minimum%5D%5Bmin%5D=0&range%5Bexperience_level_minimum%5D%5Bmax%5D=2')

time.sleep(3)
connect_button = driver.find_element_by_css_selector('button.sc-cvZCdy')
connect_button.click()
time.sleep(1)
ConnectViaLinkedIn_Button = driver.find_element_by_css_selector(
    'button.sc-cvZCdy.fqfbCq.rhd9lh-0.jGucRY')
ConnectViaLinkedIn_Button.click()
time.sleep(1)
username_input = driver.find_element(by='id', value='username')
username_input.send_keys(LinkedIn_EmailAddress)
password_input = driver.find_element(by='id', value='password')
password_input.send_keys(LinkedIn_Password)
password_input.send_keys(Keys.ENTER)

# Connection is etablished . we now need to see how to pin point the jobs that we want to apply for and the ones we don't want to apply for !

time.sleep(2)
all_jobs = driver.find_elements_by_css_selector(
    'article.nwf9oq-12.sc-7dlxn3-8.glQjTu.PtGBR')

for jobs in all_jobs:
    time.sleep(3)
    jobs.click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 200)")
    button_postuler = driver.find_element_by_css_selector(
        'button.sc-cvZCdy.iicxHA')
    button_postuler.click()
    time.sleep(10)
    # there is some kind of issue , i have to click twice for the pop up to open don't think to much about it :p
    Lettre_motivation_input = driver.find_element_by_css_selector(
        'textarea.sc-ewSTlh.hENcrI')
    Lettre_motivation_input.send_keys(Lettre_Motivation)
    time.sleep(2)
    CGU_Box = driver.find_element_by_id('terms')
    CGU_Box.click()
    time.sleep(1)
    Donnees_Entreprise_Box = driver.find_element_by_id('consent')
    Donnees_Entreprise_Box.click()
    time.sleep(1)
    Submit_Candidature = driver.find_element_by_xpath(
        '/html/body/div[7]/div/div/div/form/button')
    Submit_Candidature.click()
    time.sleep(1)
    # A lot of work to do , for now only one job , needs to go to previous page , check if already applied etc etc .
    # NOTE I have to check if the post as a H3 'Déjà vu' to avoid applying multiple times to the same post

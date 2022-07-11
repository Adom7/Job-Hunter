from json import load
from lib2to3.pgen2 import driver
from tkinter.tix import PopupMenu
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

# bon Url : https://www.welcometothejungle.com/fr/jobs?page=1&groupBy=job&sortBy=mostRelevant&query=Developpeur%20Web&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Alternance&aroundQuery=Paris%2C%20France&aroundLatLng=48.85718%2C2.34141&aroundRadius=20000&range%5Bexperience_level_minimum%5D%5Bmin%5D=0&range%5Bexperience_level_minimum%5D%5Bmax%5D=2

driver.get('https://www.welcometothejungle.com/fr/jobs?groupBy=job&page=1&query=Developpeur%20Node&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Alternance&sortBy=mostRelevant&range%5Bexperience_level_minimum%5D%5Bmin%5D=0&range%5Bexperience_level_minimum%5D%5Bmax%5D=2')

# Recherche Test : https://www.welcometothejungle.com/fr/jobs?page=1&groupBy=job&sortBy=mostRelevant&query=Developpeur+Node&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Alternance

time.sleep(5)
# close the pop up , it will cause some issues
Pop_up_Button = driver.find_element_by_xpath(
    '//*[@id="axeptio_btn_dismiss"]')
Pop_up_Button.click()
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


# let's create a function to check if the bot has already seen this post (WTTJ doesn't do it for us so we have to do it !)
def check_if_DejaVu(xpath):
    try:
        driver.find_element_by_css_selector(xpath)
    except NoSuchElementException:
        return False
    return True


def check_if_WTTJ(xpath):
    # on check si la class du button postuler est bien .
    try:
        driver.find_element_by_css_selector(xpath)
    except NoSuchElementException:
        return False
    return True


time.sleep(2)
all_jobs = driver.find_elements_by_css_selector(
    'article.nwf9oq-12.sc-7dlxn3-8.glQjTu.PtGBR')
for jobs in all_jobs:
    time.sleep(3)
    check_if_DejaVu('.sc-7dlxn3-9.gdAPzy')
    if check_if_DejaVu == True:
        print('JOB Dejà vu')
    else:
        jobs.click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(3)
        if check_if_WTTJ('button.sc-cvZCdy.iicxHA') == True:
            button_postuler = driver.find_element_by_css_selector(
                'button.sc-cvZCdy.iicxHA')
            button_postuler.click()
            time.sleep(2)
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
            Return_Search = driver.find_element_by_css_selector(
                'button.sc-cvZCdy.fHkotD')
            Return_Search.click()
            time.sleep(5)
            driver.get('https://www.welcometothejungle.com/fr/jobs?groupBy=job&page=1&query=Developpeur%20Node&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Alternance&sortBy=mostRelevant&range%5Bexperience_level_minimum%5D%5Bmin%5D=0&range%5Bexperience_level_minimum%5D%5Bmax%5D=2')
            # A lot of work to do , for now only one job , needs to go to previous page , check if already applied etc etc .
            # NOTE I have to check if the post have a H3 'Déjà vu' to avoid applying multiple times to the same post
        else:
            print('Job Out of WTTJ')
            driver.get('https://www.welcometothejungle.com/fr/jobs?groupBy=job&page=1&query=Developpeur%20Node&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Alternance&sortBy=mostRelevant&range%5Bexperience_level_minimum%5D%5Bmin%5D=0&range%5Bexperience_level_minimum%5D%5Bmax%5D=2')

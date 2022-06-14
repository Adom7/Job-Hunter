from json import load
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
Phone_Number = os.getenv("PHONE_NUMBER")


driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)


driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_JT=F%2CC&f_TPR=r2592000&geoId=90009659&keywords=Developpeur%20web&location=Paris%20et%20p%C3%A9riph%C3%A9rie&sortBy=R')

# This Part is only to connect to LinkedIn and get set on the job hunting page 🤖🎯

sign_in_button = driver.find_element_by_link_text("S’identifier")
sign_in_button.click()
username_input = driver.find_element(by='id', value='username')
username_input.send_keys(LinkedIn_EmailAddress)
password_input = driver.find_element(by='id', value='password')
password_input.send_keys(LinkedIn_Password)
password_input.send_keys(Keys.ENTER)

time.sleep(1)
all_jobs = driver.find_elements_by_css_selector(
    '.job-card-container--clickable')
time.sleep(3)


"""
ANCHOR EXPLANATIONS :

🇫🇷

Sur LinkedIn il y a 3 Types de Candidature ,
    la candidature à 1 Page , Ou il faut simplement clicker sur "Envoyer la Candidature"
    La Candidature à 3 Page , ou la premiere page nous permet de rentrer nos infos perso ('Mail' , 'Nom Prenom' , 'Numero de Tel')
            La 2e Page nous permet de fournir notre CV ('Souvent pré-remplis par LinkedIN')
            la 3e page nous permet de validé les informations , de nous abonné à la page du Job et de valider la candidature en cliquant sur "Envoyer la Candidature"
    La Candidature à plus de 3 pages auquel nous ne répondrons pas dans cette version , car celle-ci demande de répondre à differente questions ('Peut-etre dans une future version :)')

🇬🇧

On LikedIn there is 3 Types of Jobs Proposition
    Job Proposition that can be filled in 1 Page , Where you only need to click on 'Submit'
    job Proposition that can be filled in 3 pages , Where the 1st Page is for your infos ,
        The 2nd Page is for you to fill you Resume in PDF ('Usually filled by LinkedIN')
        The 3rd page is to verify your infos , sub to the job linkedIn Page via a tick box and to click on 'submit'
    Job Proposition that needs more then 3 pages , we will not apply to thoses jobs ('Maybe in a future update :) ')
 """


def check_exists_CSS(xpath):
    try:
        driver.find_element_by_css_selector(xpath)
    except NoSuchElementException:
        return False
    return True


print(len(all_jobs))
for jobs in all_jobs:

    print('Job Called')
    jobs.click()
    time.sleep(1)
    try:
        apply_button = driver.find_element_by_css_selector(
            '.jobs-apply-button')
        apply_button.click()
        time.sleep(1)
        phone_input = driver.find_element_by_css_selector(
            '.fb-single-line-text__input')
        phone_input.clear()
        # we clear the phone number to avoid pre-saved phone number to mess up the input
        phone_input.send_keys(Phone_Number)
        print(check_exists_CSS('.ph5'))
        if check_exists_CSS('.ph5') == False:
            print('Check CSS False')
            check_box = driver.find_element_by_css_selector('.ember-checkbox')
            check_box.click('Uncheck')
            submit_button = driver.find_element_by_css_selector(
                '.artdeco-button--primary')
            submit_button.click()
        else:
            suivant_button = driver.find_element_by_css_selector(
                '.artdeco-button--primary')
            suivant_button.click()
            progress_bar = driver.find_element_by_css_selector(
                '.artdeco-completeness-meter-linear__progress-element')
            if progress_bar.get_attribute('value') != 50:
                close_button = driver.find_element_by_css_selector(
                    '.artdeco-button--circle')
                close_button.click()
                time.sleep(2)
                delete_button = driver.find_element_by_css_selector(
                    '.artdeco-modal__confirm-dialog-btn')
                delete_button.click()
            else:
                verify_button = driver.find_element_by_css_selector(
                    '.artdeco-button--primary')
                verify_button.click()
                check_box = driver.find_element_by_css_selector(
                    '.ember-checkbox')
                check_box.click('Uncheck')
                submit_button = driver.find_element_by_css_selector(
                    '.artdeco-button--primary')
                submit_button.click()
    except NoSuchElementException:
        print("Pas de Button candidature , passer")
    continue

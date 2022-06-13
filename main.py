from json import load
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

LinkedIn_EmailAddress = os.getenv("LINKEDIN_EMAIL")
LinkedIn_Password = os.getenv("LINKEDIN_PASSWORD")
Phone_Number = os.getenv("PHONE_NUMBER")


driver = webdriver.Chrome(ChromeDriverManager().install())


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
        phone_input.send_keys(Phone_Number)
        next_button = driver.find_element_by_css_selector('footer button')
        time.sleep(1)
        next_button.click()
        verify_button = driver.find_element_by_css_selector(
            'footer .artdeco-button--primary')
        verify_button.click()
        time.sleep(1)
        tick_box = driver.find_element_by_css_selector(
            'footer .ember-checkbox')
        tick_box.click()
        verify_button = driver.find_element_by_css_selector(
            'footer .artdeco-button--primary')
        if verify_button.get_attribute("data-control-name") == "continue unify":
            close_button = driver.find_elements_by_class_name(
                "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(1)
            discard_button = driver.find_elements_by_class_name(
                "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print('Candidature complexe , annuler')
            continue
        else:
            tick_box = driver.find_element_by_css_selector(
                'footer .ember-checkbox')
            tick_box.click()
            verify_button.click()
            time.sleep(2)
            submit_button = driver.find_element_by_class_name()
    except NoSuchElementException:
        print("Pas de Button candidature , passer")
        continue

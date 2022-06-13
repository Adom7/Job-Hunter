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


driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_JT=F%2CC&f_TPR=r2592000&geoId=90009659&keywords=Developpeur%20web&location=Paris%20et%20p%C3%A9riph%C3%A9rie&sortBy=R')


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
print(all_jobs)


time.sleep(3)

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
        phone_input.send_keys('0650550543')
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

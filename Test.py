from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.facebook.com")
print("Application title is", driver.title)

print('Hello World !')

User = input('Choose Option 1 or 2 \n')


def sfy(option):
    if option == "1":
        return print("You Chose Option 1")

    elif option == "2":
        return print('Oprion 2')

    else:
        print('Enter a correct Option')


sfy(User)

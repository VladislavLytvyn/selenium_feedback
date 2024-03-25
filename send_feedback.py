import environ
import random
import string
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service


BASE_DIR = Path(__file__).resolve().parent

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))

# Firefox
service = Service(executable_path=env.str("GECKODRIVER_PATH"))
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

# Chrome
# service = Service(executable_path='D:\\Downloads\\chromedriver_win32\\chromedriver.exe')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

# Try to add extension:
system_extension_path = env.str("EXTENSION_PATH")
# options.add_extension((system_extension_path))

url = "http://duma.gov.ru/contacts/feedback/"
# Another URL:
# url = "http://www.gks.ru/"

# Maby not needed:
# my_timeouts = Timeouts()
# my_timeouts.implicit_wait = 10
# driver.timeouts = my_timeouts

# Previous version selenium:
# river_path = "D:\\Downloads\\chromedriver_win32\\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("http://duma.gov.ru/contacts/feedback/")


send_mail = 0
while True:
    for i in range(1000):
        driver.get(url)

        text = driver.find_element(By.ID, "text")
        name = driver.find_element(By.ID, "name")
        email = driver.find_element(By.ID, "email")

        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))

        text.send_keys(generate_random_string(10))
        name.send_keys(generate_random_string(10))
        email.send_keys(generate_random_string(10) + "+@gmail.com")
        email.send_keys(Keys.RETURN)

        try:
            success_message = WebDriverWait(driver, 2).until(
                ec.presence_of_element_located((By.XPATH, "//div[contains(text(),'Сообщение отправлено!')]"))
            )
            print("Done.")
        except:
            print("Not done.")

        send_mail += 1
        print(send_mail)

    # driver.quit()

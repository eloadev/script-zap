from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class AutomationZap:

    @staticmethod
    def send_message(message, contact):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://web.whatsapp.com/")

        print("Scan QR Code, And then Enter")
        input()

        search_box = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//div[@data-testid='chat-list-search']")))
        search_box.send_keys(contact)

        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//span[@title='" + contact + "']"))).click()

        message_input_box = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//div[@data-testid='conversation-compose-box-input']")))

        for x in range(len(message)):
            message_input_box.clear()
            message_input_box.send_keys(message[x] + Keys.ENTER)

        sleep(120)
        driver.quit()

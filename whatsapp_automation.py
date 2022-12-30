from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AutomationZap:

    @staticmethod
    def send_message(message, contact):
        driver = webdriver.Chrome()
        driver.get("https://web.whatsapp.com/")

        search_box = WebDriverWait(driver, 50).until(lambda driver: driver.find_element(By.XPATH, """//*[
        @id="side"]/div[1]/div/div/div[2]/div/div[2]"""))
        search_box.send_keys(contact)

        selected_contact = driver.find_element(By.XPATH, "//span[@title='" + contact + "']")
        selected_contact.click()
        message_input_box = driver.find_element(By.XPATH, """//*[@id="main"]/footer/div[1]/div/span[2]/div/div[
        2]/div[1]/div/div[1]""")

        for x in range(len(message)):
            message_input_box.clear()
            message_input_box.send_keys(message[x] + Keys.ENTER)

        sleep(60)
        driver.close()

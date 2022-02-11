from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InstaFollower():
    def __init__(self, chrome_driver_path, insta_username, insta_password):
        self.service = Service(chrome_driver_path)
        self.insta_username = insta_username
        self.insta_password = insta_password
        self.driver = webdriver.Chrome(service=self.service)
        self.not_following = []

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        time.sleep(3)
        email_element = self.driver.find_element(By.NAME, "username")
        email_element.send_keys(self.insta_username)

        password_element = self.driver.find_element(By.NAME, "password")
        password_element.send_keys(self.insta_password)
        password_element.send_keys(Keys.ENTER)

        time.sleep(5)
        not_save_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_save_button.click()

        time.sleep(15)
        not_alert_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_alert_button.click()

    def find_followers(self, conta_insta):
        search_element = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        search_element.send_keys(conta_insta)
        time.sleep(5)
        search_element.send_keys(Keys.ENTER)
        search_element.send_keys(Keys.ENTER)
        time.sleep(5)

        followers_element = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_element.click()

        count = 0
        while count < 10:
            time.sleep(5)
            scroll_element = self.driver.find_elements(By.CSS_SELECTOR, 'div span a')
            scroll_element[0].send_keys(Keys.END)
            count += 1

        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button div')
        self.not_following = [element for element in follow_buttons if element.text == "Seguir"]
        print(f"{len(self.not_following)} profiles not followed found.")

    def follow(self, counter):
        followed = 0

        for element in self.not_following:
            element.click()
            followed += 1

            if followed >= counter:
                break
            time.sleep(3)

        print("Followed: ", followed, " accounts. ")


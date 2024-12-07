from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.config import TestData


class LoginPage:
    email_field = (By.NAME, "EMAIL_ADDRESS")
    password_field = (By.XPATH, "//input[@id='form--signin--field--PASSWORD']")
    sign_in = (By.XPATH, "//input[@value='Sign in']")
    Sign_up = "new-account-link"
    log_out = ""
    home_signin = (By.XPATH, "//a[@aria-label='Sign in']")
    welcome = (By.XPATH, "//div[@id='profile_picture-welcome-section']")
    close_up = (By.XPATH, "//button[@id='dismissBtn']")

    #TODO page action for login page

    def __init__(self, driver):
        self.driver = driver

    def get_title(self, title):
        return self.get_title(title)

    def close_popup(self):
        # self.driver.find_element(self.home_signin).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.close_up)).click()

    def homepage_signin(self):
        # self.driver.find_element(self.home_signin).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.home_signin)).click()

    def username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_field)).send_keys(username)

    def password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_signin(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sign_in)).click()

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.log_out)).click()

    def is_displayed(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.welcome)).is_displayed()
        assert element, "element not displayed"

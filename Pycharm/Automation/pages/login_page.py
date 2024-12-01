from selenium.webdriver.common.by import By

class loginPage:
    def __init__(self, driver):
        self.driver = driver
        self.input_username = (By.NAME, 'username')
        self.input_password = (By.NAME, 'password')
        self.login_button = (By.XPATH, '//button[@type="submit"]')

    def enter_username(self, username):
        self.driver.find_element(*self.input_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.input_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

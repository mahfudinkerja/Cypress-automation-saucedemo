from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(driver):
    # Navigate to Ctas Link
    driver.get("https://satu-sim.intranet.pajak.go.id/login")
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()

    # Find the username and password fields and enter the login credentials
    driver.find_element(By.NAME, "username").send_keys("evelinsarmauli.siagian")
    driver.find_element(By.NAME, "password").send_keys("Pajak123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.implicitly_wait(10)
    driver.get("https://ctas-qa.intranet.pajak.go.id/")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()

    # case management
    driver.find_element(By.XPATH, '//*[@id="4"]').click()
    driver.find_element(By.XPATH, '//a[@href="/case-management/en-US/case-creation"]').click()
    driver.implicitly_wait(10)

    # new case form
    driver.find_element(By.ID, "CaseTypeIdentifier").click()
    driver.find_element(By.XPATH, "/html/body/csm-root/div/ui-coretax-one-column-layout/div/div/div/csm-case"
                                  "-creation/div/csm-case-creation-form/form/div["
                                  "1]/div/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input").send_keys(
        'Travel Ban Request')
    driver.find_element(By.XPATH, '//li[@area-label=‘Travel Ban Request’]').click()

import pytest
from selenium import webdriver
from pages.login_page import loginPage

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    # driver.quit()


def main(browser):
    browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    login_page = loginPage(browser)
    login_page.enter_username('Admin')
    login_page.enter_password('admin123')
    login_page.click_login()

    assert "OrangeHRM" in browser.title




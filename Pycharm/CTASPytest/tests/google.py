import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
	options = webdriver.ChromeOptions()
	options.add_experimental_option( 'detach', True )
	options.add_experimental_option( 'excludeSwitches', [ 'enable-logging' ] )
	driver = webdriver.Chrome( options = options )
	driver.implicitly_wait( 30 )
	driver.maximize_window()
	yield driver
	driver.quit()


def test_login( driver ):
	driver.get( "https://www.google.com" )
	driver.find_element( By.NAME, "q" ).click()

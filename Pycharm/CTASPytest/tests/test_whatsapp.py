import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
	options = webdriver.ChromeOptions()
	options.add_experimental_option( "detach", True )
	options.add_experimental_option( "excludeSwitches", [ "enable-logging" ] )
	driver = webdriver.Chrome( options = options )
	driver.implicitly_wait( 30 )
	driver.maximize_window()
	yield driver
	# driver.quit()


def test_login( driver ):
	driver.get( "https://web.whatsapp.com/" )
	time.sleep( 20 )

	search_box = WebDriverWait( driver, 60 ).until(
		EC.element_to_be_clickable( (By.XPATH, "//p[@class='selectable-text copyable-text x15bjb6t x1n2onr6']") )
	)
	search_box.click()
	search_box.send_keys( 'Jkt Gompar' )
	time.sleep( 10 )
	for i in range(0,10):
		selected_target = driver.find_element( By.CSS_SELECTOR, "[title='Jkt Gompar']" )
		selected_target.click()

		message_box = driver.find_element( By.CSS_SELECTOR, "[spellcheck='true'] > .selectable-text" )
		message_box.click()
		message_box.send_keys( 'Testing Looping message wa')

		message_box.send_keys( Keys.ENTER )
		if i == 10:
			break

	# time.sleep( 5 )

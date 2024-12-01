import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login( browser ):
	if browser == "chrome":
		options = webdriver.ChromeOptions()
		options.add_experimental_option( "detach", True )
		options.add_experimental_option( "excludeSwitches", [ "enable-logging" ] )
		driver = webdriver.Chrome( options = options )
	elif browser == "firefox":
		options = webdriver.FirefoxOptions()
		driver = webdriver.Firefox( options = options )
	elif browser == "safari":
		driver = webdriver.Safari()

	driver.implicitly_wait( 30 )
	driver.maximize_window()

	try:
		driver.get( "https://web.whatsapp.com/" )
		time.sleep( 20 )

		search_box = WebDriverWait( driver, 60 ).until(
			EC.element_to_be_clickable( (By.XPATH, "//p[@class='selectable-text copyable-text x15bjb6t x1n2onr6']") )
		)
		search_box.click()
		search_box.send_keys( 'LG Candra' )
		time.sleep( 10 )

		selected_target = driver.find_element( By.CSS_SELECTOR, "[title='LG Candra']" )
		selected_target.click()

		message_box = driver.find_element( By.CSS_SELECTOR, "[spellcheck='true'] > .selectable-text" )
		message_box.click()
		message_box.send_keys( 'p info' )

		message_box.send_keys( Keys.ENTER )
	finally:
		driver.quit()


def run_tests_in_parallel():
	browsers = [ "chrome", "firefox", "safari" ]
	threads = [ ]

	for browser in browsers:
		thread = threading.Thread( target = test_login, args = (browser,) )
		threads.append( thread )
		thread.start()

	for thread in threads:
		thread.join()


if __name__ == "__main__":
	run_tests_in_parallel()

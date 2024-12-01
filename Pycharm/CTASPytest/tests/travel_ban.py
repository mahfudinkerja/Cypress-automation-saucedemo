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
	tax_officer_lto_username = "wawan.nurprayogi"
	supervisor_lto = "evelinsarmauli.siagian"
	password = "Pajak123"

	driver.get( "https://satu-sim.intranet.pajak.go.id/login" )

	# Handle SSL certificate error
	WebDriverWait( driver, 10 ).until(
		EC.element_to_be_clickable( (By.ID, "details-button") )
	).click()
	WebDriverWait( driver, 10 ).until(
		EC.element_to_be_clickable( (By.ID, "proceed-link") )
	).click()

	driver.find_element( By.NAME, "username" ).send_keys( supervisor_lto )
	driver.find_element( By.NAME, "password" ).send_keys( password )
	driver.find_element( By.XPATH, '//button[@type="submit"]' ).click()

	driver.get( "https://ctas-qa.intranet.pajak.go.id/" )

	# Handle SSL certificate error on new page
	WebDriverWait( driver, 10 ).until(
		EC.element_to_be_clickable( (By.ID, "details-button") )
	).click()
	WebDriverWait( driver, 10 ).until(
		EC.element_to_be_clickable( (By.ID, "proceed-link") )
	).click()

	driver.find_element( By.XPATH, '//*[@id="4"]' ).click()
	driver.find_element(
		By.XPATH, '//a[@href="/case-management/en-US/case-creation"]'
	).click()

	case_type_identifier = "Travel Ban Request"
	taxpayer = "0747779825024000"
	information_source = "Information source"

	driver.find_element( By.ID, "CaseTypeIdentifier" ).click()
	search_box = WebDriverWait( driver, 10 ).until(
		EC.element_to_be_clickable(
			(
				By.XPATH,
				"/html/body/csm-root/div/ui-coretax-one-column-layout/div/div/div/csm-case"
				"-creation/div/csm-case-creation-form/form/div["
				"1]/div/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input",
			)
		)
	)
	search_box.send_keys( case_type_identifier )
	driver.find_element( By.XPATH, f'//span[.="{case_type_identifier}"]' ).click()

	driver.find_element( By.ID, "Taxpayer" ).click()
	driver.find_element( By.ID, "ObjectPermitNumber" ).send_keys( taxpayer )
	driver.find_element( By.CSS_SELECTOR, ".p-button-label" ).click()
	driver.find_element( By.XPATH, '//*[@id="CaseInvolvement"]/div/span' ).click()
	driver.find_element( By.XPATH, f"//span[.='{information_source}']" ).click()
	driver.find_element( By.XPATH, "//button[.='Save']" ).click()

	WebDriverWait( driver, 10 ).until(
		EC.element_to_be_clickable( (By.XPATH, "//a[.='General Information']") )
	).click()

	case_number = (
		WebDriverWait( driver, 10 )
		.until(
			EC.visibility_of_element_located(
				(By.XPATH, "//h1[@class='ng-star-inserted']")
			)
		)
		.text
	)

	driver.find_element( By.XPATH, "//a[.='Routing']" ).click()
	driver.find_element( By.ID, "nextStep" ).click()

	iframe = WebDriverWait( driver, 10 ).until(
		EC.presence_of_element_located( (By.XPATH, "//iframe[@id='connector-0']") )
	)

	driver.switch_to.frame( iframe )

	officer_id = "199511252016121002"
	driver.find_element(
		By.XPATH, "(//div//table//thead//tr[2]//th[3]//input)[1]"
	).send_keys( officer_id )
	driver.find_element( By.XPATH, "//span[.='Add']" ).click()
	driver.switch_to.default_content()

	driver.find_element( By.ID, "nextStep" ).click()
	time.sleep( 10 )
	driver.find_element( By.XPATH, "//a[.='Log off']" ).click()

	driver.find_element( By.NAME, "username" ).send_keys( tax_officer_lto_username )
	driver.find_element( By.NAME, "password" ).send_keys( password )
	driver.find_element( By.XPATH, '//button[@type="submit"]' ).click()

	driver.find_element(
		By.XPATH,
		"//ul[@class='navbar-nav mr-auto scrollmenu ng-star-inserted']/li[@class='nav-item "
		"p-0 ng-star-inserted']/a[contains(.,'Case Management')]",
	).click()
	driver.find_element( By.XPATH, "//a[.='My Due Cases']" ).click()
	driver.find_element( By.CSS_SELECTOR, "#filterCaseNumber .p-inputtext" ).send_keys(
		case_number + Keys.ENTER
	)

	driver.find_element( By.ID, "SelectButton" ).click()
	# driver.find_element(By.XPATH, "//a[.='Routing']").click()

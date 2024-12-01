from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


# Fixture to set up and tear down WebDriver instance
@pytest.fixture
def driver():
    # Set up ChromeOptions
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)  # Detach WebDriver process
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Exclude logging
    driver = webdriver.Chrome(options=options)  # Create Chrome WebDriver instance with specified options
    driver.implicitly_wait(30)  # Set implicit wait time to 30 seconds
    driver.maximize_window()  # Maximize the browser window
    yield driver  # Yield the WebDriver instance to the test function
    # driver.quit()  # Teardown: Quit the WebDriver, closing the browser window and ending the session


# Test function to simulate login process
def test_login(driver):
    # assigned officer
    tax_officer_lto_username = "wawan.nurprayogi"
    supervisor_lto = "evelinsarmauli.siagian"
    password = "Pajak123"

    # Navigate to login page
    driver.get("https://satu-sim.intranet.pajak.go.id/login")

    # Click on 'details' button (assuming SSL certificate error handling)
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()

    # Enter username and password
    driver.find_element(By.NAME, "username").send_keys(supervisor_lto)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Click on login button
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Assuming redirection to another page after login
    driver.get("https://ctas-qa.intranet.pajak.go.id/")

    # Handle SSL certificate error on new page
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()

    # Access Case Management section
    driver.find_element(By.XPATH, '//*[@id="4"]').click()

    # Proceed to create a new case
    driver.find_element(By.XPATH, '//a[@href="/case-management/en-US/case-creation"]').click()

    # Form filling process for a new case
    case_type_identifier = "Travel Ban Request"
    taxpayer = "0747779825024000"
    information_source = "Information source"

    # Select case type
    driver.find_element(By.ID, "CaseTypeIdentifier").click()
    driver.find_element(By.XPATH, "/html/body/csm-root/div/ui-coretax-one-column-layout/div/div/div/csm-case"
                                  "-creation/div/csm-case-creation-form/form/div["
                                  "1]/div/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input").send_keys(
        case_type_identifier)
    driver.find_element(By.XPATH, f'//span[.="{case_type_identifier}"]').click()

    # Enter taxpayer information
    driver.find_element(By.ID, 'Taxpayer').click()
    driver.find_element(By.ID, 'ObjectPermitNumber').send_keys(taxpayer)
    driver.find_element(By.CSS_SELECTOR, '.p-button-label').click()
    driver.find_element(By.XPATH, '//*[@id="CaseInvolvement"]/div/span').click()
    driver.find_element(By.XPATH, f"//span[.='{information_source}']").click()
    driver.find_element(By.XPATH, "//button[.='Save']").click()  # Save the new case

    # Assuming redirection to another page after saving the case
    driver.find_element(By.XPATH, "//a[.='General Information']").click()

    # Get the case number for further actions
    case_number = (driver.find_element(By.XPATH, "//h1[@class='ng-star-inserted']")).text

    # Proceed to routing
    driver.find_element(By.XPATH, "//a[.='Routing']").click()
    driver.find_element(By.ID, "nextStep").click()

    # Assign an officer to the case
    iframe = driver.find_element(By.XPATH, "//iframe[@id='connector-0']")
    driver.switch_to.frame(iframe)

    officer_id = "199511252016121002"

    driver.find_element(By.XPATH, "(//div//table//thead//tr[2]//th[3]//input)[1]").send_keys(officer_id)
    driver.find_element(By.XPATH, "//span[.='Add']").click()
    driver.switch_to.default_content()

    # Proceed to the next step
    driver.find_element(By.ID, "nextStep").click()

    # Log off and login as tax officer lto
    driver.execute_script("window.open('https://ctas-qa.intranet.pajak.go.id/');")
    driver.switch_to.window(driver.window_handles[1])

    driver.find_element(By.XPATH, "//a[.='Log off']").click()

    driver.find_element(By.NAME, "username").send_keys(tax_officer_lto_username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Access Case Management and My Due Cases section
    driver.find_element(By.XPATH, "//ul[@class='navbar-nav mr-auto scrollmenu ng-star-inserted']/li[@class='nav-item "
                                  "p-0 ng-star-inserted']/a[contains(.,'Case Management')]").click()
    driver.find_element(By.XPATH, "//a[.='My Due Cases']").click()

    # Search for the previously created case
    driver.find_element(By.CSS_SELECTOR, "#filterCaseNumber .p-inputtext").send_keys(case_number + Keys.ENTER)

    # Start working on the assigned case
    driver.find_element(By.XPATH, "//tbody[@class='p-element p-datatable-tbody']/tr[2]//button["
                                  "@id='SelectButton']").click()

    # driver.find_element(By.XPATH, "//a[.='Routing']").click()

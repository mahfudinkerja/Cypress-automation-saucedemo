from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os


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
    driver.quit()  # Teardown: Quit the WebDriver, closing the browser window and ending the session


# Helper function to take a screenshot
def take_screenshot(driver, step_name):
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    driver.save_screenshot(f"{screenshot_dir}/{step_name}.png")


# Test function to simulate login process
def test_login(driver):
    # assigned officer
    tax_officer_lto_username = "wawan.nurprayogi"
    supervisor_lto = "evelinsarmauli.siagian"
    password = "Pajak123"

    # Navigate to login page
    driver.get("https://satu-sim.intranet.pajak.go.id/login")

    # Click on 'details' button (assuming SSL certificate error handling)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "details-button"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "proceed-link"))).click()

    # Enter username and password
    driver.find_element(By.NAME, "username").send_keys(supervisor_lto)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Click on login button
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Assuming redirection to another page after login
    driver.get("https://ctas-qa.intranet.pajak.go.id/")

    # Handle SSL certificate error on new page
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "details-button"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "proceed-link"))).click()

    # Access Case Management section
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="4"]'))).click()

    # Proceed to create a new case
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/case-management/en-US/case-creation"]'))).click()

    # Form filling process for a new case
    case_type_identifier = "Travel Ban Request"
    taxpayer = "0747779825024000"
    information_source = "Information source"

    # Select case type
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "CaseTypeIdentifier"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/csm-root/div/ui-coretax-one-column-layout/div/div/div/csm-case"
                                  "-creation/div/csm-case-creation-form/form/div["
                                  "1]/div/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input"))).send_keys(case_type_identifier)
    take_screenshot(driver, "case_type_identifier_selected")  # Take screenshot
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//span[.="{case_type_identifier}"]'))).click()

    # Enter taxpayer information
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'Taxpayer'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ObjectPermitNumber'))).send_keys(taxpayer)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.p-button-label'))).click()
    take_screenshot(driver, "taxpayer_information_entered")  # Take screenshot
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CaseInvolvement"]/div/span'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//span[.='{information_source}']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[.='Save']"))).click()  # Save the new case

    # Assuming redirection to another page after saving the case
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[.='General Information']"))).click()

    # Get the case number for further actions
    case_number = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='ng-star-inserted']"))).text

    # Proceed to routing
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Routing']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nextStep"))).click()
    take_screenshot(driver, "routing_step_completed")  # Take screenshot

    # Assign an officer to the case
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='connector-0']")))
    driver.switch_to.frame(iframe)

    officer_id = "199511252016121002"

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div//table//thead//tr[2]//th[3]//input)[1]"))).send_keys(officer_id)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Add']"))).click()
    take_screenshot(driver, "officer_assigned")  # Take screenshot
    driver.switch_to.default_content()

    # Proceed to the next step
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nextStep"))).click()
    #
    # Log off and login as tax officer lto
    driver.execute_script("window.open('https://ctas-qa.intranet.pajak.go.id/');")
    driver.switch_to.window(driver.window_handles[1])

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Log off']"))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(tax_officer_lto_username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
    take_screenshot(driver, "login_as_officer_lto")  # Take screenshot

    case_number_login2 = str(case_number)
    # Access Case Management and My Due Cases section
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='navbar-nav mr-auto scrollmenu ng-star-inserted']/li[@class='nav-item "
                                  "p-0 ng-star-inserted']/a[contains(.,'Case Management')]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[.='My Due Cases']"))).click()

    # Search for the previously created case
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#filterCaseNumber .p-inputtext"))).send_keys(case_number_login2 + Keys.ENTER)

    # Start working on the assigned case
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//tbody[@class='p-element p-datatable-tbody']/tr[2]//button["
                                  "@id='SelectButton']"))).click()
    take_screenshot(driver, "case_selected")  # Take screenshot

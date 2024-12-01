import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, executable_path=chrome_path)
        yield browser
        browser.close()

def test_login(browser):
    tax_officer_lto_username = "wawan.nurprayogi"
    supervisor_lto = "evelinsarmauli.siagian"
    password = "Pajak123"

    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    # Open the login page
    page.goto("https://satu-sim.intranet.pajak.go.id/login")

    # Handle SSL certificate error if it appears
    try:
        page.click("#details-button")
        page.click("#proceed-link")
    except:
        pass  # Ignore if the certificate error handling buttons are not present

    # Perform login
    page.fill('input[name="username"]', supervisor_lto)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')

    # Navigate to the second URL
    page.goto("https://ctas-qa.intranet.pajak.go.id/")

    # Handle SSL certificate error if it appears
    try:
        page.click("#details-button")
        page.click("#proceed-link")
    except:
        pass  # Ignore if the certificate error handling buttons are not present

    # Perform additional navigation and interactions
    page.click("text=General Information")
    page.click('//*[@id="4"]')
    page.click('//a[@href="/case-management/en-US/case-creation"]')

    case_type_identifier = "Travel Ban Request"
    taxpayer = "0747779825024000"
    information_source = "Information source"

    page.click('#CaseTypeIdentifier')
    search_box = page.wait_for_selector(
        "/html/body/csm-root/div/ui-coretax-one-column-layout/div/div/div/csm-case-creation/div/csm-case-creation-form/form/div[1]/div/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input"
    )
    search_box.fill(case_type_identifier)
    page.click(f'//span[.="{case_type_identifier}"]')

    page.click('#Taxpayer')
    page.fill('#ObjectPermitNumber', taxpayer)
    page.click(".p-button-label")
    page.click('//*[@id="CaseInvolvement"]/div/span')
    page.click(f"//span[.='{information_source}']")
    page.click("//button[.='Save']")

    page.click("text=General Information")

    case_number = page.wait_for_selector("//h1[@class='ng-star-inserted']").text_content()

    page.click("text=Routing")
    page.click('#nextStep')
#
#     # Handle iframe
#     iframe = page.frame(name="connector-0")
#     iframe.fill("(//div//table//thead//tr[2]//th[3]//input)[1]", "199511252016121002")
#     iframe.click("//span[.='Add']")
#
#     page.click('#nextStep')
#
#     page.click("text=Log off")
#
#     page.fill('input[name="username"]', tax_officer_lto_username)
#     page.fill('input[name="password"]', password)
#     page.click('button[type="submit"]')
#
#     page.click("text=Case Management")
#     page.click("text=My Due Cases")
#     page.fill("#filterCaseNumber .p-inputtext", case_number)
#     page.keyboard.press("Enter")
#     page.click("h1")
#     page.click("#SelectButton")
#
#     page.click("text=Add New Data")
#     page.click("text=Routing")
# #
# # # Untuk menjalankan pytest, Anda bisa menggunakan perintah berikut di terminal:
# # # pytest nama_file.py

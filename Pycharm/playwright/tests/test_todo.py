import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser():
	chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
	with sync_playwright() as p:
		browser = p.chromium.launch( headless = False, executable_path = chrome_path )
		yield browser
		# browser.close()

while True:
	def test_login( browser ):
		context = browser.new_context()
		page = context.new_page()
		page.goto( 'https://demo.playwright.dev/todomvc/#/' )
		page.locator("//input[@class='new-todo']").fill('Hallo')




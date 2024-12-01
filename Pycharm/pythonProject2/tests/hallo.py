import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.goto("chrome-error://chromewebdata/")
    page.get_by_role("button", name="Advanced").click()
    page.get_by_role("link", name="Proceed to satu-sim.intranet.").click()
    page.get_by_placeholder("Email ID").click()
    page.get_by_placeholder("Email ID").fill("admin")
    page.get_by_placeholder("Email ID").press("Tab")
    page.get_by_placeholder("Password").fill("Pajak123")
    page.get_by_placeholder("Password").press("Enter")
    page.get_by_role("button", name="Details").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.goto("https://satu-sim.intranet.pajak.go.id/login")
    page.get_by_role("button", name="Advanced…").click()
    page.get_by_role("button", name="Accept the Risk and Continue").click()
    page.get_by_placeholder("Email ID").click()
    page.get_by_placeholder("Email ID").fill("admin")
    page.get_by_placeholder("Email ID").press("Tab")
    page.get_by_placeholder("Password").fill("Pajak123")
    page.get_by_role("button", name="LOGIN").click()
    page.goto("http://localhost:8083/")
    page.goto("https://ctas-qa.intranet.pajak.go.id/")
    page.get_by_role("button", name="Advanced…").click()
    page.get_by_role("button", name="Accept the Risk and Continue").click()
    page.goto("https://ctas-qa.intranet.pajak.go.id/home/en-US/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

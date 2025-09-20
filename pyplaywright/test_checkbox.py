import time

from playwright.sync_api import Playwright, sync_playwright, expect
import re

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://selectorshub.com/xpath-practice-page/")
    page.locator("input[type='checkbox']:left-of(:text('John.Smith'))").first.click()
    time.sleep(3)
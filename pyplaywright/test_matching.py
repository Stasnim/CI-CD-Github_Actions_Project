import time

from playwright.sync_api import Playwright, sync_playwright, expect
import re

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.daraz.com.bd/")
    list_element= page.locator("a", has_text=re.compile(r"sign\s*up", re.I))
    list_element.click()
    time.sleep(3)


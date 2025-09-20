import time

from playwright.sync_api import Playwright, sync_playwright, expect
import re

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.spicejet.com/")
    time.sleep(3)
    page.fill(".css-1cwyjr8","mu")
    city_name= page.locator(".r-knv0ih").all_inner_texts()
    for city in city_name:
        print(city)
    time.sleep(5)
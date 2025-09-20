"""from playwright.sync_api import Playwright


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.globalsqa.com/free-ebooks/")
    first_tagname= page.locator(".menu-custom-main-menu-container li a >> nth=0").text_content()
    print(first_tagname)

    page.locator(".menu-custom-main-menu-container li a >> nth=0").click()"""
from playwright.sync_api import sync_playwright, Playwright
import time

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.globalsqa.com/free-ebooks/")
    first_link = page.locator(".menu-custom-main-menu-container li a").first
    print(first_link.text_content())
    first_link.click()

    # Wait 5 seconds so you can see the result before browser closes
    time.sleep(5)
    browser.close()

with sync_playwright() as playwright:
    test_run(playwright)
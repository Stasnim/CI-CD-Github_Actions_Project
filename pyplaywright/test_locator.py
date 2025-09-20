"""import time
from playwright.sync_api import Playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

  # Shadow DOM
    page.goto("https://selectorshub.com/iframe-in-shadow-dom/")
    page.frame_locator("#pact1").locator("#glaf").fill("Playright")


    # Wait 5 seconds so you can see the result before browser closes
    time.sleep(5)
    #browser.close()

#with sync_playwright() as playwright:
    #run(playwright)"""
from playwright.sync_api import sync_playwright
import time


def test_fill_shadow_dom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://selectorshub.com/iframe-in-shadow-dom/")
        page.frame_locator("#pact1").locator("#glaf").fill("Playwright")

        time.sleep(3)
        browser.close()
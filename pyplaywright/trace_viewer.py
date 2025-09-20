"""from playwright.sync_api import Page, sync_playwright, expect


def run_trace(page: Page) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.google.com/")
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.context.tracing.stop(path="trace.zip")
    page.context.close()
    page.browser.close()



with sync_playwright() as page:
    run_trace(page)"""

import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/")
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.get_by_role("button", name="Node.js").click()
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Get started").click()
    page.locator("html").click()
    page.context.tracing.stop(path="trace.zip")
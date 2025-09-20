import pytest
from playwright.sync_api import Playwright, Page


def browser_context_args(playwright):
    iphone_11 = playwright.devices['iPhone 11 Pro']
    browser = playwright.chromium.launch(headless= False)
    context= browser.new_context(
        **iphone_11,
    )
    page = context.new_page()
    page.goto("https://playwright.dev/")
    page.pause()


""""import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture(scope='session')
def browser_context_args(browser_context_args, playwright):
    iphone_11 = playwright.devices['iPhone 11 pro']
    return {
        **browser_context_args,
        **iphone_11,
    }"""
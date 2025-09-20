import time
from playwright.sync_api import Playwright


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.daraz.com.bd/")
    count_a= page.locator("//a >> visible= true").count()
    print(count_a)
    list_a= page .locator("//a >> visible= true").all_text_contents()
    for al in list_a:
        print(al)
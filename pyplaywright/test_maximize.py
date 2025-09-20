
"""from playwright.sync_api import Playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    page = context.new_page()
    page.set_viewport_size({'width':500, 'height':500})   [hard coded]
    page.goto("https://playwright.dev/python/")"""



"""import time
from playwright.sync_api import Playwright
import tkinter as tk


def test_run(playwright: Playwright) -> None:
    root = tk. Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()

    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({'width': screenwidth, 'height': screenheight})
    page.goto("https://playwright.dev/python/")
    time.sleep(5)"""


import time
from playwright.sync_api import Playwright
import tkinter as tk


def test_run(playwright: Playwright) -> None:
    root = tk. Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()

    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(
        viewport={'width': screenwidth, 'height': screenheight}
    )
    page = context.new_page()
    page.goto("https://playwright.dev/python/")
    time.sleep(5)
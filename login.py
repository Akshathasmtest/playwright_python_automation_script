from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://qa-dev.apiwiz.io", wait_until="domcontentloaded", timeout=60000)  # 60s

   

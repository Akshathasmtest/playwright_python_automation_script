from playwright.sync_api import sync_playwright

# Start Playwright manually
p = sync_playwright().start()

# Launch Chrome
browser = p.chromium.launch(channel="chrome", headless=False)
page = browser.new_page()

# Navigate to Google
page.goto("https://qa-dev.apiwiz.io/api-design/oas", timeout=60000)

# Keep the browser open forever
print("Browser is open. Close it manually to exit.")
while True:
    pass

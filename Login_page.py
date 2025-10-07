from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome",headless=False)
    page = browser.new_page()
    page.goto("https://qa-dev.apiwiz.io/auth", wait_until="networkidle", timeout=60000)
    page.wait_for_selector('input[placeholder="Enter Username"]', timeout=10000)


    try:
        # Check if username input is visible
        if page.locator('//input[@placeholder="Enter Username"]').is_visible():
            page.locator('//input[@placeholder="Enter Username"]').fill('AkshathaSM')
            print("Username entered.")
        else:
            print("Username input not found.")
        
        # Check if password input is visible
        if page.locator('//input[@placeholder="Enter Password"]').is_visible():
            page.locator('//input[@placeholder="Enter Password"]').fill('Aad77607945@998')
            print("Password entered.")
        else:
            print("Password input not found.")
        
        # Check if login button is visible
        login_button = page.locator('xpath=//*[@id="app-root"]/div/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/div[3]/div[2]/div/div/input')
        if login_button.is_visible():
            page.wait_for_timeout(2000)  # small wait before clicking
            login_button.click()
            print("Login button clicked.")
            
            # Optional: wait a few seconds for page to load
            page.wait_for_timeout(5000)

        else:
            print("Login button not found.")
    
    except TimeoutError:
        print("One or more elements were not found on the page.")
    
    print("Page title:", page.title())
    page.wait_for_selector('//div[@class="text-transform-uppercase flex-center cursor-pointer position-relative bg-gray-500 text-white w-24px h-24px bg-gray-500 br-50 border-stroke-section-1px fs-13px fw-500"]', timeout=10000)
    browser.close()

import openpyxl
import pytest
from playwright.sync_api import sync_playwright, Page, expect

EXCEL_FILE = "/Users/akshathasm/Desktop/Playwright_Python/Test/xlsheet.xlsx"

# ---------- Excel Reader ----------
def get_excel_data(file_path: str) -> list[tuple[str, str]]:
    """Reads username/password pairs from Excel (.xlsx) file."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        if username and password:
            data.append((username, password))
    return data


# ---------- Reusable Login Function ----------
def stage_login(page: Page, username: str, password: str):
    """Performs login and returns True if successful."""
    page.goto("https://qa-dev.apiwiz.io/auth", wait_until="networkidle", timeout=60000)
    page.locator('//input[@placeholder="Enter Username"]').fill(username)
    page.locator('//input[@placeholder="Enter Password"]').fill(password)

    login_button = page.locator('//div[contains(@class,"bg-blue-800") and contains(@class,"cursor-pointer")]')
    login_button.click()

    expect(page.get_by_text("qa-dev")).to_be_visible(timeout=15000)
    print(f"✅ Login successful for user: {username}")
    return True


# ---------- Custom fixture to maximize browser ----------
@pytest.fixture(scope="session")
def maximized_page() -> Page:
    """Launch browser maximized and return a Page object."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--start-maximized"]
        )
        context = browser.new_context(viewport=None)  # viewport=None ensures full window size
        page = context.new_page()
        
        # Optional JS maximize if OS ignores args
        page.evaluate("window.moveTo(0,0); window.resizeTo(screen.width, screen.height);")
        
        yield page
        
        context.close()
        browser.close()


# ---------- Parametrized Pytest using maximized browser ----------
@pytest.mark.parametrize("username,password", get_excel_data(EXCEL_FILE))
def test_login_flow(maximized_page: Page, username: str, password: str):
    """Login test that reads credentials from Excel using a maximized browser."""
    page = maximized_page
    assert stage_login(page, username, password)

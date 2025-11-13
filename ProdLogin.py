import openpyxl
import pytest
from playwright.sync_api import Page, expect


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


EXCEL_FILE = "/Users/akshathasm/Desktop/Playwright_Python/Test/ProdLogin.xlsx"

# EXCEL_FILE= "/Users/akshathasm/Desktop/Playwright_Python/Test/xlsheet1.xlsx"
# ---------- Reusable Login Function ----------
def Prodlogin(page: Page, username: str, password: str):
    """Performs login and returns True if successful."""
    page.evaluate("window.moveTo(0,0); window.resizeTo(screen.width, screen.height);")
    page.goto("https://acme-team-production.apiwiz.io/", wait_until="networkidle", timeout=60000)
    page.set_viewport_size({"width": 1600, "height": 900})
    page.locator('//input[@placeholder="Enter Username"]').fill(username)
    page.locator('//input[@placeholder="Enter Password"]').fill(password)

    login_button = page.locator('//div[contains(@class,"bg-blue-800") and contains(@class,"cursor-pointer")]')
    login_button.click()

    expect(page.get_by_text("acme-team-production")).to_be_visible(timeout=15000)
    print(f"✅ Login successful for user: {username}")
    return True



# ---------- Parametrized Pytest ----------
@pytest.mark.parametrize("username,password", get_excel_data(EXCEL_FILE))
def test_login_flow(page: Page, username: str, password: str) -> None:
    """Login test that reads credentials from Excel."""
    assert Prodlogin(page, username, password)

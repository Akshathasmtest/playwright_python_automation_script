import re
from playwright.sync_api import Page, expect
import pytest
import openpyxl

def get_excel_data(file_path: str) -> list[tuple[str, str]]:
    """Reads username/password pairs from Excel (.xlsx) file."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []

    # Skip header row if present
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        if username and password:
            data.append((username, password))
    return data
# def get_csv_data() -> list:
#     import csv
#     data=[]
#     with open("/Users/akshathasm/Desktop/Playwright_Python/Test/xldata.csv", newline='')as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             data.append(row)
#     return data

# @pytest.mark.parametrize("username,password", get_csv_data())
# def test_login_flow(page: Page,username,password) -> None:

#     page.goto("https://qa-dev.apiwiz.io/auth")
#     page.get_by_role("textbox", name="Enter Username").click()
#     page.get_by_role("textbox", name="Enter Username").press("CapsLock")
#     page.get_by_role("textbox", name="Enter Username").fill(username)
#     page.get_by_role("textbox", name="Enter Password").click()
#     page.get_by_role("textbox", name="Enter Password").fill(password)
#     page.locator("div").filter(has_text=re.compile(r"^Log in$")).click()
#     expect(page.get_by_text("qa-dev")).to_be_visible()

EXCEL_FILE = "/Users/akshathasm/Desktop/Playwright_Python/Test/xlsheet.xlsx"

@pytest.mark.parametrize("username,password", get_excel_data(EXCEL_FILE))
def test_login_flow(page: Page, username: str, password: str):
    page.goto("https://qa-dev.apiwiz.io/auth")

    page.get_by_role("textbox", name="Enter Username").fill(username)
    page.get_by_role("textbox", name="Enter Password").fill(password)
    page.locator("div").filter(has_text=re.compile(r"^Log in$")).click()

    # page.wait_for_load_state("networkidle")
    # expect(page.get_by_text(re.compile("qa-dev", re.I))).to_be_visible()

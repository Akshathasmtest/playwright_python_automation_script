import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://qa-dev.apiwiz.io/auth")
    page.get_by_role("textbox", name="Enter Username").click()
    page.get_by_role("textbox", name="Enter Username").press("CapsLock")
    page.get_by_role("textbox", name="Enter Username").fill("Akshatha")
    page.get_by_role("textbox", name="Enter Username").press("CapsLock")
    page.get_by_role("textbox", name="Enter Username").fill("AkshathaSM")
    page.get_by_role("textbox", name="Enter Password").click()
    page.get_by_role("textbox", name="Enter Password").press("CapsLock")
    page.get_by_role("textbox", name="Enter Password").fill("Aad77607945@99")
    page.locator(".eyeIcon > .color-text-subdued").click()
    page.get_by_role("textbox", name="Enter Password").click()
    page.get_by_role("textbox", name="Enter Password").click()
    page.get_by_role("textbox", name="Enter Password").click()
    page.get_by_role("textbox", name="Enter Password").fill("Aad77607945@19899")
    page.locator("div").filter(has_text=re.compile(r"^Log in$")).click()
    expect(page.get_by_text("qa-dev")).to_be_visible()
    page.get_by_text("API Monetization").click()
    page.locator("div").filter(has_text=re.compile(r"^Total Packages20$")).first.click()
    page.locator("div").filter(has_text=re.compile(r"^Add Package$")).nth(1).click()
    page.get_by_role("textbox", name="Enter package name...").click()

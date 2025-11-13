from playwright.sync_api import sync_playwright
from StageLogin import stage_login, get_excel_data, EXCEL_FILE
from playwright.sync_api import Page , expect
import random


    
def run_api_design_flow(page: Page):
# Now `page` is already logged in
    
    # --------- NAVIGATE TO API DESIGN PAGE ---------
    OAS_AddButton = page.goto("https://qa-dev.apiwiz.io/api-design/oas/new", wait_until="networkidle", timeout=60000)
   
    page.wait_for_timeout(2000)
    StartBlank=page.locator('//div[@class="bg-surface-l1 hover-parent fade-in-0 position-relative hover-bg-surface-underground h-144px p-24px w-234px border-stroke-subsection-1px br-8px hover-surface-underground cursor-pointer flex-col gap-8px"]')
    StartBlank.click()
    page.wait_for_timeout(2000)
    Swagger_name = page.locator('//input[@class="undefined  false hasBg null null w-100 formInputTag" and @placeholder="Enter swagger name"]').fill('Swagger_1')
    page.wait_for_timeout(2000)
    Swagger_version=page.locator('//input[@class="undefined  false hasBg null null w-100 formInputTag" and @placeholder="Enter swagger version"]').fill('1.0.0')
    page.wait_for_timeout(2000)
    Swagger_serviceUrl= page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter Terms of Services URL"]').fill('http://url.io')
    page.wait_for_timeout(2000)
    Swagger_Description=page.locator('//textarea[@class="formInputTag w-100 false undefined hasBg null"]').fill('This Swagger definition provides a comprehensive specification of the API endpoints, request/response formats, authentication mechanisms, and error handling for the application. The purpose of this API is to enable developers to programmatically interact with the backend services in a standardized, consistent, and secure manner.')
    page.wait_for_timeout(2000)
    Environment_DropDown=page.locator('//div[@class="css-1xc3v61-indicatorContainer"]').click()
    page.wait_for_timeout(2000)
    Environment_details=page.locator('//div[text()="builder - 1 Domain"]').wait_for(state="visible", timeout=20000)
    Environment_details.click()
    page.wait_for_timeout(2000)
    LicenceName=page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter license name"]').fill('Apache 2.0')
    page.wait_for_timeout(2000)
    licenseUrl = page.locator('//input[contains(@class,"formInputTag") and @placeholder="Enter license url"]')
    licenseUrl.wait_for(state="visible", timeout=20000)
    licenseUrl.fill("https://www.apache.org")
    print("License URL entered successfully.")

  
    Licence_ContactName =page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter contact name"]').fill('APIwiz Support')
    Licence_ContactUrl=page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter contact url"]').fill('https://apiwiz.io/support')
    Lincence_ContactEmail=page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter contact email"]').fill('support@apiwiz.io')
    Licence_ExternalDocument=page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter document url"]').fill('https://apiwiz.io/docs')
    Licence_ExternalDocumentDescription=page.locator('//textarea[@class="formInputTag w-100  undefined hasBg null" and @placeholder="Enter documentation description"]').fill('Full API Documentation')
    
    proceed = page.locator('//div[@class="ripple-btn"]/preceding-sibling::p[@class="color-text-regular fs-13px text-white fs-12px"]')
    proceed.evaluate("el => el.click()")

    #Paths 
    paths = page.locator('//p[@class="color-text-subdued fs-12px fw-600" and text()="Paths"]/ancestor::div[@class="h-36px flex-row vt-center hz-space-between px-12px py-4px border-bottom-stroke-subsection-1px gap-6px"]/descendant::div[@class="ripple-btn"][2]')
    paths.wait_for(state="visible", timeout=30000)
    paths.click()
    
    page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag"]').fill('/operation')
    
    page.locator('//p[@class="color-text-subdued fs-12px fw-600" and text()="Paths"]/ancestor::div[@class="h-100 w-100 flex-col gap-8px"]/descendant::div[@class="w-100 px-8px flex-row vt-center hz-space-between h-36px gap-4px"]/descendant::div[@class="ripple-btn"][2]').click()
    
     # Hover over the element
    target = page.locator('//div[@class="ripple-btn"]/ancestor::div[@class="w-100"]/descendant::div[@class="w-100 flex-col"]/descendant::div[@class="w-100 overflow-scroll noscrollbar px-8px"]/descendant::div[@class="ripple-btn"]')
    target.wait_for(state="visible", timeout=30000)  # wait until visible
    target.hover()   # perform mouse hover
    print("✅ Hover successful")

    # Optional: click after hover
    target.click()
    print("✅ Click successful")
    
    page.locator('//div[@class="hover-bg-surface-underground cursor-pointer p-8px color-text-regular fs-13px fw-500" and text()="Add Operation"]').click()
    
    Operaton_Id= page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag"]').fill('get_operation')
    
    page.locator('//div[@class="ripple-btn"]/ancestor::div[@class="w-70px flex-row vt-center hz-space-between px-4px h-32px"]/descendant::div[@class="ripple-btn"][2]').click()
    
    page.locator('//div[@class="w-50 cursor-pointer py-4px op-0-5"]').click()
    
    # Example Component
    Example =page.locator('//p[@class="color-text-subdued fs-12px fw-600 text-transform-capitalize" and text()="Examples"]')
    Example.hover()
    print("✅ Example Hover successful")
    
    Example.click()
    print("✅ Example Clicked successful")
    
    Example_addButton = page.locator('//p[@class="color-text-regular fw-600 fs-13px" and text()="Examples"]/ancestor::div[@class="w-100 bg-surface-l2 h-36px p-8px flex-row vt-center hz-space-between border-bottom-stroke-subsection-1px"]/descendant::div[@class="ripple-btn"][1]')
    Example_addButton.click()
    
    Example_name = page.locator('//input[@class="noBorder  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter Example name"]')
    Example_name.fill('Example_1')
    
    Example_summary = page.locator('//textarea[@class="formInputTag w-100  undefined hasBg null" and @placeholder="Enter example summary"]')
    Example_summary.fill('The user (ID:101) is an active Admin with email user@example.com prefers English, has notifications enabled, skilled in Python, Playwright, and API Automation; profile retrieved successfully.')
    
    Example_Description = page.locator('//textarea[@class="formInputTag w-100  undefined hasBg null" and @placeholder="Enter example description"]')
    Example_Description.fill('This JSON object contains the details of a system user, including their unique ID, role, contact information, language preference, notification settings, and list of technical skills. It is used to manage user access, display profile information, and facilitate interactions with various modules of the application.')
    
    Example_value = page.locator('//textarea[@class="formInputTag w-100  undefined hasBg null" and @placeholder="Enter value"]')
    Example_value.fill('{ "status": "success", "data": { "user_id": 101, "name": "Akshatha SM", "email": "akshatha@example.com", "role": "Admin", "active": true, "preferences": { "language": "en", "notifications": true }, "skills": ["Python", "Playwright", "API Automation"], "created_at": "2025-10-04T09:00:00Z" }, "message": "User profile retrieved successfully." }')
    
    Example_save_button = page.locator('//p[@class="color-text-regular fs-13px text-white fw-500" and text()="Save"]')
    Example_save_button.evaluate("el => el.click()")
    page.wait_for_timeout(2000)
    expect(page.get_by_text("Example created successfully")).to_be_visible(timeout=15000)
    print("Example created successfull")
   
    # Header Component
    Header = page.locator('//p[@class="color-text-subdued fs-12px fw-600 text-transform-capitalize" and text()="Headers"]')
    Header.hover()
    print("✅ Header Hover successful")
    
    Header.click()
    print("✅ Header Clicked successful")
    
    Header_addButton = page.locator('//p[@class="color-text-regular fw-600 fs-13px" and text()="Headers"]/ancestor::div[@class="w-100 bg-surface-l2 h-36px p-8px flex-row vt-center hz-space-between border-bottom-stroke-subsection-1px"]/descendant::div[@class="ripple-btn"][1]')
    Header_addButton.click()
    
    Header_name = page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter Header name"]')
    Header_name.fill('Tenant')
    
    Header_description = page.locator('//textarea[@class="formInputTag w-100  undefined hasBg null" and @placeholder="Enter Header description"]')
    Header_description.fill('Headers required for authenticating and formatting API requests')
    
    Header_Schema_ToggleButton = page.locator('//span[@class="switch-slider"]')
    Header_Schema_ToggleButton.click()
    
    Header_SaveButton = page.locator('//p[@class="color-text-regular fs-13px text-white fw-500" and text()="Save"]')
    Header_SaveButton.evaluate("el => el.click()")
    
    # Links Component
    # Link = page.locator('//p[@class="color-text-subdued fs-12px fw-600 text-transform-capitalize" and text()="Links"]')
    # Link.hover()
    # print("✅ Link Hover successful")
    
    # Link.click()
    # print("✅ Link Clicked successful")
    
    # Link_AddButton = page.locator('//p[@class="color-text-regular fw-600 fs-13px" and text()="Links"]/ancestor::div[@class="w-100 bg-surface-l2 h-36px p-8px flex-row vt-center hz-space-between border-bottom-stroke-subsection-1px"]/descendant::div[@class="ripple-btn"]')
    # Link_AddButton.click()
    # page.wait_for_timeout(2000)
    
    # Link_Name = page.locator('//input[@class="noBorder  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter link name"]')
    # Link_Name.fill('#Link')
    # page.wait_for_timeout(2000)
    
    # Link_Description = page.locator('//textarea[@class="formInputTag w-100  undefined hasBg null" and @placeholder="Enter link description"]')
    # Link_Description.fill('Retrieve orders for the user')
    # page.wait_for_timeout(2000)
    
    # Link_OperationID = page.locator('//p[@class="fs-13px fw-700 color-text-regular" and text()="Operation Type"]/ancestor::div[@class="flex-col gap-4px w-100"]/descendant::div[@class="form__input false flex-row w-100 text-left flex-center br-5px undefined"]')
    # Link_OperationID.evaluate("el=>.el.click()")
    # Link_OperationID.fill('s').press("Enter")
    # page.wait_for_timeout(2000)
    
    # Link_RequestBody = page.locator('//input[@class="noBorder  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter Request Body"]')
    # Link_RequestBody.fill('{ "message": "Check out this link for more info!", "links": [ { "title": "OpenAI Website", "url": "https://www.openai.com", "description": "Official website of OpenAI for AI research and products." }, { "title": "API Documentation", "url": "https://api.example.com/docs", "description": "Full documentation of the Example API." } ], "recipient": { "user_id": "12345", "channel_id": "general" }, "priority": "high" }')
    # page.wait_for_timeout(2000)
    
    # Link_SaveButton = page.locator('//p[@class="color-text-regular fs-13px text-white fw-500" and text()="Save"]')
    # Link_SaveButton.click()
    # page.wait_for_timeout(2000)
    
    # Parameter Component
    Parameter = page.locator('//p[@class="color-text-subdued fs-12px fw-600 text-transform-capitalize" and text()="Parameters"]')
    Parameter .hover()
    print("✅ Parameter Hover successful")
    
    Parameter.click()
    print("✅ Parameter Clicked successful")
    
    Parameter_AddButton= page.locator('//p[@class="color-text-regular fw-600 fs-13px" and text()="Parameters"]/ancestor::div[@class="w-100 bg-surface-l2 h-36px p-8px flex-row vt-center hz-space-between border-bottom-stroke-subsection-1px"]/descendant::div[@class="ripple-btn"][1]')
    Parameter_AddButton.evaluate("el => el.click()")
    print("✅ Parameter AddButton Clicked successful")
    
    page.wait_for_timeout(2000)
    
    Parameter_Name = page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter Parameter name"]')
    Parameter_Name.wait_for(state="visible", timeout=20000)
    Parameter_Name.fill('userId')
    print("✅ Parameter Name filled successfully")
    
    page.wait_for_timeout(2000)
    
    Parameter_description = page.locator('//textarea[@class="formInputTag w-100  undefined hasBg null" and @placeholder="Enter Parameter description"]')
    Parameter_description.fill('ID of the user to whom the message is sent')
    
    Parameter_Location = page.locator('//label[@class="isRequired text-left text-nowrap fs-13px fw-700 color-text-regular undefined " and text()="Location"]/ancestor::div[@class="form__input border-bottom-stroke-subsection-1px flex-row w-100 text-left flex-center br-5px undefined"]/descendant::div[@class="v1select hasBg undefined w-100 undefined null css-b62m3t-container"]')
    Parameter_Location.click()
    page.wait_for_timeout(2000)
    
    Query =page.locator('//div[text()="Query"]')
    Query.click()
    page.wait_for_timeout(2000)
     
    Parameter_Schema = page.locator('//span[@class="switch-slider"]')
    Parameter_Schema.hover()
    page.wait_for_timeout(2000)
    print('✅ Schema button hover succesfully')
    Parameter_Schema.click()
    print('✅ Schema button hover succesfully')
    
    Parameter_SaveButton = page.locator('//p[@class="color-text-regular fs-13px text-white fw-500" and text()="Save"]')
    Parameter_SaveButton.evaluate("el => el.click()")
    
    # Server Component
    Server = page.locator('//p[@class="color-text-subdued fs-12px fw-600 text-transform-capitalize" and text()="Servers"]') 
    Server.hover()
    Server.click()
    
    Server_AddButton= page.locator('//p[@class="color-text-regular fw-600 fs-13px" and text()="Servers"]/ancestor::div[@class="w-100 bg-surface-l2 h-36px p-8px flex-row vt-center hz-space-between border-bottom-stroke-subsection-1px"]/descendant::div[@class="ripple-btn"][1]')
    Server_AddButton.evaluate("el => el.click()")
    
    Server_name = page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter Server name"]')
    Server_name.fill('Server_1')
    
    Server_description =page.locator('//textarea[@class="formInputTag w-100  undefined hasBg null" and @placeholder="Enter Server Description"]')
    Server_description.fill('Staging server')
    
    Server_Schema = page.locator('//input[@id="https://"]')
    Server_Schema.click()
    
    Server_Host = page.locator('//div[@class="css-1xc3v61-indicatorContainer"]')
    Server_Host.click()
    Serverdetails =page.locator('//div[text()="qa-dev-sujith.apiwiz.io"]')
    Serverdetails.click()
    
    num = random.randint(1, 100)
    
    Server_BasePath = page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag" and @placeholder="Enter Server Base Path"]')
    Server_BasePath.fill(f'/v1/sandbox/{num}')
    
    Server_SaveButton = page.locator('//p[@class="color-text-regular fs-13px text-white fw-500" and text()="Save"]')
    Server_SaveButton.evaluate("el =>el.click()")
    
    # Tags Components
    Tags =page.locator('//p[@class="color-text-subdued fs-12px fw-600 text-transform-capitalize" and text()="Tags"]')
    Tags.hover()
    Tags.click()
    
    Tags_AddButton = page.locator('//p[@class="color-text-regular fw-600 fs-13px" and text()="Tags"]/ancestor::div[@class="w-100 bg-surface-l2 h-36px p-8px flex-row vt-center hz-space-between border-bottom-stroke-subsection-1px"]/descendant::div[@class="ripple-btn"]')
    Tags_AddButton.evaluate("el =>el.click()")
    
    Tags_name=page.locator('//input[@class="undefined  isDefault hasBg null null w-100 formInputTag"]')
    Tags_name.fill('User')
    
    Tags_description =page.locator('//textarea[@class="formInputTag w-100  undefined hasBg null"]')
    Tags_description.fill('Operations related to user management')
    
    Tags_SaveButton = page.locator('//p[@class="color-text-regular fs-13px text-white fw-500" and text()="Save"]')
    Tags_SaveButton.evaluate("el =>el.click()")
    
    # Paths Section
    Paths = page.locator('//p[@class="fs-12px fw-600 color-text-regular text-center" and text()="Paths"]')
    Paths.evaluate("el =>el.click()")
    
    Get_operation=page.locator('//p[@class="text-truncate-1 w-100 fs-13px fw-500 color-text-regular" and text()="/operation"]/ancestor::div[@class="accordion__item"]/descendant::div[@class="accordion__panel"]')
    Get_operation.hover()
    Get_operation.click()
    
    # Response_LinkButton = page.locator('//p[@class="w-250px fs-15px fw-500 color-text-regular text-truncate-1" and text()="get_operation"]/ancestor::div[@class="h-fit-content hover-parent position-relative br-4px bg-surface-ground box-shadow-4 border-gray-300"]/descendant::p[@class="fs-15px fw-700 color-text-regular font-roboto"and text()="Responses"]/ancestor::div[@class="w-100 px-8px py-6px  flex-row px-8px py-6px vt-center border-bottom-stroke-subsection-1px py-4px cursor-pointer "]/descendant::div[@class="position-absolute px-2px h-20px flex-center bg-surface-ground br-tr-2px br-br-2px border-right-stroke-section-1px border-top-stroke-section-1px border-bottom-stroke-section-1px"]')
    Response_LinkButton=page.locator('//p[@class="fs-15px fw-700 color-text-regular font-roboto" and text()="Responses"]')
    Response_LinkButton.hover()
    print('Mouse hover successfully')
    Response_LinkButton.evaluate("el =>el.click()")
    
    ResponseBody_SettingsButton= page.locator('//p[@class="color-text-regular fw-600 fs-13px" and text()="Response Bodies"]/ancestor::div[@class="w-100 bg-surface-l2 p-8px flex-col border-bottom-stroke-subsection-1px"]/descendant::div[@class="ripple-btn"]')
    ResponseBody_SettingsButton.hover()
    ResponseBody_SettingsButton.evaluate("el =>el.click()")
    
    ResponseDetails_AddButton= page.locator('//p[@class="fs-14px fw-500 color-text-regular" and text()="Edit Response details"]/ancestor::div[@class="w-100 h-36px px-4px flex-row hz-space-between vt-center border-bottom-stroke-subsection-1px"]/descendant::div[@class="ripple-btn"][2]')
    ResponseDetails_AddButton.hover()
    ResponseDetails_AddButton.click()
   
    Response_dropdown=page.locator('//div[@class="border-stroke-section-1px br-2px p-8px flex-col gap-8px"]')
    Response_dropdown.hover()
    Response_dropdown.click()
    
    Select_StatusCode = page.locator('//p[@class="fs-13px fw-700 color-text-regular" and text()="Status Code"]/ancestor::div[@class="flex-col gap-4px w-100"]/descendant::div[@class="form__input false flex-row w-100 text-left flex-center br-5px undefined"]')
    Select_StatusCode.click()
    
    StatusCode =page.locator('//div[text()="200 - OK"]')
    StatusCode.click()
    
    StatusCode_Description=page.locator('//input[@class="noBorder  isDefault hasBg null null w-100 formInputTag"]')
    StatusCode_Description.fill('200 ok')
    
    # ContentType_AddButton =page.locator('//p[@class="fs-14px fw-500 color-text-regular" and text()="Content Type"]/ancestor::div[@class="flex-row vt-center hz-space-between"]/descendant::div[@class="ripple-btn"]')
    # ContentType_AddButton.click()
    
    # ContentType =page.locator('//p[@class="fs-13px fw-700 color-text-regular" and text()="Content Type"]/ancestor::div[@class="flex-col gap-4px w-100"]/descendant::div[@class="form__input border-bottom-stroke-subsection-1px flex-row w-100 text-left flex-center br-5px undefined"]')
    # ContentType.click()
    
    ResponseSaveButton=page.locator('//p[@class="color-text-regular fs-13px text-white fw-500" and text()="Save"]')
    ResponseSaveButton.evaluate("el =>el.click()")
    
    page.wait_for_timeout(2000)
    
    try:
        print("🕒 Waiting for Save button...")
        saveButton = page.locator('//div[@class="flex-row vt-center gap-6px position-absolute"]')
        saveButton.wait_for(state="visible", timeout=10000)

        saveButton.scroll_into_view_if_needed()
        saveButton.hover()
        saveButton.click()
        print("✅ Save button clicked successfully.")

    except Exception as e:
        print(f"⚠️ Click failed: {e}")
        try:
            saveButton.click(force=True)
            print("✅ Force click successful.")
        except Exception as e2:
            print(f"❌ Still failed to click Save button: {e2}")
            page.screenshot(path="save_button_error.png")
            print("📸 Screenshot saved: save_button_error.png")
    
    
    
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False, args=["--start-maximized"])
        context = browser.new_context()
        page = context.new_page()

        # ---------- Login (Excel-driven) ----------
        username, password = get_excel_data(EXCEL_FILE)[0]  # fetch first row of Excel
        stage_login(page, username, password)  # ✅ pass the credentials
        
  
        print("✅ Logged in successfully")

        # ---------- Run API Design Flow ----------
        run_api_design_flow(page)

        print("🎯 All steps executed successfully")
        context.close()
        browser.close()

if __name__ == "__main__":
    main()


 
    
    

from playwright.sync_api import sync_playwright
from StageLogin import stage_login, get_excel_data, EXCEL_FILE
from playwright.sync_api import Page , expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
import Design_studio

def sandboxpage(page: Page):
# Now `page` is already logged in
    
 SandboxModule=page.goto("https://qa-dev.apiwiz.io/api-sandbox", wait_until="networkidle", timeout=60000)
 try:
        page.wait_for_selector("text=Mock Collection")
        print("✅ Page loaded successfully — 'Mock Collection' found.")
 except PlaywrightTimeoutError:
        print("❌ Page did not load correctly — 'Mock Collection' not found.")
        
#  page.wait_for_timeout(4000) 
#  SandboxModule=page.locator('//div[@class="menuItems h-100 relative"]/descendant::div[@class="menuItem api-sandbox active"]')
#  page.wait_for_timeout(2000)
#  SandboxModule.hover()
#  page.wait_for_timeout(2000)
#  SandboxModule.evaluate("el => el.click()")
#  try:
#         page.wait_for_selector("text=Mock Collection")
#         print("✅ Page loaded successfully — 'Mock Collection' found.")
#  except PlaywrightTimeoutError:
#         print("❌ Page did not load correctly — 'Mock Collection' not found.")
    
 page.wait_for_timeout(2000)
 
 Sandbox_AddButton =page.locator('//div[@class="fs-16px fw-600 color-text-heading text-nowrap" and text()="Mock Collection"]/ancestor::div[@class="flex-row vt-center hz-space-between px-8px border-bottom-stroke-section-1px h-36px"]/descendant::div[@class="ripple-btn"][3]')
 Sandbox_AddButton.hover()
 page.wait_for_timeout(2000)
 try:
        Sandbox_AddButton.click(timeout=5000)
        print("✅ SandboxAddButton Clicked successfully.")
        page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ SandboxAddButton not clicked successfully")
 
        
 Import_from_Design_Studio= page.locator('//p[@class="text-truncate-1 fs-13px fw-500 color-text-regular" and text()="Import from Design Studio"]/ancestor::div[@class="bg-surface-l1 flex-row vt-center hz-space-between gap-6px zIndex-2 pr-8px"]/descendant::div[@class="flex-row vt-center form__radio cursor-pointer"]')
 Import_from_Design_Studio.click()
 
 page.wait_for_timeout(2000)
 Specification_DropDown= page.locator('//div[@class="css-1xc3v61-indicatorContainer"]')
 Specification_DropDown.click(force=True)
 page.wait_for_timeout(2000)
 dadasdadasads =page.locator(f'//div[text()="Swagger_1"]')
 dadasdadasads.click()
 page.wait_for_timeout(2000)
 
#  OasName=Design_studio.Swagger_name
#  print("oas---->" , OasName)
#  page.wait_for_selector(f'//div[text()="{OasName}"]', state="visible")
#  dadasdadasads =page.locator(f'//div[text()="{OasName}"]')
#  dadasdadasads.click()
#  page.wait_for_timeout(6000)
 
 Revision_DropDown =page.locator('//label[@class=" text-left text-nowrap fs-13px fw-700 color-text-regular undefined " and text()="Revision"]/ancestor::div[@class="form__input border-bottom-stroke-subsection-1px flex-row w-100 text-left flex-center br-5px undefined"]/descendant::div[@class="css-1wy0on6"]')
 Revision_DropDown.click()
 page.wait_for_timeout(2000)
 Oas_Revision=page.locator('//span[text()="Revision - 1 ( Env: builder )"]')
 Oas_Revision.click()
 page.wait_for_timeout(2000)
 
 Resource_DropDown=page.locator('//label[@class=" text-left text-nowrap fs-13px fw-700 color-text-regular undefined " and text()="Resource"]/ancestor::div[@class="form__input border-bottom-stroke-subsection-1px flex-row w-100 text-left flex-center br-5px undefined"]/descendant::div[@class="css-1wy0on6"]')
 Resource_DropDown.click()
 
 SwaggerOasResource=page.locator('//div[text()="get - /operation"]')
 SwaggerOasResource.click()
 page.wait_for_timeout(2000)
 
 Next_Button=page.locator('//p[@class="fw-500 fs-13px text-white" and text()="Next"]')
 Next_Button.evaluate("el => el.click()")
 
 page.wait_for_timeout(2000)
 
#  Create From Blank
 ServiceCallOutAddButton=page.locator('//button[@class="vertex-edge-add-button w-14px h-14px flex-center cursor-pointer p-8px"]')
 ServiceCallOutAddButton.hover()
 page.wait_for_timeout(2000)
 ServiceCallOutAddButton.click()
 page.wait_for_timeout(2000)

 RestApi=page.locator('//p[@class="color-text-regular fs-13px fw-600" and text()="REST API"]/ancestor::div[contains(@class,"position-relative overflow-hidden w-100")]')
 RestApi.hover()
 page.wait_for_timeout(2000)
 RestApi.click()
 page.wait_for_timeout(2000)

 RestApiStartFromBlank=page.locator('//div[@class="position-relative overflow-hidden cursor-pointer fs-11px fw-600 text-nowrap px-12px py-8px text-white br-4px bg-surface-blue-dark-hover"]')
 RestApiStartFromBlank.hover()
 page.wait_for_timeout(2000)
 RestApiStartFromBlank.click()
 page.wait_for_timeout(2000)
 
 ServiceCallOut =page.locator('//div[@class="flex-col br-6px custom__node target-node ghosted border-stroke-section-1px w-max-content"]')
 ServiceCallOut.hover()
 page.wait_for_timeout(2000)
 ServiceCallOut.click()
 page.wait_for_timeout(2000)
 
 ServiceCallOutNode =page.locator('//p[@class="color-text-regular fs-12px fw-500" and text()="Service Callout"]/ancestor::div[@class="border-stroke-section-1px bg-surface-l2 br-4px custom__node-wrapper  position-relative"]')
 ServiceCallOutNode.hover()
 page.wait_for_timeout(2000)
 ServiceCallOutNode.click()
 page.wait_for_timeout(2000)
 
 ServiceCallOutNodeNameTextField =page.locator('//input[@class="undefined   undefined null null w-100 formInputTag" and @placeholder="Enter Name"]')
 ServiceCallOutNodeNameTextField.click()
 page.wait_for_timeout(2000)
 ServiceCallOutNodeNameTextField.fill("UserDetails")
 page.wait_for_timeout(2000)
 
 ServiceCallOutNodeDescriptionTextField= page.locator('//div[@class="w-50  pb-44px flex-row vt-center gap-4px pt-4px pr-6px border-bottom-stroke-subsection-1px"]/ancestor::div[@class="form__input flex-row w-100 flex-center br-5px "]/descendant::div[@class="w-50 flex-row vt-center position-relative"]')
 ServiceCallOutNodeDescriptionTextField.click()
 ServiceCallOutNodeDescriptionTextField.fill("The User Details section displays essential information about each registered user, such as name, email address, role, and account status.")
 
 ServiceCallOutNodeHostField=page.locator('//input[@class="undefined   undefined null null w-100 formInputTag" and @placeholder="Enter HostName"]')
 ServiceCallOutNodeHostField.click()
 page.wait_for_timeout(2000)
 ServiceCallOutNodeHostField.fill("url.io")
 page.wait_for_timeout(2000)
 
 ServiceCallOutNodePathField=page.locator('//input[@class="undefined   undefined null null w-100 formInputTag" and @placeholder="Enter Path"]')
 ServiceCallOutNodePathField.click()
 page.wait_for_timeout(2000)
 ServiceCallOutNodePathField.fill("/operation")
 page.wait_for_timeout(2000)
 
 ServiceCallOutNodeSaveButton=page.locator('//p[@class="color-text-regular fs-13px fs-13px fw-500" and text()="Save"]/ancestor::div[@class=" cursor-pointer py-6px px-12px br-4px flex-center bg-surface-blue-dark border-stroke-field-border-default-1px cursor-pointer flex-center gap-8px position-relative overflow-hidden"]')
 ServiceCallOutNodeSaveButton.hover()
 page.wait_for_timeout(2000)
 ServiceCallOutNodeSaveButton.evaluate("el => el.click()")
 page.wait_for_timeout(2000)
 
 ChangeStatusButton=page.locator('//p[text()="GET - get_operation"]/ancestor::div[@class="accordion__button"]')
 ChangeStatusButton.hover()
 dots=page.locator('xpath=/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div')
 dots.wait_for(state="visible")
 dots.hover()
 dots.click()
 page.wait_for_timeout(4000)
 
 View_revision= page.locator('//div[@class="hover-bg-surface-underground cursor-pointer p-8px color-text-regular fs-13px fw-500" and text()="View Revisions"]')
 View_revision.click()
 
 page.wait_for_timeout(4000)
 
 View_revision_MouseHover = page.locator('//div[@class="flex-row vt-center hz-space-between px-8px py-10px v1-border-bottom-1 position-relative bg hover-bg-surface-underground cursor-pointer"]')
 View_revision_MouseHover.hover()
 page.wait_for_timeout(2000)
 View_revision_MouseHover.click()
 page.wait_for_timeout(2000)
 
 Revion_DripDown=page.locator('//div[@class="css-1xc3v61-indicatorContainer"]')
 Revion_DripDown.click()
 page.wait_for_timeout(2000)
 
 Approved= page.locator('//div[text()="Approved"]')
 Approved.click()
 page.wait_for_timeout(2000)
 
 Message = page.locator('//textarea[@class="formInputTag w-100 false form__input undefined null"]')
 Message.click()
 page.wait_for_timeout(2000)
 Message.fill("Approved")
 page.wait_for_timeout(2000)
 
 ChangeStatusButton=page.locator('//p[@class="text-white fs-13px fw-600" and text()="Change Status"]')
 ChangeStatusButton.click()
 try:
        page.wait_for_selector("text=Changes updated successfully")
        print("✅ workflow created succcessfully")
        page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ workflow is not created ")
        
 DeployButton =page.locator('//div[@class="border-left-stroke-section-1px bg-surface-ground h-100"]/descendant::div[@class="ripple-btn"][5]')
 DeployButton.hover()
 DeployButton.click()
 page.wait_for_timeout(2000)
 
 Select_a_host_to_deploy=page.locator('//label[@class=" text-left text-nowrap fs-13px fw-700 color-text-regular undefined " and text()="Virtual Host"]/ancestor::div[@class="form__input border-bottom-stroke-subsection-1px flex-row w-100 text-left flex-center br-5px undefined"]/descendant::div[@class="css-1wy0on6"]')
 Select_a_host_to_deploy.click()
 page.wait_for_timeout(2000)
 
 qa_dev_virtual_host=page.locator('//div[text()="test"]')
 qa_dev_virtual_host.click()
 page.wait_for_timeout(2000)
 
#  Select_a_environment=page.locator('//div[@class="css-1jqq78o-placeholder" and text()="Select a environment"]')
#  Select_a_environment.click()
#  page.wait_for_timeout(2000)
 
 Deploy = page.locator('//p[@class="fs-13px fw-600 text-white" and text()="Deploy"]')
 Deploy.click()
 page.wait_for_timeout(2000)
 try:
        page.wait_for_selector("text=Proxy deployed successfully")
        print("✅ Proxy deployed successfully")
 except Exception as e:
        print("❌ Proxy not deployed successfully")
        
 
 RunBUtton = page.locator('//p[@class="fw-500 fs-13px color-text-heading" and text()="Run"]')
 RunBUtton.hover()
 RunBUtton.click()
 page.wait_for_timeout(2000)
 
 SelectToHostToRunButtonDropDown= page.locator('//p[@class="color-text-regular fs-13px fw-600" and text()="Request"]/ancestor::div[@class="h-36px flex-row vt-center gap-8px hz-space-between px-8px py-4px border-bottom-stroke-subsection-1px"]/descendant::div[@class="css-1wy0on6"]').first
 SelectToHostToRunButtonDropDown.click()
 page.wait_for_timeout(2000)
 
 SelectingTestVirtualHostLocator = page.locator('//div[text()="test"]').first
 SelectingTestVirtualHostLocator.click()
 page.wait_for_timeout(2000)
 
 RunWithEventDropDown=page.locator('//div[@class="cursor-pointer h-32px flex-row vt-center w-32px gap-8px hz-center"]')
 RunWithEventDropDown.hover()
 RunWithEventDropDown.click()
 page.wait_for_timeout(2000)
 
 RunWithEventButton = page.locator('//div[@class="dropdown__options-item hover-bg-surface-ground-hover cursor-pointer p-8px color-text-regular fs-12px fw-500 false false px-8px py-4px fw-400" and text()="Run with Events"]')
 RunWithEventButton.hover()
 RunWithEventButton.click()
 page.wait_for_timeout(2000)
 
 ViewEventButton = page.locator('//div[@class="flex-row vt-center hz-center p-8px"]')
 ViewEventButton.click()
 page.wait_for_timeout(2000)
 try:
        page.wait_for_selector("text=200 - 200 ok")
        print("✅ 200 ok Response generated")
        
 except Exception as e:
        print("❌ Response is not generated")
        
#  DeployButton =page.locator('//div[@class="border-left-stroke-section-1px bg-surface-ground h-100"]/descendant::div[@class="ripple-btn"][4]')
#  DeployButton.hover()
#  DeployButton.click()
#  page.wait_for_timeout(2000)
 
 
 UndeployButton = page.locator('//div[@class="px-15px py-4px bg-red-1600 color-red-1700 border-red-1800  cursor-pointer br-38px text-transform-capitalize flex-center w-fit-content fs-11px fw-500 " and text()="undeploy"]')
 UndeployButton.hover()
 page.wait_for_timeout(2000)
 UndeployButton.click()
 try:
        page.wait_for_selector("text=Proxy undeployed successfully")
        print("✅ Undeployed Successfully")      
 except Exception as e:
        print("❌ not undeployed")
        
 page.wait_for_timeout(2000)  
 
 EventButton= page.locator('//p[@class="fw-500 fs-13px color-text-heading" and text()="Events"]')
 EventButton.hover()
 page.wait_for_timeout(2000)
 EventButton.click()
 page.wait_for_timeout(2000) 
     
 VirtualHostDropDown = page.locator('//p[@class="fw-700 fs-13px color-text-regular" and text()="Virtual Host"]/ancestor::div[@class="flex-center w-22 gap-6px"]/descendant::div[@class="css-1wy0on6"]')
 VirtualHostDropDown.click()
 
 TestVirtualHost =page.locator('//div[text()="test"]')
 TestVirtualHost.click()
 
 EventLogs=page.locator('//div[@class="h-30px flex-row vt-center hover-parent w-100 hover-bg-surface-blue-subtle border-bottom-stroke-subsection-1px cursor-pointer"]')
 EventLogs.hover()
 page.wait_for_timeout(2000)
 EventLogs.click()
 try:
        page.wait_for_selector("text=Execution Log")
        print("✅ Execution Log Displaying")
 except Exception as e:
        print("❌ Execution Log is not Displayed")
 
 
 Collection=page.locator('//p[@class="color-text-subtle fs-13px text-truncate-1" and text()="GET - get_operation"]/ancestor::div[@class="accordion__item"]/descendant::div[@class="flex-row vt-center gap-6px cursor-pointer"]')
 Collection.hover()
 page.wait_for_timeout(2000) 
 Collection.click()
 page.wait_for_timeout(2000) 
 
 CollectionThreeDot =page.locator('//p[@class="color-text-subtle fs-13px text-truncate-1" and text()="GET - get_operation"]/ancestor::div[@class="accordion__item"]/descendant::div[@class="accordion__heading"]/descendant::div[contains(@class, "undefined h-18px w-18px hover-bg-surface-l1-hover overflow-hidden")]')
 CollectionThreeDot.hover()
 page.wait_for_timeout(2000) 
 CollectionThreeDot.click()
 page.wait_for_timeout(2000) 
 
 DeleteButton =page.locator('//div[@class="hover-bg-surface-underground cursor-pointer p-8px color-text-regular fs-13px fw-500" and text()="Delete"]')
 DeleteButton.hover()
 page.wait_for_timeout(2000) 
 DeleteButton.click()
 page.wait_for_timeout(2000) 
 
 DeleteOkButton =page.locator('//p[@class="color-text-regular fs-13px fs-12px fw-600 text-white" and text()="Ok"]/ancestor::div[@class=" border-stroke-section-1px br-6px bg-surface-blue-dark w-72px h-28px py-5px px-8px cursor-pointer flex-center gap-8px position-relative overflow-hidden"]')
 DeleteOkButton.hover()
 DeleteOkButton.click()
 try:
        page.wait_for_selector("text=Collection deleted successfully")
        print("✅ Undeployed Successfully")      
 except Exception as e:
        print("❌ Workflow is not Deleted Successfully")
        
 
#  ChangeStatusButton=page.locator('//p[text()="GET - get_operation"]/ancestor::div[@class="accordion__button"]')
#  ChangeStatusButton.hover()
#  dots=page.locator('xpath=/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div')
#  dots.wait_for(state="visible")
#  dots.hover()
#  dots.click()
#  page.wait_for_timeout(4000)
        
#  DeleteRevision = page.locator('//div[@class="hover-bg-surface-underground cursor-pointer p-8px color-text-regular fs-13px fw-500" and text()="Delete"]')
#  DeleteRevision.click()
#  page.wait_for_timeout(2000)
 
#  DeleteOkButton =page.locator('//p[@class="color-text-regular fs-13px fs-12px fw-600 text-white" and text()="Ok"]/ancestor::div[@class=" border-stroke-section-1px br-6px bg-surface-blue-dark w-72px h-28px py-5px px-8px cursor-pointer flex-center gap-8px position-relative overflow-hidden"]').first
#  DeleteOkButton.hover()
#  DeleteOkButton.click()
#  page.wait_for_timeout(2000)
 
 
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context()
        page = context.new_page()

        # ---------- Login (Excel-driven) ----------
        username, password = get_excel_data(EXCEL_FILE)[0]  # fetch first row of Excel
        stage_login(page, username, password)  # ✅ pass the credentials
  
        print("✅ Logged in successfully")

        # ---------- Run API Design Flow ----------
        sandboxpage(page)

        print("🎯 All steps executed successfully")
        context.close()
        browser.close()

if __name__ == "__main__":
    main()


 
    
    

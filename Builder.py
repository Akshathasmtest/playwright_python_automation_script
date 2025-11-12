from playwright.sync_api import Page ,expect
from playwright.sync_api import sync_playwright
from StageLogin import  stage_login, get_excel_data ,EXCEL_FILE


def Builder(page: Page):
 page.wait_for_timeout(4000)  
    
 BuilderModule=page.locator('//div[@class="menuItems h-100 relative"]/descendant::div[@class="menuItem api-builder "]')
 try:
        BuilderModule.hover()
        page.wait_for_timeout(4000)
        BuilderModule.evaluate("el => el.click()")
        print("✅BuilderModule clicked successfully")
 except Exception as e:
        page.screenshot(path="screenshots/BuilderModule.png")
        print("📸 Screenshot saved: BuilderModule.png")
        raise Exception("❌ BuilderModule is not clicked, stopping test!")
 page.wait_for_timeout(4000)
 
 WorkflowAddButton=page.locator('//div[@class="fs-16px fw-600 color-text-heading text-nowrap" and text()="Workflows"]/ancestor::div[@class="flex-row vt-center hz-space-between px-8px border-bottom-stroke-section-1px h-36px"]/descendant::div[@class="ripple-btn"][3]')
 try:
       WorkflowAddButton.hover()
       page.wait_for_timeout(4000)
       WorkflowAddButton.click()
       print("✅Workflw created successfully")
       page.wait_for_timeout(4000)
 except Exception as e:
        page.screenshot(path="screenshots/WorkflowAddButton.png")
        print("📸 Screenshot saved: WorkflowAddButton.png")
        raise Exception("❌ WorkflowAddButton is not clicked successfully, stopping test!")
        
 ImportFromDesignStudio= page.locator('//p[@class="text-truncate-1 fs-13px fw-500 color-text-regular" and text()="Import from Design Studio"]/ancestor::div[@class="bg-surface-l1 flex-row vt-center hz-space-between gap-6px zIndex-2 pr-8px"]/descendant::div[@class="flex-row vt-center form__radio cursor-pointer"]')
 try:
       ImportFromDesignStudio.click()
       print("✅Oas is imported successfully")
 except Exception as e:
        page.screenshot(path="screenshots/ImportFromDesignStudio.png")
        print("📸 Screenshot saved: ImportFromDesignStudio.png")
        raise Exception("❌ ImportFromDesignStudio button is not clicked successfully, stopping test!")
        
 page.wait_for_timeout(2000)
 
 SpecificationDropDown= page.locator('//div[@class="css-1xc3v61-indicatorContainer"]')
 try:
       SpecificationDropDown.click(force=True)
       print("✅SpecificationDropDown Clicked Successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/SpecificationDropDown.png")
        print("📸 Screenshot saved: SpecificationDropDown.png")
        raise Exception("❌ SpecificationDropDown is not Clicked Successfully, stopping test!")
        
 SwaggerSelectionSpecificationDropDown =page.locator(f'//div[text()="Swagger_1"]')
 try:
       SwaggerSelectionSpecificationDropDown.click()
       print("✅waggerSelectionSpecificationDropDown is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/SwaggerSelectionSpecificationDropDown.png")
        print("📸 Screenshot saved: SwaggerSelectionSpecificationDropDown.png")
        raise Exception("❌ waggerSelectionSpecificationDropDown is not clicked successfully, stopping test!")
 
 RevisionDropDown =page.locator('//label[@class=" text-left text-nowrap fs-13px fw-700 color-text-regular undefined " and text()="Revision"]/ancestor::div[@class="form__input border-bottom-stroke-subsection-1px flex-row w-100 text-left flex-center br-5px undefined"]/descendant::div[@class="css-1wy0on6"]')
 try:
       RevisionDropDown.click()
       print("✅RevisionDropDown is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
       page.screenshot(path="screenshots/RevisionDropDown.png")
       print("📸 Screenshot saved: RevisionDropDown.png")
       raise Exception("❌ RevisionDropDown is not clicked successfully, stopping test!")
       
 OasRevision=page.locator('//span[text()="Revision - 1 ( Env: builder )"]')
 try:   
       OasRevision.click()
       print("✅OasRevision is selected successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
       page.screenshot(path="screenshots/OasRevision.png")
       print("📸 Screenshot saved: OasRevision.png")
       raise Exception("❌ OasRevision is not selected successfully, stopping test!")
       
 ResourceDropDown=page.locator('//label[@class=" text-left text-nowrap fs-13px fw-700 color-text-regular undefined " and text()="Resource"]/ancestor::div[@class="form__input border-bottom-stroke-subsection-1px flex-row w-100 text-left flex-center br-5px undefined"]/descendant::div[@class="css-1wy0on6"]')
 try:
     ResourceDropDown.click()
     print("✅ResourceDropDown is selected successfully")
 except Exception as e:
       page.screenshot(path="screenshots/ResourceDropDown.png")
       print("📸 Screenshot saved: ResourceDropDown.png")
       raise Exception("❌ ResourceDropDown is not selected successfully, stopping test!")
           
 SwaggerOasResource=page.locator('//div[text()="get - /operation"]')
 try:
        SwaggerOasResource.click()
        print("✅SwaggerOasResource is selected successfully")
        page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/SwaggerOasResource.png")
        print("📸 Screenshot saved: SwaggerOasResource.png")
        raise Exception("❌ SwaggerOasResource is not selected successfully, stopping test!")
 
 NextButton=page.locator('//p[@class="fw-500 fs-13px text-white" and text()="Next"]/ancestor::div[@class="position-relative overflow-hidden btn-primary cursor-pointer"]')
 try: 
       NextButton.hover()
       print("✅NextButton is hovered successfully")
       page.wait_for_timeout(2000)
       NextButton.evaluate("el => el.click()")
       print("✅NextButton is clicked successfully")
       # expect(page.get_by_text("New proxy with import data is created successfully")).to_be_visible(timeout=1500)
       page.wait_for_timeout(2000)
       print("NextButton clicked successfully")      
 except Exception as e:
        page.screenshot(path="screenshots/NextButton.png")
        print("📸 Screenshot saved: NextButton.png")
        raise Exception("❌ NextButton is not clicked successfully, stopping test!")
 
 #  Create From Blank
 ServiceCallOutAddButton=page.locator('//button[@class="vertex-edge-add-button w-14px h-14px flex-center cursor-pointer p-8px"]')
 try:
       ServiceCallOutAddButton.hover()
       print("✅ServiceCallOutAddButton is hovered successfully")
       page.wait_for_timeout(2000)
       ServiceCallOutAddButton.click()
       print("✅ServiceCallOutAddButton is Clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/ServiceCallOutAddButton.png")
        print("📸 Screenshot saved: ServiceCallOutAddButton.png")
        raise Exception("❌ ServiceCallOutAddButton is not clicked successfully, stopping test!")
        
 RestApi=page.locator('//p[@class="color-text-regular fs-13px fw-600" and text()="REST API"]/ancestor::div[contains(@class,"position-relative overflow-hidden w-100")]')
 try:
       RestApi.hover()
       print("✅RestApi Button is hovered successfully")
       page.wait_for_timeout(2000)
       RestApi.click()
       print("✅RestApi Button is Clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/RestApi.png")
        print("📸 Screenshot saved: RestApi.png")
        raise Exception("❌ RestApi Button is not clicked successfully, stopping test!")

 RestApiStartFromBlank=page.locator('//div[@class="position-relative overflow-hidden cursor-pointer fs-11px fw-600 text-nowrap px-12px py-8px text-white br-4px bg-surface-blue-dark-hover"]')
 try:
       RestApiStartFromBlank.hover()
       print("✅RestApiStartFromBlank button is hovered successfully")
       page.wait_for_timeout(2000)
       RestApiStartFromBlank.click()
       print("✅RestApiStartFromBlank button is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/RestApiStartFromBlank.png")
        print("📸 Screenshot saved: RestApiStartFromBlank.png")
        raise Exception("❌ RestApiStartFromBlank button is not clicked successfully, stopping test!")
 
 ServiceCallOut =page.locator('//div[@class="flex-col br-6px custom__node target-node ghosted border-stroke-section-1px w-max-content"]')
 try:
       ServiceCallOut.hover()
       print("✅ServiceCallOut button is hovered successfully")
       page.wait_for_timeout(2000)
       ServiceCallOut.click()
       print("✅ServiceCallOut button is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/RestApiStartFromBlank.png")
        print("📸 Screenshot saved: RestApiStartFromBlank.png") 
        raise Exception("❌ ServiceCallOut button is not clicked successfully, stopping test!")     
 
 ServiceCallOutNode =page.locator('//p[@class="color-text-regular fs-12px fw-500" and text()="Service Callout"]/ancestor::div[@class="border-stroke-section-1px bg-surface-l2 br-4px custom__node-wrapper  position-relative"]')
 try:
       ServiceCallOutNode.hover()
       print("✅ServiceCallOutNode is hovered successfully")
       page.wait_for_timeout(2000)
       ServiceCallOutNode.click()
       print("✅ServiceCallOutNode is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/ServiceCallOutNode.png")
        print("📸 Screenshot saved: ServiceCallOutNode.png") 
        raise Exception("❌ ServiceCallOutNode is not clicked successfully, stopping test!")
 
 ServiceCallOutNodeNameTextField =page.locator('//input[@class="undefined   undefined null null w-100 formInputTag" and @placeholder="Enter Name"]')
 try:
       ServiceCallOutNodeNameTextField.click()
       print("✅ServiceCallOutNodeNameTextField is clicked successfully")
       page.wait_for_timeout(2000)
       ServiceCallOutNodeNameTextField.fill("UserDetails")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/ServiceCallOutNodeNameTextField.png")
        print("📸 Screenshot saved: ServiceCallOutNodeNameTextField.png")
        raise Exception("❌ ServiceCallOutNodeNameTextField is not clicked successfully, stopping test!")
 
 ServiceCallOutNodeDescriptionTextField= page.locator('//textarea[@class="formInputTag w-100  undefined undefined null" and @placeholder="Enter Description"]')
 try:
       ServiceCallOutNodeDescriptionTextField.click()
       print("✅ServiceCallOutNodeDescriptionTextField is clicked successfully")
       ServiceCallOutNodeDescriptionTextField.fill("The User Details section displays essential information about each registered user, such as name, email address, role, and account status.")
 except Exception as e:
        page.screenshot(path="screenshots/ServiceCallOutNodeDescriptionTextField.png")
        print("📸 Screenshot saved: ServiceCallOutNodeDescriptionTextField.png") 
        raise Exception("❌ ServiceCallOutNodeDescriptionTextField is not clicked successfully, stopping test!")
 
 ServiceCallOutNodeHostField=page.locator('//input[@class="undefined   undefined null null w-100 formInputTag" and @placeholder="Enter HostName"]')
 try:
       ServiceCallOutNodeHostField.click()
       print("✅ServiceCallOutNodeHostField is clicked successfully")
       page.wait_for_timeout(2000)
       ServiceCallOutNodeHostField.fill("url.io")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/ServiceCallOutNodeHostField.png")
        print("📸 Screenshot saved: ServiceCallOutNodeHostField.png")
        raise Exception("❌ ServiceCallOutNodeHostField is not clicked successfully, stopping test!")
 
 
 ServiceCallOutNodePathField=page.locator('//input[@class="undefined   undefined null null w-100 formInputTag" and @placeholder="Enter Path"]')
 try:
       ServiceCallOutNodePathField.click()
       print("✅ServiceCallOutNodePathField is clicked successfully")
       page.wait_for_timeout(2000)
       ServiceCallOutNodePathField.fill("/operation")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/ServiceCallOutNodePathField.png")
        print("📸 Screenshot saved: ServiceCallOutNodePathField.png")
        raise Exception("❌ ServiceCallOutNodePathField is not clicked successfully, stopping test!")
 
 ServiceCallOutNodeSaveButton=page.locator('//p[@class="color-text-regular fs-13px fs-13px fw-500" and text()="Save"]/ancestor::div[@class=" cursor-pointer py-6px px-12px br-4px flex-center bg-surface-blue-dark border-stroke-field-border-default-1px cursor-pointer flex-center gap-8px position-relative overflow-hidden"]')
 try:
       ServiceCallOutNodeSaveButton.hover()
       print("✅ServiceCallOutNodeSaveButton is hovered successfully")
       page.wait_for_timeout(2000)
       ServiceCallOutNodeSaveButton.evaluate("el => el.click()")
       print("✅ServiceCallOutNodeSaveButton is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/ServiceCallOutNodeSaveButton.png")
        print("📸 Screenshot saved: ServiceCallOutNodeSaveButton.png")
        raise Exception("❌ ServiceCallOutNodeSaveButton is not clicked successfully, stopping test!")
 
 ChangeStatusButton=page.locator('//p[text()="GET - get_operation"]/ancestor::div[@class="accordion__button"]/ancestor::div[@class="accordion__heading"]')
 try:
       ChangeStatusButton.wait_for(state="visible")
       ChangeStatusButton.hover()
       print("✅ChangeStatusButton is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/ChangeStatusButton.png")
        print("📸 Screenshot saved: ChangeStatusButton.png")
        raise Exception("❌ ChangeStatusButton is not clicked successfully, stopping test!")
        
 ChangeStatusButtonDots=page.locator('xpath=/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div/div')
 try:
       ChangeStatusButtonDots.wait_for(state="visible")
       ChangeStatusButtonDots.hover()
       print("✅ChangeStatusButtonThreeDots hovered successfully")
       ChangeStatusButtonDots.evaluate("el => el.click()")
       print("✅ChangeStatusButtonThreeDots is clicked successfully")
       page.wait_for_timeout(4000)
 except Exception as e:
        page.screenshot(path="screenshots/ChangeStatusButtonDots.png")
        print("📸 Screenshot saved: ChangeStatusButtonDots.png")
        raise Exception("❌ ChangeStatusButtonThreeDots is not clicked successfully, stopping test!")
        
 ViewRevisionButton= page.locator('//div[@class="hover-bg-surface-underground cursor-pointer p-8px color-text-regular fs-13px fw-500" and text()="View Revisions"]')
 try:
       ViewRevisionButton.click()
       print("✅ViewRevisionButton is clicked successfully")
 except Exception as e:
        page.screenshot(path="screenshots/ViewRevision.png")
        print("📸 Screenshot saved: ViewRevision.png")
        raise Exception("❌ ViewRevisionButton is not clicked successfully, stopping test!")     
 
 page.wait_for_timeout(4000)
 
 ViewRevisionOption = page.locator('//div[@class="flex-row vt-center hz-space-between px-8px py-10px v1-border-bottom-1 position-relative bg hover-bg-surface-underground cursor-pointer"]')
 try:
       ViewRevisionOption.hover()
       print("✅ViewRevisionOption is hovered successfully")
       page.wait_for_timeout(2000)
       ViewRevisionOption.click()
       print("✅ViewRevisionOption is clciked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/ViewRevisionMouseHover.png")
        print("📸 Screenshot saved: ViewRevisionMouseHover.png")
        raise Exception("❌ ViewRevisionOption is not clicked successfully, stopping test!") 
 
 RevionDropDown=page.locator('//div[@class="css-1xc3v61-indicatorContainer"]')
 try:
       RevionDropDown.click()
       print("✅RevionDropDown is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/RevionDropDown.png")
        print("📸 Screenshot saved: RevionDropDown.png")  
        raise Exception("❌ RevionDropDown is not clicked successfully, stopping test!")
 
 ApprovedButtonInRevionDropDown= page.locator('//div[text()="Approved"]')
 try:
       ApprovedButtonInRevionDropDown.click()
       print("✅ApprovedButtonInRevionDropDown is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/ApprovedButtonInRevionDropDown.png")
        print("📸 Screenshot saved: ApprovedButtonInRevionDropDown.png") 
        raise Exception("❌ ApprovedButtonInRevionDropDown is clicked successfully, stopping test!")
 
 MessageForApprovedStatusTextfield = page.locator('//textarea[@class="formInputTag w-100 false form__input undefined null"]')
 try:
       MessageForApprovedStatusTextfield.click()
       print("✅MessageForApprovedStatusTextfield is clicked successfully")
       page.wait_for_timeout(2000)
       MessageForApprovedStatusTextfield.fill("Approved")
       page.wait_for_timeout(2000)
 except Exception as e:
        page.screenshot(path="screenshots/MessageForApprovedStatus.png")
        print("📸 Screenshot saved: MessageForApprovedStatus.png") 
        raise Exception("❌ MessageForApprovedStatusTextfield is clicked successfully, stopping test!")
        
 ChangeStatusButton=page.locator('//p[@class="text-white fs-13px fw-600" and text()="Change Status"]')
 try:   
        ChangeStatusButton.click()
        page.wait_for_selector("text=Changes updated successfully")
        print("✅ workflow created succcessfully")
        page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ workflow is not created ")
        page.screenshot(path="screenshots/ChangeStatusButton.png")
        print("📸 Screenshot saved: ChangeStatusButton.png")
        raise Exception("❌ ChangeStatusButton is clicked successfully, stopping test!")
        
 DeployButton =page.locator('//div[@class="border-left-stroke-section-1px bg-surface-ground h-100"]/descendant::div[@class="ripple-btn"][5]')
 try:
       DeployButton.hover()
       DeployButton.click()
       print("✅  workflow Deployed Successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ workflow is not Deploy")
        page.screenshot(path="screenshots/DeployButton.png")
        print("📸 Screenshot saved: DeployButton.png")
        raise Exception("❌ workflow is not Deploy, stopping test!")
 
 Select_a_host_to_deploy=page.locator('//label[@class=" text-left text-nowrap fs-13px fw-700 color-text-regular undefined " and text()="Virtual Host"]/ancestor::div[@class="form__input border-bottom-stroke-subsection-1px flex-row w-100 text-left flex-center br-5px undefined"]/descendant::div[@class="css-1wy0on6"]')
 try:
       Select_a_host_to_deploy.click()
       print(" ✅ Host details is selected from dropdown")
       page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ Host details is not selected from dropdown")
        page.screenshot(path="screenshots/Select_a_host_to_deploy.png")
        print("📸 Screenshot saved: Select_a_host_to_deploy.png")
        raise Exception("❌ Select_a_host_to_deploy Button is not clicked successfully, stopping test!")
 
 qaDevVirtualHost=page.locator('//div[text()="qa-dev"]')
 try:
       qaDevVirtualHost.click()
       print("✅ qaDevVirtualHost is selected from virtual dropdown")
       page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ qaDevVirtualHost is not selected from virtual dropdown")
        page.screenshot(path="screenshots/Select_a_host_to_deploy.png")
        print("📸 Screenshot saved: Select_a_host_to_deploy.png")
        raise Exception("❌ qaDevVirtualHost is not selected from virtual dropdown, stopping test!")
 
 
#  Select_a_environment=page.locator('//div[@class="css-1jqq78o-placeholder" and text()="Select a environment"]')
#  Select_a_environment.click()
#  page.wait_for_timeout(2000)
 
 Deploy = page.locator('//p[@class="fs-13px fw-600 text-white" and text()="Deploy"]')
 try:
        Deploy.click()
        page.wait_for_timeout(2000)
        page.wait_for_selector("text=Proxy deployed successfully")
        print("✅ Deploy button is clicked successfully")
 except Exception as e:
        print("❌ Deploy button is not clicked successfully")
        page.screenshot(path="screenshots/Deploy.png")
        print("📸 Screenshot saved: Deploy.png")
        raise Exception("❌ Deploy button is not clicked successfully, stopping test!")
 
 RunButton = page.locator('//p[@class="fw-500 fs-13px color-text-heading" and text()="Run"]')
 try:
       RunButton.hover()
       print("✅ Runbutton is hovered successfully")
       RunButton.click()
       print("✅ Runbutton is clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ Runbutton is not clicked")
        page.screenshot(path="screenshots/RunButton.png")
        print("📸 Screenshot saved: RunButton.png")
        raise Exception("❌ Runbutton is not clicked, stopping test!")

 virtualHostListDropdownInRequestSection= page.locator('//p[@class="color-text-regular fs-13px fw-600" and text()="Request"]/ancestor::div[@class="h-36px flex-row vt-center gap-8px hz-space-between px-8px py-4px border-bottom-stroke-subsection-1px"]/descendant::div[@class="css-1wy0on6"]').first
 try:
       virtualHostListDropdownInRequestSection.click()
       print("✅  virtualHostListDropdownInRequestSection is selected successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ virtualHostListDropdownInRequestSection is not selected successfully")
        page.screenshot(path="screenshots/virtualHostListDropdownInRequestSection.png")
        print("📸 Screenshot saved: virtualHostListDropdownInRequestSection.png")
        raise Exception("❌virtualHostListDropdownInRequestSection is not selected successfully, stopping test!")
 
 SelectingTestVirtualHostInRequestSection = page.locator('//div[text()="qa-dev"]').first
 try:
       SelectingTestVirtualHostInRequestSection.click()
       print("✅  SelectingTestVirtualHostInRequestSection is selected successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ SelectingTestVirtualHostInRequestSection is not selected successfully")
        page.screenshot(path="screenshots/virtualHostListDropdownInRequestSection.png")
        print("📸 Screenshot saved: virtualHostListDropdownInRequestSection.png")
        raise Exception("❌SelectingTestVirtualHostInRequestSection is not selected successfully, stopping test!")
 
 RunWithEventDropDown=page.locator('//div[@class="cursor-pointer h-32px flex-row vt-center w-32px gap-8px hz-center"]')
 try:
       RunWithEventDropDown.hover()
       print("✅ RunWithEventDropDown hovered successfully")
       RunWithEventDropDown.click()
       print("✅ RunWithEventDropDown clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ RunWithEventDropDown is not clicked successfully")
        page.screenshot(path="screenshots/RunWithEventDropDown.png")
        print("📸 Screenshot saved: RunWithEventDropDown.png")
        raise Exception("❌RunWithEventDropDown is not clicked successfully, stopping test!")
 
 RunWithEventButton = page.locator('//div[@class="dropdown__options-item hover-bg-surface-ground-hover cursor-pointer p-8px color-text-regular fs-12px fw-500 false false px-8px py-4px fw-400" and text()="Run with Events"]')
 try:
       RunWithEventButton.hover()
       print("✅ RunWithEventButton hovered successfully")
       RunWithEventButton.click()
       print("✅ RunWithEventButton clicked successfully")
       page.wait_for_timeout(2000)
 except Exception as e:
        print("❌ RunWithEventButton is not clicked successfully")
        page.screenshot(path="screenshots/RunWithEventButton.png")
        print("📸 Screenshot saved: RunWithEventButton.png")
        raise Exception("❌RunWithEventButton is not clicked successfully, stopping test!")
 
 ViewEventButton = page.locator('//div[@class="flex-row vt-center hz-center p-8px"]')
 try: 
        ViewEventButton.click()
        page.wait_for_timeout(2000)
        page.wait_for_selector("text=200 - 200 ok")
        print("✅ ViewEventButton Cliked successfully")
 except Exception as e:
        print("❌ ViewEventButton is not Cliked successfully")
        page.screenshot(path="screenshots/ViewEventButton.png")
        print("📸 Screenshot saved: ViewEventButton.png")
        raise Exception("❌ViewEventButton is not Cliked successfully, stopping test!")
 
 UndeployButton = page.locator('//div[@class="px-15px py-4px bg-red-1600 color-red-1700 border-red-1800  cursor-pointer br-38px text-transform-capitalize flex-center w-fit-content fs-11px fw-500 " and text()="undeploy"]')
 try:
        UndeployButton.hover()
        print("✅ UndeployButton hovered successfully")
        page.wait_for_timeout(2000)
        UndeployButton.click()
        print("✅ UndeployButton Cliked successfully")
        page.wait_for_selector("text=Proxy undeployed successfully")
        print("✅ UndeployButton Successfully")      
 except Exception as e:
        print("❌ UndeployButton is not Cliked successfully")
        raise Exception("❌UndeployButton is not Cliked successfully, stopping test!")
        
 page.wait_for_timeout(2000)  
 
 EventButton= page.locator('//p[@class="fw-500 fs-13px color-text-heading" and text()="Events"]')
 try:
       EventButton.hover()
       print("✅ EventButton hovered successfull")
       page.wait_for_timeout(2000)
       EventButton.click()
       print("✅ EventButton is clicked successfull")
 except Exception as e:
       page.screenshot(path="screenshots/EventButton.png")
       print("📸 Screenshot saved: EventButton.png")
       page.wait_for_timeout(2000) 
       raise Exception("❌EventButton not Cliked successfully, stopping test!")
       
     
 VirtualHostDropDown = page.locator('//p[@class="fw-700 fs-13px color-text-regular" and text()="Virtual Host"]/ancestor::div[@class="flex-center w-22 gap-6px"]/descendant::div[@class="css-1wy0on6"]')
 try:
       VirtualHostDropDown.click()
       print("✅ VirtualHostDropDown is Cliked successfully")
 except Exception as e:
       page.screenshot(path="screenshots/VirtualHostDropDown.png")
       print("📸 Screenshot saved: VirtualHostDropDown.png")
       raise Exception("❌VirtualHostDropDown is not Cliked successfully, stopping test!")
 page.wait_for_timeout(2000) 
 
 QaDevVirtualHostInEvent =page.locator('//div[@class="css-1dimb5e-singleValue" and text()="qa-dev"]')
 try:
       QaDevVirtualHostInEvent.evaluate("el => el.click()")
       print("✅ QaDevVirtualHostInEvent is Cliked successfully")
 except Exception as e:
       page.screenshot(path="screenshots/TestVirtualHost.png")
       print("📸 Screenshot saved: TestVirtualHost.png")
       raise Exception("❌QaDevVirtualHostInEventt is not Cliked successfully, stopping test!")
 
 EventLogs=page.locator('//div[@class="h-30px flex-row vt-center hover-parent w-100 hover-bg-surface-blue-subtle border-bottom-stroke-subsection-1px cursor-pointer"]')
 try:
        EventLogs.hover()
        print("✅ EventLogs is hovered successfully")
        page.wait_for_timeout(2000)
        EventLogs.click()
        print("✅ EventLogs is clicked successfully")
        page.wait_for_selector("text=Execution Log")
        print("✅ Execution Log Displaying")
 except Exception as e:
        print("❌ Execution Log is not Displayed")
        page.screenshot(path="screenshots/EventLogs.png")
        print("📸 Screenshot saved: EventLogs.png")
        raise Exception("❌EventLogs is not Cliked successfully, stopping test!")
 
 Collection=page.locator('//p[text()="GET - get_operation"]/ancestor::div[@class="accordion__button"]/ancestor::div[@class="accordion__heading"]')
 Collection.wait_for(state="visible")
 Collection.hover()
 print("✅ Collection is hovered successfully")
 page.wait_for_timeout(2000)
 CollectionThreeDot=page.locator('xpath=/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div/div')
 CollectionThreeDot.wait_for(state="visible")
 CollectionThreeDot.hover()
 print("✅ CollectionThreeDot is hovered successfully")
 CollectionThreeDot.evaluate("el => el.click()")
 print("✅ CollectionThreeDot is clicked successfully")
 page.wait_for_timeout(4000)
 
 DeleteButton =page.locator('//div[@class="hover-bg-surface-underground cursor-pointer p-8px color-text-regular fs-13px fw-500" and text()="Delete"]')
 try:
        DeleteButton.hover()
        print("✅ DeleteButton is hovered successfully")
        page.wait_for_timeout(4000) 
        DeleteButton.click()
        print("✅ DeleteButton is clicked successfully")
 except Exception as e:
        page.screenshot(path="screenshots/DeleteButton.png")
        print("📸 Screenshot saved: DeleteButton.png")
        page.wait_for_timeout(4000) 
        raise Exception("❌DeleteButton is not Cliked successfully, stopping test!")
 
#  DeleteOkButton =page.locator('//p[@class="color-text-regular fs-13px fs-12px fw-600 text-white" and text()="Ok"]/ancestor::div[@class=" border-stroke-section-1px br-6px bg-surface-blue-dark w-72px h-28px py-5px px-8px cursor-pointer flex-center gap-8px position-relative overflow-hidden"]')
#  DeleteOkButton.hover()
#  page.wait_for_timeout(2000)
#  DeleteOkButton.click()
 
#  DeleteOkButton =page.locator('//p[@class="color-text-regular fs-13px fs-12px fw-600 text-white" and text()="Ok"]/ancestor::div[@class=" border-stroke-section-1px br-6px bg-surface-blue-dark w-72px h-28px py-5px px-8px cursor-pointer flex-center gap-8px position-relative overflow-hidden"]')
#  try:
#         DeleteOkButton.hover()
#         page.wait_for_timeout(2000) 
#         print("✅ DeleteOkButton is hovered successfully")
#         DeleteOkButton.click()
#         page.wait_for_timeout(2000) 
#        #  page.wait_for_selector("text=Collection deleted successfully")
#         print("✅ Undeployed Successfully")      
#  except Exception as e:
#         print("❌ Workflow is not Deleted Successfully")
#         page.screenshot(path="screenshots/DeleteOkButton.png")
#         print("📸 Screenshot saved: DeleteOkButton.png")
#         raise Exception("❌Workflow is not Deleted Successfully, stopping test!")
 
 try:
       DeleteOkButton = page.locator('//p[@class="color-text-regular fs-13px fs-12px fw-600 text-white" and text()="Ok"]/ancestor::div[@class=" border-stroke-section-1px br-6px bg-surface-blue-dark w-72px h-28px py-5px px-8px cursor-pointer flex-center gap-8px position-relative overflow-hidden"]')
    
       DeleteOkButton.wait_for(state="visible", timeout=5000)
       DeleteOkButton.hover()
       page.wait_for_timeout(2000)
       print("✅ DeleteOkButton is hovered successfully")
    
       DeleteOkButton.click()
       page.wait_for_timeout(2000)
       print("✅ Undeployed Successfully")      
 except Exception as e:
    print(f"❌ Workflow is not Deleted Successfully: {e}")
    page.screenshot(path="screenshots/DeleteOkButton.png")
    print("📸 Screenshot saved: DeleteOkButton.png")
    raise

# evaluate("el => el.click()")
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
        Builder(page)

        print("🎯 All steps executed successfully")
        context.close()
        browser.close()

if __name__ == "__main__":
    main()
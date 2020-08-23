from selenium import webdriver


#Open Browser
driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")


#Go to Parking webpage
driver.get(r"https://access.e-park.dk/Account/Login")

#Find Email field and insert email
driver.implicitly_wait(10) # seconds
driver.find_element_by_id("Email").click()
driver.find_element_by_id("Email").send_keys("EMAIL")

#Find Password field and insert password
driver.implicitly_wait(10) # seconds
driver.find_element_by_id("Password").click()
driver.find_element_by_id("Password").send_keys("KODE")

#Press login button
driver.implicitly_wait(10) # seconds
driver.find_element_by_css_selector(".button[value = 'Log ind']").click()

#Find Licenseplate field and insert
driver.implicitly_wait(10) # seconds
driver.find_element_by_name("LicensePlate").send_keys("NUMMERPLADE")

#Find email field and insert
driver.implicitly_wait(10) # seconds
driver.find_element_by_xpath("/html/body/div/div/div[2]/section/form/div/div[3]/div[2]/div[2]/div/input").send_keys("EMAIL?")

#Press confirm button
driver.find_element_by_css_selector(".button[value = 'Opret P-tilladelse']").click()

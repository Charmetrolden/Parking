from selenium import webdriver

driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")

driver.get(r"https://access.e-park.dk/Account/Login")


#driver.find_element_by_id("Email").click()
driver.find_element_by_id("Email").send_keys("Bayramozturk@msn.com")


#driver.find_element_by_id("Password").click()
driver.find_element_by_id("Password").send_keys("Kayseri38")


driver.find_element_by_css_selector(".button[value = 'Log ind']").click()

#driver.implicitly_wait(10) # seconds
driver.find_element_by_id("LicensePlate").click()
driver.find_element_by_id("LicensePlate").send_keys("CH28806")

#driver.find_element_by_name("Email").click()
#driver.find_element_by_name("Email").send_keys("omer96@live.dk")

driver.find_element_by_xpath("/html/body/div/div/div[2]/section/form/div/div[3]/div[2]/div[2]/div/input").send_keys("omer96@live.dk")
driver.find_element_by_css_selector(".button[value = 'Opret P-tilladelse']").click()

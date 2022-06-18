from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://karresults.nic.in/slpuind.asp")

reg= driver.find_element_by_name("reg").send_keys("000000") #enter required puc reg no 

dropdown = Select(driver.find_element_by_id("ddlsub"))
dropdown.select_by_value("S")  #for arts select "A" for commerce select "C"

button=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/form/button').click()


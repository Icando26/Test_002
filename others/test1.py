from selenium import webdriver
from time import sleep
driver=webdriver.Firefox(executable_path = '/users/zyl/Downloads/geckodriver')
driver.get("https://www.pgyer.com/user/login")

driver.find_element_by_id("email").send_keys("2197999082@qq.com")
driver.find_element_by_id("password").send_keys("SZLVDU01")

sleep(3)

driver.find_element_by_id("submitButton").click()


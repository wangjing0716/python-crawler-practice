from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('D:\other software\chromedriver_win32\chromedriver.exe')
driver.get("https://www.baidu.com")

# input = driver.find_element_by_css_selector('#kw')
input = driver.find_element(by=By.ID, value="kw")
input.send_keys("高考")

# button = driver.find_element_by_css_selector('#su')
button = driver.find_element(by=By.ID, value="su")
button.click()

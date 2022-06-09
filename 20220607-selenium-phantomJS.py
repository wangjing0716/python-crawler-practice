from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome('D:\other software\chromedriver_win32\chromedriver.exe')
# browser = webdriver.PhantomJS()
browser.get("https://www.bilibili.com/")

soon_login_btn = WebDriverWait(browser, 20).until(presence_of_element_located((By.CSS_SELECTOR, ".login-btn")))
soon_login_btn.click()

username = WebDriverWait(browser, 20).until(presence_of_element_located((By.CSS_SELECTOR, ".bili-mini-account")))
password = WebDriverWait(browser, 20).until(presence_of_element_located((By.CSS_SELECTOR, ".bili-mini-password")))
submit = WebDriverWait(browser, 20).until(
    element_to_be_clickable((By.XPATH, "//*[substring(@class,string-length(@class)-9)=' login-btn']")))

username.send_keys('2515847748@qq.com')
password.send_keys('你的密码')
submit.click()

input = WebDriverWait(browser, 20).until(
    presence_of_element_located((By.CSS_SELECTOR, "#banner_link > div > div > form > input")))
submit = WebDriverWait(browser, 20).until(
    element_to_be_clickable((By.XPATH, '//*[@id="banner_link"]/div/div/form/button')))

input.send_keys('蔡徐坤 篮球')
submit.click()

# todo login

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Desktop\\Data\\aKrishna\\study\\Testing\\chromedriver.exe")
driver.implicitly_wait(2)
driver.get("http://www.google.com")
print(driver.title)

time.sleep(2)
driver.quit()
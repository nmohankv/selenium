from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Desktop\\Data\\aKrishna\\study\\Testing\\chromedriver.exe")
driver.implicitly_wait(2)
driver.get("http://www.google.com")
print(driver.title)
driver.find_element(By.NAME,'q').send_keys("selenium python")
opList=driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(opList))
for ele in opList:
    print(ele.text)
    continue

time.sleep(2)
driver.quit()
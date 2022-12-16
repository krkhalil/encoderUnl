# 👇️ for Selenium version 3
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.geeksforgeeks.org/")
element = driver.find_element_by_xpath('(//div[@class="ant-row"])[1]')
time.sleep(2)
element.screenshot('foo1.png')
time.sleep(2)

driver.close()

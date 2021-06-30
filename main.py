from idlelib import window

from selenium import webdriver
from urllib3.util import url

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://www.google.com")


driver.maximize_window()
#print(driver.title)
#print(driver.current_url)

driver.find_element_by_xpath("//div[2]/input[1]").send_keys("amazon.in")
driver.find_element_by_xpath("//div[3]/center/input[1]").click()
driver.find_element_by_xpath("//h3[contains(text(),'Amazon.in')]").click()
#driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
driver.find_element_by_id("twotabsearchtextbox").send_keys("mobile")
driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()
driver.find_element_by_xpath("//span[contains(text(),'Samsung Galaxy M42 5G ')]").click()

a = driver.window_handles
driver.switch_to.window(a[1])

driver.find_element_by_xpath("//p[contains(text(),'8GB RAM & 128GB Storage')]").click()

desc = driver.find_element_by_xpath("//div[@id='featurebullets_feature_div']/div[@id='feature-bullets']/ul[1]").text
print("Description: " +desc)

#price = driver.find_element_by_xpath("//span[@id='priceblock_ourprice']")
#print(price)

driver.find_element_by_id("add-to-cart-button").click()

driver.close()
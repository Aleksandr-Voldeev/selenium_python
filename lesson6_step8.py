import math 
import time

from selenium import webdriver 

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/find_xpath_form")

try:
    input1 = driver.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    
    input3 = driver.find_element_by_name("firstname")
    input3.send_keys("Smolensk")
    
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    
    button = driver.find_element_by_xpath("//div[6]/button[3]")
    button.click()

finally:
    
    time.sleep(30)
    
    browser.quit()

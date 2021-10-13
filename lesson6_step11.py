import math 
import time

from selenium import webdriver 

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/registration2")

try:
    
    input1 = driver.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    
    input2 = driver.find_element_by_css_selector("input.form-control.third")
    input2.send_keys("Petrov")
    
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    
    time.sleep(30)
    
    browser.quit()

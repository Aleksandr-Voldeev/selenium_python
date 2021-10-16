import math
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()
finally:
    time.sleep(30)
    browser.quit()

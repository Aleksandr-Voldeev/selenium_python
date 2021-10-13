from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver

try: 
    link = "http://suninjuly.github.io/registration1.html"
    driver: WebDriver = webdriver.Chrome()
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = driver.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")
    
    input2 = driver.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    
    input3 = driver.find_element_by_css_selector(".first_block .third")
    input3.send_keys("test@mail.com")
    
    input4 = driver.find_element_by_css_selector(".second_block .first")
    input4.send_keys("123456789101")
    
    input5 = driver.find_element_by_css_selector(".second_block .second")
    input5.send_keys("adress")

    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver: WebDriver.quit()
    
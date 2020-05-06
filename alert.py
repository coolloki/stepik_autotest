import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Edge()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    submit = browser.find_element_by_css_selector("[type = 'submit']")
    submit.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_css_selector("#input_value")
    x = x.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    submit = browser.find_element_by_css_selector("[type = 'submit']")
    submit.click()
    result = browser.switch_to.alert
    result = result.text
    print (result)

finally:
    browser.quit()
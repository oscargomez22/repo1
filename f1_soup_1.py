from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

br = webdriver.Chrome()
br.get('https://www.formula1.com/en/f1-live.html')


element = br.find_element_by_id("truste-consent-button")

action = ActionChains(br)
action.click(on_element=element)
action.perform()


time.sleep(3)

br.get("https://account.formula1.com/#/en/login?redirect=https%3A%2F%2Fwww.formula1.com%2Fen%2Ff1-live.html&lead_source=web_f1core")

time.sleep(3)

inputElement = br.find_element_by_class_name("txtLogin")
inputElement.send_keys('22.o.gomez@gmail.com')

inputElement = br.find_element_by_class_name("txtPassword")
inputElement.send_keys('patata')

#inputElement.send_keys(Keys.ENTER)

print("done")


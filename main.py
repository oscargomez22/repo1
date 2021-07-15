from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#html_text = requests.get('https://www.fiaformula2.com/livetiming/index.html').text
#soup = BeautifulSoup(html_text, 'lxml')
#rows = soup.find('td', class_ ='interval')
#print(html_text)

url = 'https://www.fiaformula2.com/livetiming/index.html'

option = webdriver.ChromeOptions()
option.add_argument("--headless")

driver = webdriver.Chrome()
driver.implicitly_wait(100)


driver.get(url)
soup_level1 = BeautifulSoup(driver.page_source, 'lxml')

body = driver.execute_script("return document.body")
source = body.get_attribute('innerHTML') 

print(source)

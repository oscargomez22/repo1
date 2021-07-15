from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

time_start = time.perf_counter()
chrome_options = Options()
chrome_options.add_argument("--headless")


br = webdriver.Chrome(options=chrome_options)
br.get('https://www.fiaformula2.com/livetiming/index.html')

time.sleep(1)

html = br.page_source

soup_level1 = BeautifulSoup(html, 'lxml')

soup_driver = soup_level1.find_all('td', class_ = "driver-full-name ng-binding")
soup_s1 = soup_level1.find_all('td', class_ = "sector1-time ng-binding")
soup_s2 = soup_level1.find_all('td', class_ = "sector2-time ng-binding")
soup_s3 = soup_level1.find_all('td', class_ = "sector3-time ng-binding")

time_end = time.perf_counter()
#print(soup_level2)

i = 0
while i < len(soup_driver):
    print(soup_driver[i].text + "     " + soup_s1[i].text + "     " + soup_s2[i].text + "     " + soup_s3[i].text)
    i += 1

br.quit()
print(time_end-time_start)

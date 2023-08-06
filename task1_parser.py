from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests


URL = 'https://nedradv.ru/nedradv/ru/auction'

driver = webdriver.Chrome()
dates = driver.find_elements(By.NAME, 'a')

for date in dates:
    print(date.text)

response = requests.get(URL)
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)

driver.quit()

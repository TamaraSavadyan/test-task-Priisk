from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

URL = 'https://nedradv.ru/nedradv/ru/auction'
DOMAIN = 'https://nedradv.ru'
driver_chrome = webdriver.Chrome()


def parse_data(driver: webdriver, url: str):
    driver.get(url)
    file_path = 'data2.json'
    output = []
    json_result = []
    urls = []
    conditions = [
        'Срок подачи заявок',
        'Взнос за участие в аукционе (руб)',
        'Организатор'
    ]

    elements = driver.find_elements(By.CLASS_NAME, 'g-color-gray-dark-v1')

    for i, element in enumerate(elements[:401]):
        if not i % 3 and i:
            data_src_value = element.get_attribute('data-src')
            new_url = f'{DOMAIN}{data_src_value}'
            if not new_url in urls:
                urls.append(new_url)

        if not i % 4 and i:
            data = {
                'Дата': output[0],
                'Участок': output[1],
                'Регион': output[2],
                'Статус': output[3],
            }

            json_result.append(data)
            output.clear()

        output.append(element.text)
    
   

    for i, url in enumerate(urls):
        driver.get(url)
        elems_json = dict()

        elements1 = driver.find_elements(By.CLASS_NAME, 'col-sm-3')
        elements2 = driver.find_elements(By.CLASS_NAME, 'col-sm-9')

        for elems in zip(elements1, elements2):
            if elems[0].text in conditions:
                elems_json[elems[0].text] = elems[1].text

        json_result[i] = {**json_result[i], **elems_json}

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_result, json_file, indent=2, ensure_ascii=False)

    # input('Press any key to exit...')
    driver.quit()


if __name__ == '__main__':
    parse_data(driver_chrome, URL)
    

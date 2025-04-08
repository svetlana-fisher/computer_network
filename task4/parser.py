import csv
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# загрузка драйвера
def init_driver():
    driver = webdriver.Firefox()
    return driver

# парсинг страницы
def fetch_data(driver):
    data = []
    # Находим элементы на странице
    authors_name_elements = driver.find_elements(By.CLASS_NAME, "tm-article-snippet__meta")
    article_name_elements = driver.find_elements(By.CLASS_NAME, "tm-title__link")
    articles_text_elements = driver.find_elements(By.CLASS_NAME, "tm-publication-hubs__container")

    # Проходим по всем элементам и собираем данные
    for i in range(len(authors_name_elements)):
        authors_data = (authors_name_elements[i].text).split('\n')
        authors_name = authors_data[0]
        published_time = authors_data[1]

        articles_title = article_name_elements[i].text

        publication_hubs = articles_text_elements[i].text if i < len(articles_text_elements) else ''
        # Убираем символы '*' и заменяем '\n' на '; '
        publication_hubs = publication_hubs.replace('*', '').replace('\n', '; ').strip()

        data.append([authors_name, published_time, articles_title, publication_hubs])
    return data

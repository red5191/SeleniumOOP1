# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)
# pip3 install faker (Устанавливаем библиотеку faker)

# импортируем необходимые библиотеки и элементы
import time
# from datetime import datetime, timedelta
# from faker import Faker
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

base_url = 'https://www.saucedemo.com/'


class AutoTest:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver = driver

    def test_start(self, link):
        self.driver.get(link)
        self.driver.maximize_window()

    def test_end(self):
        time.sleep(5)
        self.driver.quit()


test = AutoTest()
test.test_start(base_url)
test.test_end()
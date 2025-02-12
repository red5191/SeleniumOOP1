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


class AutoTest:

    def __init__(self, link, headless=False):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        if headless:
            self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))
        self.base_url = link

    def test_start(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def test_end(self, seconds=5):
        time.sleep(seconds)
        self.driver.quit()

base_url = 'https://www.saucedemo.com/'
test = AutoTest(base_url, headless=False)
test.test_start()
test.test_end()
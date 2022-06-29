from os import getcwd, path
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Edge():
    """ Класс для загрузки драйверов и запуска браузера"""
    def way_driver(self):
        """ Получаем директорию для драйвера"""
        way_driver = path.join(getcwd(), "driver") # получили путь текущей директории + папка для driver
        return way_driver
    def install_driver(self):
        """Установка драйвера в директорию"""
        way = self.way_driver()
        path_driver = EdgeChromiumDriverManager(path=way).install()
        return path_driver
    def open_edge(self):
        """ Открытие браузера"""
        path_drivers = self.install_driver()
        driver = webdriver.Edge(path_drivers)
        return driver

class Tranlator(Edge):
    def __init__(self, n):
        if n == 0:
            self.url = "https://translate.google.ru/?sl=en&tl=ru&op=translate"
            self.input = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea'
            self.out = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]'
            self.clear = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[1]/div/div/span/button/div[3]'
        else:
            self.url = "https://translate.yandex.ru/?lang=en-ru"
            self.input = '//*[@id="fakeArea"]'
            self.out = '//*[@id="translation"]'
            self.clear = '/html/body/div[1]/main/div[1]/div[1]/div[3]/div[1]/div/div[3]/button'

    def site_translator(self):
        """ Открываем браузер и переходим по URL"""
        driver = self.open_edge()
        driver.get(self.url)
        self.driver = driver
        return self.driver

    def translate(self, text):
        """ Передаем text в переводчик, перед этим обязатлеьно вызвать функцию site_translator"""
        self.driver.find_element(By.XPATH, self.input).send_keys(text)
        sleep(2)
        res = self.driver.find_element(By.XPATH, self.out).text
        self.driver.find_element(By.XPATH, self.clear).click()
        return res
    def closed(self):
        self.driver.close()
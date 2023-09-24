from selenium import webdriver
import time
import allure
from selenium.webdriver.common.keys import Keys


@allure.parent.suite("TEST SBERMARKET")
@allure.suite("TEST YANDEX AND GOOGLE")
class TestSBERMARKETPage:

    @allure.title("Open page from yandex")
    @allure.description("проверяем открытие страницы с яндекса")
    @allure.severity("Critical")
    def test_open_yandex_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ya.ru/")
        time.sleep(5)
        SEARCH_FIELD_YANDEX = self.driver.find_element("xpath", "//input[@class = 'search3__input mini-suggest__input']")
        SEARCH_FIELD_YANDEX.send_keys("sbermarketing")
        FIND_BUTTON = self.driver.find_element("xpath", "//button[text() = 'Найти']").click()

        time.sleep(5)
        assert self.driver.find_element("xpath", "//b[text() = 'SberMarketing.ru']"), "Нет ссылки на СБЕРМАРКЕТИНГ"
        time.sleep(10)

    @allure.title("Open page from google")
    @allure.description("проверяем открытие страницы с гугла")
    @allure.severity("Critical")
    def test_open_google_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.ru/')
        time.sleep(5)
        SEARCH_FIELD_GOOGLE = self.driver.find_element("xpath", "//textarea[@class = 'gLFyf']")
        SEARCH_FIELD_GOOGLE.send_keys("sbermarketing")
        SEARCH_FIELD_GOOGLE.send_keys(Keys.ENTER)
        assert self.driver.find_element("xpath", "//cite[text() = 'https://sbermarketing.ru']")
        time.sleep(5)


    @allure.title("Open page sbermarketing")
    @allure.description("проверяем открытие страницы sbermarketing.ru")
    @allure.severity("Critical")
    def test_open_sbermarketing(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ya.ru/")
        time.sleep(5)
        SEARCH_FIELD_YANDEX = self.driver.find_element("xpath", "//input[@class = 'search3__input mini-suggest__input']")
        SEARCH_FIELD_YANDEX.send_keys("sbermarketing")
        FIND_BUTTON = self.driver.find_element("xpath", "//button[text() = 'Найти']").click()
        SBERMARKETING_LINK = self.driver.find_element("xpath", "//b[text() = 'SberMarketing.ru']").click()
        assert self.driver.title == "СберМаркетинг – технологичный маркетинговый партнер", "Check URL"
        time.sleep(10)

    @allure.title("Open page authorisation")
    @allure.description("проверяем открытие страницы авторизации")
    @allure.severity("Critical")
    def test_log_in_mrm(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://sbermarketing.ru/")
        time.sleep(5)
        ENTER_MRM_BUTTON = self.driver.find_element("xpath", "//div[@class = 'header']//span[@class = 'm-hidden']").click()
        time.sleep(5)
        assert self.driver.title == "Sber-Marketing", "Check AUTH PAGE"
        time.sleep(10)

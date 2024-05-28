import pytest
import allure
from selenium import webdriver
from helpers.test_data import Urls


@allure.step('Открываем браузер Firefox / Открываем страницу Яндекс Самокат / Закрываем браузер')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.HOME_PAGE_URL)
    yield driver
    driver.quit()

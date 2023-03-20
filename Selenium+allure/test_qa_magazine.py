import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_qa():
    """
    Тест-кейс 1
    """
    # Описание опций запуска браузера
    chrome_options = Options()
    chrome_options.add_argument('start-maximized')  # Открываем на полный экран
    chrome_options.add_argument('--disable-infobars')  # Отключаем инфо сообщения
    chrome_options.add_argument('--disable-extentions')  # Отключаем расширения
    # chrome_options.add_argument('--headless')  # Режим "Без браузера"

    # Устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # Запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service = service, options = chrome_options)
    # Определяем адрес страницы для тестирования и переходим на нее
    url = "https://test.qa.studio"
    driver.get(url = url)
    # Ищем по селектору элемент меню "Горячие товары" и кликаем по нему
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()
	# Ищем по XPATH "Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    x_path_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = driver.find_element(By.XPATH, value=x_path_table)
    element.click()
	# Ищем по имени класса артикул для "Журнального столика"
    sku = driver.find_element(By.CLASS_NAME, value="sku")
	# Проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"

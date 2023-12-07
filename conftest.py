import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='module', autouse=True)
def browser_management():

    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options


    browser.open()
    print('Браузер открыт')
    browser.config.base_url = 'https://todomvc.com/examples/'

    yield

    browser.quit()
    print('')
    print('Браузер закрыт')
    print('**Завершение тестирования**')
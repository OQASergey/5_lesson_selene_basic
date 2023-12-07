import pytest
from selene import browser

@pytest.fixture(scope='module', autouse=True)
def browser_management():
    browser.open()
    print('Браузер открыт')
    browser.config.base_url = 'https://todomvc.com/examples/'

    yield

    browser.quit()
    print('Браузер открыт')
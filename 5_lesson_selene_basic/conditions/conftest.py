import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/'

    yield

    browser.quit()
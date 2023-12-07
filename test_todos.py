import pytest
from selene import browser, have, be

def test_start():
    print('Начало теста')

def test_open_todo():
    browser.open('/emberjs/')
    browser.element('[id="new-todo"]').should(be.blank)

def test_complite_todo():
    browser.element('[id="new-todo"]').type('a').press_enter()
    browser.element('[id="new-todo"]').type('b').press_enter()
    browser.element('[id="new-todo"]').type('c').press_enter()
    #browser.all('[id="todo-list"]>li').should(have.size(3))
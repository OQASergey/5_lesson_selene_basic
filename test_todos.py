from selene import browser, have, be

def test_start():
    print('')
    print('**Начало тестирования**')

def test_open_todo():
    browser.open('/emberjs/')
    browser.element('[id="new-todo"]').should(be.blank)

def test_type_todo():
    browser.element('[id="new-todo"]').type('a').press_enter()
    browser.element('[id="new-todo"]').type('b').press_enter()
    browser.element('[id="new-todo"]').type('c').press_enter()

def test_complite():
    browser.all('[id="todo-list"]>li').should(have.size(3))
    browser.all('[id="todo-list"]>li').element_by(have.exact_texts('a', 'b', 'c'))


def test_toggle():
    browser.all('[id="todo-list"]>li').element_by(have.exact_text('c')).element('.toggle').click()

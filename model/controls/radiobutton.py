from selene import have
from selene.support.shared import browser


def select_gender(element, option):
    browser.all(element).element_by(have.value(option)).element('..').click()



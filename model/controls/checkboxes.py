from selene import have
from selene.support.shared import browser


def select_hobby(element, option):
    browser.all(element).element_by(have.text(option)).click()


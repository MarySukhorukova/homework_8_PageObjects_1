from selene import have
from selene.support.shared import browser


def select(element, option):
    browser.element(element).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(option)
    ).click()
from selene import be, have
from selene.support.shared import browser
import os
from selene import command
import tests
from model.controls import dropdown, checkboxes, datepicker, radiobutton


def open_practice_form():
    browser.open('/automation-practice-form')


def type_first_name(first_name):
    browser.element('#firstName').type(first_name)


def type_last_name(last_name):
    browser.element('#lastName').type(last_name)


def type_email(email):
    browser.element('#userEmail').type(email)


def select_gender(gender):
    radiobutton.select_gender('[name=gender]', gender)


def type_phone(phone):
    browser.element('#userNumber').type(phone)


def calendar_click():
    browser.element('#dateOfBirthInput').click()


def select_birthday(month, year, day):
    datepicker.select_date(month, year, day)


def type_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def select_hobby(hobby):
    checkboxes.select_hobby('[for^=hobbies-checkbox]', hobby)


def add_file():
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(tests.__file__), 'files/Pytest_logo.svg.png')))


def type_address(address):
    browser.element('#currentAddress').type(address).perform(command.js.scroll_into_view)


def select_state(state):
    dropdown.select('#state', state)


def select_city(city):
    dropdown.select('#city', city)


def submit_form():
    browser.element('#submit').press_enter()


def should_be_data_in_form(*data):
    browser.element('.table').all('.table td:nth-child(2)').should(have.texts(data))


















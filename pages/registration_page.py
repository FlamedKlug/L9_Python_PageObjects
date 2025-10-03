import inspect
import os
from datetime import date

from selene import browser, have
from Users.User import Gender, Hobbies, User


class RegistrationPage:
    @staticmethod
    def open():
        browser.config.window_height = 2080
        browser.config.window_width = 1920
        browser.open('https://demoqa.com/automation-practice-form')

    @staticmethod
    def _fill_first_name(value):
        browser.element('#firstName').type(value)

    @staticmethod
    def _fill_last_name(value):
        browser.element('#lastName').type(value)

    @staticmethod
    def _fill_email(value):
        browser.element('#userEmail').type(value)

    @staticmethod
    def _fill_gender(test_user_gender: Gender):
        browser.element(test_user_gender.value).click()

    @staticmethod
    def _fill_mobile(value):
        browser.element('#userNumber').type(value)

    @staticmethod
    def _fill_date_of_birth(test_user_birthday: date):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(test_user_birthday.year)
        browser.element('.react-datepicker__month-select').type(test_user_birthday.strftime('%B'))
        browser.element(f'.react-datepicker__day--0{test_user_birthday.day}').click()

    @staticmethod
    def _fill_subjects(value):
        browser.element('#subjectsInput').type(value).press_enter()

    @staticmethod
    def _fill_hobbies(test_user_hobbies: [Hobbies]):
        for user_hobbies in test_user_hobbies:
            browser.element(user_hobbies.value).click()

    @staticmethod
    def _fill_picture(value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(value))

    @staticmethod
    def _fill_current_address(value):
        browser.element('#currentAddress').type(value)

    @staticmethod
    def _fill_state_and_city(state, city):
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()

    @staticmethod
    def _submit_fill_form():
        browser.element('#submit').click()

    @staticmethod
    def _expect_data(name, email, gender, mobile, date_of_birth, subject, hobbies, picture, address, state_and_city):
        browser.element('tbody').all('td').even.should(have.texts(
            name,
            email,
            gender,
            mobile,
            date_of_birth,
            subject,
            hobbies,
            picture,
            address,
            state_and_city
        ))

    def registration(self, test_user: User):
        self._fill_first_name(test_user.first_name)
        self._fill_last_name(test_user.second_name)
        self._fill_email(test_user.email)
        self._fill_gender(test_user.gender)
        self._fill_mobile(test_user.mobile)
        self._fill_date_of_birth(test_user.date_of_birth)
        self._fill_subjects(test_user.subject)
        self._fill_hobbies(test_user.hobbies)
        self._fill_picture(test_user.picture)
        self._fill_current_address(test_user.current_address)
        self._fill_state_and_city(test_user.state, test_user.city)
        self._submit_fill_form()

    def should_have_registered(self, test_user: User):
        self._expect_data(
            f'{test_user.first_name} {test_user.second_name}',
            test_user.email,
            test_user.gender.name,
            str(test_user.mobile),
            test_user.date_of_birth.strftime('%d %B,%Y'),
            test_user.subject,
            ', '.join([i.name for i in test_user.hobbies]),
            test_user.picture,
            test_user.current_address,
            f'{test_user.state} {test_user.city}'
        )

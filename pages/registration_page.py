import os

from selene import browser, have


class RegistrationPage:
    @staticmethod
    def open():
        browser.config.window_height = 2080
        browser.config.window_width = 1920
        browser.open('https://demoqa.com/automation-practice-form')

    @staticmethod
    def fill_first_name(value):
        browser.element('#firstName').type(value)

    @staticmethod
    def fill_last_name(value):
        browser.element('#lastName').type(value)

    @staticmethod
    def fill_email(value):
        browser.element('#userEmail').type(value)

    @staticmethod
    def fill_gender():
        browser.element('[for=gender-radio-1]').click()

    @staticmethod
    def fill_mobile(value):
        browser.element('#userNumber').type(value)

    @staticmethod
    def fill_date_of_birth(year, month,day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}').click()

    @staticmethod
    def fill_subjects(value):
        browser.element('#subjectsInput').type(value).press_enter()

    @staticmethod
    def fill_hobbies():
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()

    @staticmethod
    def fill_picture(value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(value))

    @staticmethod
    def fill_current_address(value):
        browser.element('#currentAddress').type(value)

    @staticmethod
    def fill_state_and_city(state, city):
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()

    @staticmethod
    def submit_fill_form():
        browser.element('#submit').click()

    @staticmethod
    def expect_data(name, email, gender, mobile, date_of_birth, subject, hobbies, picture, address, state_and_city):
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

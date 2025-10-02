import os

from selene import browser, have


def test_filling_form():
    # открытие браузера со страницей формы
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open('https://demoqa.com/automation-practice-form')

    # заполнение формы
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivan.Ivanov@fakemail.org')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('1901')
    browser.element('.react-datepicker__month-select').type('July')
    browser.element('.react-datepicker__day--013').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_jpg.jpg'))
    browser.element('#currentAddress').type('На деревню дедушке')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    # отправка формы
    browser.element('#submit').click()

    # проверка результатов
    browser.element('tbody').all('td').even.should(have.texts(
        'Ivan Ivanov',
        'Ivan.Ivanov@fakemail.org',
        'Male',
        '1234567890',
        '13 July,1901',
        'Computer Science',
        'Sports, Music',
        'test_jpg.jpg',
        'На деревню дедушке',
        'NCR Delhi'
    ))


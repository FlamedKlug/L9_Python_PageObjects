from pages.registration_page import RegistrationPage


def test_filling_form():
    # открытие браузера со страницей формы
    registration_page = RegistrationPage()
    registration_page.open()

    # заполнение формы
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanov')
    registration_page.fill_email('Ivan.Ivanov@fakemail.org')
    registration_page.fill_gender()
    registration_page.fill_mobile('1234567890')
    registration_page.fill_date_of_birth('1901', 'July', '13')
    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies()
    registration_page.fill_picture('test_jpg.jpg')
    registration_page.fill_current_address('На деревню дедушке')
    registration_page.fill_state_and_city('NCR', 'Delhi')

    # отправка формы
    registration_page.submit_fill_form()

    # проверка результатов
    registration_page.expect_data(
        'Ivan Ivanov',
        'Ivan.Ivanov@fakemail.org',
        'Male',
        '1234567890',
        '13 July,1901',
        'Computer Science',
        'Sports, Music',
        'test_jpg.jpg',
        'На деревню дедушке',
        'NCR Delhi')

from datetime import date
from Users.User import User, Gender, Hobbies
from pages.registration_page import RegistrationPage


def test_filling_form(browser_setup):
    test_user = User(first_name='Ivan',
                     second_name='Ivanov',
                     email='Ivan.Ivanov@fakemail.org',
                     gender=Gender.Male,
                     mobile=1234567890,
                     date_of_birth=date(1901, 7, 13),
                     subject='Computer Science',
                     hobbies=[Hobbies.Sports, Hobbies.Music],
                     picture='test_jpg.jpg',
                     current_address='На деревню дедушке',
                     state='NCR',
                     city='Delhi'
                     )

    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.registration(test_user)
    registration_page.should_have_registered(test_user)

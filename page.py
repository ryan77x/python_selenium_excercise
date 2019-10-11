from element import BasePageTextBoxElement
from locators import AdminLoginPageLocators

class UserNameTextElement(BasePageTextBoxElement):
    locator = 'email'

class PasswordTextElement(BasePageTextBoxElement):
    locator = 'password'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class AdminLoginPage(BasePage):
    user_name = UserNameTextElement()
    password = PasswordTextElement()

    def is_title_matches(self):
        return "Login" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_BUTTON)
        element.click()

    def is_login_failed(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_RESULT_ALERT_TEXT)
        return element.text == "Invalid Login Credentials"

    def is_login_email_format_invalid(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_RESULT_ALERT_TEXT)
        return element.text == "The Email field must contain a valid email address."


class AdminPage(BasePage):
    def is_title_matches(self):
        return "Dashboard" in self.driver.title
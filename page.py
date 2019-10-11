from element import BasePageTextBoxElement
from locators import AdminLoginPageLocators

class UserNameTextElement(BasePageTextBoxElement):
    locator = 'email'

class PasswordTextElement(BasePageTextBoxElement):
    locator = 'password'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

class AdminLoginPage(BasePage):
    user_name = UserNameTextElement()
    password = PasswordTextElement()

    def click_login_button(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_BUTTON)
        element.click()

    def get_invalid_login_alert_message(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_RESULT_ALERT_TEXT)
        return element.text

    def get_invalid_email_format_alert_message(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_RESULT_ALERT_TEXT)
        return element.text


class AdminPage(BasePage):
    pass
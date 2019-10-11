from selenium.webdriver.common.by import By

class AdminLoginPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGIN_RESULT_ALERT_TEXT = (By.CSS_SELECTOR, "div.resultlogin")

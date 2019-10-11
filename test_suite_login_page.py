#Author: Rayn Liang

import unittest
from selenium import webdriver
import page
import time

class AdminLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.phptravels.net/admin")

    def test_login_invalid_credential(self):

        admin_login_page = page.AdminLoginPage(self.driver)
        self.login_helper(admin_login_page, "admin@phptravels.com", "badpassword", 2)
        self.assertEqual(admin_login_page.get_invalid_login_alert_message(), "Invalid Login Credentials")

    def test_login_invalid_email_format(self):

        admin_login_page = page.AdminLoginPage(self.driver)
        self.login_helper(admin_login_page, "admin", "demoadmin", 2)
        self.assertEqual(admin_login_page.get_invalid_email_format_alert_message(), "The Email field must contain a valid email address.")

    def test_login_valid_credential(self):

        admin_login_page = page.AdminLoginPage(self.driver)
        self.login_helper(admin_login_page, "admin@phptravels.com", "demoadmin", 2)
        admin_page = page.AdminPage(self.driver)
        self.assertEqual(admin_page.get_page_title(), "Dashboard")
        
    def tearDown(self):
        self.driver.close()

    def login_helper(self, admin_login_page, user_name, password, sleep_time):

        self.assertEqual(admin_login_page.get_page_title(), "Administator Login")
        admin_login_page.user_name = user_name
        admin_login_page.password = password
        admin_login_page.click_login_button()
        time.sleep(sleep_time)

suite = unittest.TestLoader().loadTestsFromTestCase(AdminLogin)
unittest.TextTestRunner(verbosity=2).run(suite)
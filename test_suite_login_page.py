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
        self.assertTrue(admin_login_page.is_login_failed())

    def test_login_invalid_email_format(self):

        admin_login_page = page.AdminLoginPage(self.driver)
        self.login_helper(admin_login_page, "admin", "demoadmin", 2)
        self.assertTrue(admin_login_page.is_login_email_format_invalid())

    def test_login_valid_credential(self):

        admin_login_page = page.AdminLoginPage(self.driver)
        self.login_helper(admin_login_page, "admin@phptravels.com", "demoadmin", 2)
        admin_page = page.AdminPage(self.driver)
        self.assertTrue(admin_page.is_title_matches())
        
    def tearDown(self):
        self.driver.close()

    def login_helper(self, admin_login_page, user_name, password, sleep_time):

        self.assertTrue(admin_login_page.is_title_matches())
        admin_login_page.user_name = user_name
        admin_login_page.password = password
        admin_login_page.click_login_button()
        time.sleep(sleep_time)

suite = unittest.TestLoader().loadTestsFromTestCase(AdminLogin)
unittest.TextTestRunner(verbosity=2).run(suite)
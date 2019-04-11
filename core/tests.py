from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class WebLiveTestCase(LiveServerTestCase):
    port = 9696

    def setUp(self):
        self.browser = WebDriver()
        self.url = 'http://127.0.0.1:9696'
        print(self.live_server_url)
        super(WebLiveTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(WebLiveTestCase, self).tearDown()

    def test_admin(self):
        browser = self.browser
        url = '{}/admin/login/?next=/admin/'.format(self.url)
        print(url)
        # Opening the link we want to test
        browser.get(url)
        print(browser.title)
        assert 'Django' in browser.title

    def test_api_auth_in(self):
        browser = self.browser
        url = '{}/api-auth/login/'.format(self.url)
        browser.get(url)
        print(browser.title)
        assert 'REST' in browser.title

    def test_api_auth_out(self):
        browser = self.browser
        url = '{}/api-auth/logout/'.format(self.url)
        browser.get(url)
        print(browser.title)
        assert 'Log in again' in browser.page_source
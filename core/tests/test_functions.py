from django.test import LiveServerTestCase
from django.urls import reverse_lazy, reverse
# from rest_framework.reverse import reverse, reverse_lazy
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class WebLiveTestCase(LiveServerTestCase):
    port = 9696

    def setUp(self):
        self.browser = WebDriver()
        self.url = 'http://127.0.0.1:9696'
        super(WebLiveTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(WebLiveTestCase, self).tearDown()

    def test_admin(self):
        browser = self.browser
        url = '{}{}'.format(self.url, reverse_lazy('admin:login'))
        print(url)
        # Opening the link we want to test
        browser.get(url)
        print(browser.title)
        assert 'admin' in browser.title

    def test_api_auth_in(self):
        browser = self.browser
        print(reverse_lazy('rest_framework:login'))
        url = '{}{}'.format(self.url, reverse_lazy('rest_framework:login'))
        browser.get(url)
        print(browser.title)
        assert 'REST' in browser.title

    def test_api_auth_out(self):
        browser = self.browser
        url = '{}{}'.format(self.url, reverse_lazy('rest_framework:logout'))
        browser.get(url)
        print(browser.title)
        assert 'out' in browser.title

    def test_ping(self):
        browser = self.browser
        url = '{}{}'.format(self.url, reverse_lazy('ping'))
        browser.get(url)
        print(browser)

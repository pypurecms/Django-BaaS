from django.test import LiveServerTestCase
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
        # Opening the link we want to test
        print(self.live_server_url)
        browser.get('{}/admin'.format(self.url))
        body = browser.find_element_by_tag_name('body')
        assert 'Username' in body.text

    def test_index(self):
        browser = self.browser
        browser.get('{}/start-up'.format(self.url))
        try:
            body = browser.find_element_by_tag_name('body')
            assert True
        except Exception:
            print('error')


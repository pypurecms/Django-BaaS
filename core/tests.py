from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class WebLiveTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = WebDriver()
        super(WebLiveTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(WebLiveTestCase, self).tearDown()

    def test_admin(self):
        browser = self.browser
        # Opening the link we want to test
        print(self.live_server_url)
        browser.get('{}/admin'.format(self.live_server_url))
        body = browser.find_element_by_tag_name('body')
        assert 'Username' in body.text

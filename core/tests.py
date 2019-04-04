from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WebLiveTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        super(WebLiveTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(WebLiveTestCase, self).tearDown()

    def test_register(self):
        browser = self.browser
        # Opening the link we want to test
        browser.get('http://127.0.0.1:8000')
        body = browser.find_element_by_tag_name('body')
        assert 'Django' in body.text

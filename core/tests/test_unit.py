from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class DummyTestCase(TestCase):

    def test_math(self):
        self.assertEqual(1 + 1, 2)


class BaseEndpointTestCase(APITestCase):

    def the_setup(self, url_name):
        self.url_name = url_name

    def list_case(self):
        url = reverse(self.url_name)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results', [])), 0)


class HumansTestCase(BaseEndpointTestCase):

    def setUp(self):
        self.the_setup('humans-list')
        super(HumansTestCase, self).setUp()

    def test_list_case(self):
        self.list_case()


class UsersTestCase(BaseEndpointTestCase):
    def setUp(self):
        self.the_setup('users-list')
        super(UsersTestCase, self).setUp()

    def test_list_case(self):
        url = reverse(self.url_name)
        response = self.client.get(url, format='json')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

class DummyTestCase(TestCase):

    def test_math(self):
        self.assertEqual(1+1, 2)

class MansTestCase(APITestCase):

    def test_man_list(self):
        url = reverse('humans-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results', [])), 0)
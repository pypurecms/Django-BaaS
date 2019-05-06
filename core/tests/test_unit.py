from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from model_mommy import mommy
from ..models import Human, Child, Parent, Sibling, Avatar, User
from ..utils import get_enabled


class DummyTestCase(TestCase):

    def test_math(self):
        self.assertEqual(1 + 1, 2)


class HumanTestCase(APITestCase):

    def setUp(self):
        self.endpoint_enabled = get_enabled('human')
        self.the_setup('humans', obj=Human)

    def tearDown(self):
        super(HumanTestCase, self).tearDown()

    def the_setup(self, base_name, obj):
        if self.endpoint_enabled:
            self.base_name = base_name
            self.password = 'password1'
            self.user1 = mommy.make(User, username='user1')
            self.user2 = mommy.make(User, username='user2')
            self.user1.is_staff = True
            self.user1.set_password(self.password)
            self.user1.save()
            self.objs = []
            for i in range(3):
                self.objs.append(mommy.make(obj, name='1-name-{}'.format(i), user=self.user1))
            for i in range(2):
                self.objs.append(mommy.make(obj, name='2-name-{}'.format(i), user=self.user2))
        super(HumanTestCase, self).setUp()

    def test_list_without_auth(self):
        if self.endpoint_enabled:
            url = reverse('{}-list'.format(self.base_name))
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_with_staff_auth(self):
        if self.endpoint_enabled:
            url = reverse('{}-list'.format(self.base_name))
            self.client.login(username=self.user1.username, password=self.password)
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(3 + 2, response.data.get('count'), response.data)
            self.client.logout()

    def test_list_with_user_auth(self):
        if self.endpoint_enabled:
            url = reverse('{}-list'.format(self.base_name))
            self.user1.is_staff = False
            self.user1.save()
            self.client.login(username=self.user1.username, password=self.password)
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
            self.client.logout()

    def test_list_mine_with_user_auth(self):
        if self.endpoint_enabled:
            url = reverse('{}-list-mine'.format(self.base_name))
            # function name list_mine but here it is list-mine
            self.user1.is_staff = False
            self.user1.save()
            self.client.login(username=self.user1.username, password=self.password)
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(3, response.data.get('count'), response.data)
            self.client.logout()


class ChildTestCase(HumanTestCase):
    def setUp(self):
        self.endpoint_enabled = get_enabled('child')
        self.the_setup('children', obj=Child)


class AvatarTestCase(HumanTestCase):
    def setUp(self):
        self.endpoint_enabled = get_enabled('avatar')
        self.the_setup('avatars', obj=Avatar)


class ParentTestCase(HumanTestCase):
    def setUp(self):
        self.endpoint_enabled = get_enabled('parent')
        self.the_setup('parents', obj=Parent)

    def test_list_with_user_auth(self):
        if self.endpoint_enabled:
            url = reverse('{}-list'.format(self.base_name))
            self.user1.is_staff = False
            self.user1.save()
            self.client.login(username=self.user1.username, password=self.password)
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.client.logout()


class SiblingTestCase(ParentTestCase):
    def setUp(self):
        self.endpoint_enabled = get_enabled('sibling')
        self.the_setup('siblings', obj=Sibling)

from django.test import TestCase
from model_mommy import mommy
from ..models import Human, Child, Parent, Sibling, Avatar, User


class BaseModelTestCase(TestCase):
    def setUp(self):
        self.user1 = mommy.make(User, username='user1')
        self.user2 = mommy.make(User, username='user2')

        self.parent = mommy.make(Parent, name='Category1')
        self.human = mommy.make(Human, user=self.user1, parent=self.parent)
        self.childs = mommy.make(Child, name="comment", human=self.human, _quantity=3, user=self.user2)

        ## make 5 siblings for the human
        mommy.make(Sibling, _quantity=5, humans=[self.human.id])
        self.avatar = mommy.make(Avatar, name='page', human=self.human)

    def tearDown(self):
        pass

class ModelsBaseTestCase(BaseModelTestCase):

    def setUp(self):
        super(ModelsBaseTestCase, self).setUp()

    def test_instance(self):
        self.assertTrue(isinstance(self.human, Human))
        self.assertEqual(self.childs[2].human.name, self.human.name)
        self.assertEqual(self.human.parent.name, 'Category1')
        self.assertEqual(len(self.human.siblings.all()), 5)
        self.assertEqual(self.human.avatar, self.avatar)
        self.assertEqual(self.human.user, self.user1)
        self.assertEqual(self.childs[0].user, self.user2)

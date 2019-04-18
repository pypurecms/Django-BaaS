from django.test import TestCase

#Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# Relative imports of the 'app-name' package
from core.models import Human, Child, Parent, Sibling, Avatar

class ManTestCase(TestCase):

    def setUp(self):
        self.human=mommy.make(Human)
        self.childs = mommy.make(Child, human=self.human, _quantity=3)
        self.parent = mommy.make(Parent, name='Category1')
        mommy.make(Sibling, _quantity=5, humans=[self.human.id])
        self.human.parent=self.parent
        self.human.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.human, Human))
        self.assertEqual(self.childs[2].human.name, self.human.name)
        self.assertEqual(self.human.parent.name, 'Category1')
        self.assertEqual(len(self.human.siblings.all()), 5)

from django.test import TestCase

#Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# Relative imports of the 'app-name' package
from core.models import Human, Child, Parent, Sibling, Avatar

class ManTestCase(TestCase):

    def setUp(self):
        self.man=mommy.make(Human)
        self.childs = mommy.make(Child, man=self.man, _quantity=3)
        self.parent = mommy.make(Parent, name='Category1')
        mommy.make(Sibling, _quantity=5, mans=[self.man.id])
        self.man.parent=self.parent
        self.man.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.man, Human))
        self.assertEqual(self.childs[2].man.name, self.man.name)
        self.assertEqual(self.man.parent.name, 'Category1')
        self.assertEqual(len(self.man.siblings.all()), 5)

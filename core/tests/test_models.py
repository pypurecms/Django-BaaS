from django.test import TestCase

#Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# Relative imports of the 'app-name' package
from core.models import Man, Child

class ManTestCase(TestCase):

    def setUp(self):
        self.man=mommy.make(Man)
        self.childs = mommy.make(Child, man=self.man, _quantity=3)

    def test_instance(self):
        self.assertTrue(isinstance(self.man, Man))
        self.assertEqual(self.childs[2].man.name, self.man.name)

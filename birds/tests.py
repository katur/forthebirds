from django.test import TestCase

from birds.models import Species


class BirdsTestCase(TestCase):
    def setUp(self):
        Species.objects.create(

    def test_one_plus_one(self):
        self.assertTrue(2 == 1 + 1)

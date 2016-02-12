from django.test import TestCase


class BirdsTestCase(TestCase):
    def test_one_plus_one(self):
        self.assertTrue(2 == 1 + 1)

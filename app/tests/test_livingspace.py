import unittest
from app.livingspace import LivingSpace


class TestLivingSpace(unittest.TestCase):
    def test_if_livingspace_inherits(self):
        self.assertTrue(issubclass(LivingSpace, object))

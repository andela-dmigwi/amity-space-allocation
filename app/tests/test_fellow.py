import unittest
from app.fellow import Fellow


class TestFellow(unittest.TestCase):
    def test_if_fellow_inherits(self):
        self.assertTrue(issubclass(Fellow, object))

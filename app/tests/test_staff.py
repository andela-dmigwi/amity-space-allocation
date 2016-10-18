import unittest
from app.staff import Staff


class TestStaff(unittest.TestCase):
    def test_if_staff_class_inherits(self):
        self.assertTrue(issubclass(Staff, object))

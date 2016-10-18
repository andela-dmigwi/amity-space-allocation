import unittest
from app.office import Office


class TestOffice(unittest.TestCase):
    def test_if_office_inherits(self):
        self.assertTrue(issubclass(Office, object))

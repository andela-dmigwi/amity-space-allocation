import unittest
from app.fellow import Fellow

class TestFellow(unittest.TestCase):
    def setUp(self):
        self.fellow  = Fellow()

    def test_add_fellow(self):
        fw = self.fellow.add_fellow(person_name='Jackline Kimani', person_id=9)
        self.assertEqual(fw, {'Jackline Kimani':9})

    def test_add_fellow(self):
        fw = self.fellow.add_fellow(person_name='Dennis Okari', person_id=11)
        self.assertEqual(fw, {'Dennis Okari':11})

    #test if person_name is empty
    def test_add_empty_name(self):
        fw = self.fellow.add_fellow(person_name='', person_id=9)
        self.assertEqual(fw, 'person_name is too short')

    #test if person_name is too long(longer than 20 characters)
    def test_add_too_long_name(self):
        person_name = 'This is a very long, very long, long name'
        fw = self.fellow.add_fellow(person_name, person_id=9)
        self.assertEqual(fw, 'person_name is too long')

    #test invalid person_id
    def test_invalid_person_id(self):       
        fw = self.fellow.add_fellow(person_name='Lewis', person_id='10')
        self.assertEqual(fw, 'Id should an Int')

    def test_invalid_person_id(self):       
        fw = self.fellow.add_fellow(person_name='Lewis', person_id= 700000000000)
        self.assertEqual(fw, 'Id not found')

    #test invalid person_name
    def test_invalid_person_id(self):       
        fw = self.fellow.add_fellow(person_name=['Lewis'], person_id= 7)
        self.assertEqual(fw, 'Invalid name type')

    def test_delete_fellow(self):        
        self.assertEqual(self.fellow.delete_fellow(person_id = 9), 'Delete Successful')

    def test_delete_fellow_not_available(self):
        person_id = 27000000000
        self.assertEqual(self.fellow.delete_fellow(person_id), 'Id not found')

    def test_delete_incorrect_fellow_id(self):
        person_id = '9wwddw'
        self.assertEqual(self.fellow.delete_fellow(person_id), 'Id should be an Int')

    def test_delete_incorrect_fellow_id(self):       
        self.assertEqual(self.fellow.delete_fellow({9}), 'Id should be an Int')

    def test_delete_incorrect_fellow_id(self):   
        self.assertEqual(self.fellow.delete_fellow({'Id':9}), 'Id should be an Int')

    def test_assign_level(self):
        al = self.fellow.assign_level(person_id = 11, level='D0A')
        self.assertEqual(al,'Dennis Okari assigned level D0A')

    def test_assign_invalid_id(self):
        al = self.fellow.assign_level(person_id='xx', level = 'D1')
        self.assertEqual(al, 'xx is not an id')

    def test_assign_invalid_level(self):
        res = self.fellow.assign_level(person_id=11, level='samurai')
        self.assertEqual(res, 'samurai is not an accepted level')
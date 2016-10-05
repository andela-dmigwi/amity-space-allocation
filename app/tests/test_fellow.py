import unittest
from app.fellow import Fellow

class TestFellow(unittest.TestCase):
    def setUp(self):
        self.fellow  = Fellow({})    

    def test_add_fellow(self):
        fw = self.fellow.add_fellow(person_name='Dennis Okari')
        self.assertTrue(fw)

    #test if person_name is empty
    def test_add_empty_name(self):
        fw = self.fellow.add_fellow(person_name='')
        self.assertEqual(fw, 'Invalid Person name used')

    #test if person_name is too long(longer than 20 characters)
    def test_add_too_long_name(self):        
        fw = self.fellow.add_fellow(person_name = 'This is a very long, very long, long name')
        self.assertEqual(fw, 'Person Name is too long')   

    #test invalid person_name
    def test_invalid_person_name(self):       
        fw = self.fellow.add_fellow(person_name=['Lewis'])
        self.assertEqual(fw, 'Invalid name type')

    def test_delete_fellow(self):   
        self.fellow.add_fellow(person_name='Stephen Njoroge')     
        self.assertTrue(self.fellow.delete_fellow(person_name='Stephen Njoroge'))

    def test_delete_fellow_not_available(self):
        self.assertEqual(self.fellow.delete_fellow(person_name='Barrack Obama'), 
            'Barrack Obama not found')    
import unittest
from app.staff import Staff

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff = Staff()
        
    def test_add(self):
        name = self.staff.add_staff('Fally Ipupa')
        self.assertTrue(name)
    
    # Test empty name
    def test_add_empty_name(self):
        self.assertEqual(self.staff.add_staff(''), 'Invalid Staff name type')

    #Test name longer than expected (Longer than 20 characters)
    def test_add_too_long_name(self):
        name = 'Ezekiel Adebayo Mabukoroje'
        self.assertEqual(self.staff.add_staff(name), 'Too long Staff name') 

       #Type of name passed
    def test_add_list_type_name(self):
        self.assertEqual(self.staff.add_staff(['Fally Ipupa']), 'Invalid Staff name type')

    def test_delete_staff(self):  
        self.staff.add_staff('Edward King')      
        self.assertTrue(self.staff.delete_staff(person_name = 'Edward King'))

    def test_delete_staff_not_available(self):
        self.assertEqual(self.staff.delete_staff(person_name = 'Larry King'),
            'Larry King not found')
    
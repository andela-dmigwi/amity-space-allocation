import unittest
from app.staff import Staff

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff = Staff()
        
    def test_add(self):
        name = self.staff.add_staff('Fally Ipupa',person_id=20)
        self.assertEqual(name, {'Fally Ipupa':20}) 

    # Test empty name
    def test_add_empty_name(self):
        self.assertEqual(self.staff.add_staff('', person_id=20), 'Too short name')

    #Test name longer than expected (Longer than 20 characters)
    def test_add_too_long_name(self):
        name = 'Ezekiel Adebayo Mabukoroje'
        self.assertEqual(self.staff.add_staff(name, person_id=21), 'Too long name') 

    # Test invalid type of person_id
    def test_add_empty_name(self):
        self.assertEqual(self.staff.add_staff('Migwi Ndung\'u',person_id='2'), 'person id should be an int')

        #Type of name passed
    def test_add_list_type_name(self):
        self.assertEqual(self.staff.add_staff(['Fally Ipupa'], 20), 'Invalid name type')

    def test_add_dict_type_name(self):
        name = self.staff.add_staff({'name':'Fally Ipupa'} ,20)
        self.assertEqual(name, 'Invalid name type')     

    def test_delete_staff(self):        
        self.assertEqual(self.staff.delete_staff(person_id = 20), 'Delete Successful')

    def test_delete_staff_not_available(self):
        person_id = 2000000000
        self.assertEqual(self.staff.delete_staff(person_id), 'Id not found')

    def test_delete_incorrect_staff_id(self):
        person_id = '2wwddw'
        self.assertEqual(self.staff.delete_staff(person_id), 'Id should be an Int')

    def test_delete_incorrect_staff_id(self):       
        self.assertEqual(self.staff.delete_staff({20}), 'Id should be an Int')

    def test_delete_incorrect_staff_id(self):   
        self.assertEqual(self.staff.delete_staff({'Id':20}), 'Id should be an Int')

    def test_assign_department(self):
        dept = 'SS'
        self.assertEqual(self.staff.assign_department(dept), 'Fally Ipupa assigned '+
            'Support Staff Department')

    def test_assign_department_not_available(self):
        dept = "DA"
        self.assertEqual(self.staff.assign_department(dept), 'That department doesn\'t exist')
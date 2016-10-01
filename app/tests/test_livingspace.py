import unittest
from app.livingspace import LivingSpace
from app.fellow import Fellow
from app.staff import Staff

class TestLivingSpace(unittest.TestCase):
    def setUp(self):
        self.living = LivingSpace()
        self.fellow = Fellow()
        self.staff = Staff()
        
    def test_allocate_livingspace(self):
        self.fellow.add_fellow(person_name="Elias Kanyi")
        ls = self.living.allocate_livingspace(room_name='Valhala', person_name="Elias Kanyi")
        self.assertTrue(ls)

    def test_allocate_staff_livingspace(self):
        self.staff.add_staff(person_name="Judy Wakhungu")
        ls = self.living.allocate_livingspace(room_name='Valhala', person_name="Elias Kanyi")
        self.assertEqual(ls, 'Staff cannot have accomodation')

    def test_allocate_livingspace_again(self):
        ls = self.living.allocate_livingspace(room_name='Valhala', person_name="Elias Kanyi")
        self.assertEqual(ls, '"Elias Kanyi has a livingspace already')

    def test_recall_allocated_livingspace(self):
        ls = self.living.recall_allocated_livingspace(person_name="Elias Kanyi")
        self.assertEqual(ls, 'Room has been recalled')

    def test_recall_allocated_livingspace_again(self):
        ls = self.living.recall_allocated_livingspace(person_name="Elias Kanyi") 
        self.assertEqual(ls, '"Elias Kanyi not found')

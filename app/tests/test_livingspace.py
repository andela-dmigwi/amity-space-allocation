import unittest
from app.livingspace import LivingSpace
from app.fellow import Fellow
from app.staff import Staff
from app.room import Room

class TestLivingSpace(unittest.TestCase):
    def setUp(self):
        self.living = LivingSpace({})
        self.fellow = Fellow({})
        self.staff = Staff([])
        self.rm = Room()
        
    def test_allocate_livingspace(self):
        self.fellow.add_fellow(person_name="Elias Kanyi")
        ls = self.living.allocate_livingspace(person_name="Elias Kanyi")
        self.assertTrue(ls)

    def test_allocate_staff_livingspace(self):
        self.staff.add_staff(person_name="Judy Wakhungu")
        ls = self.living.allocate_livingspace(person_name="Elias Kanyi")
        self.assertEqual(ls, 'Only A fellow who can get Accomodation')

    def test_allocate_livingspace_again(self):
        ls = self.living.allocate_livingspace(person_name="Elias Kanyi")
        self.assertEqual(ls, '"Elias Kanyi has a livingspace already')

    def test_reallocate_livingspace(self):
        self.rm.create_room(room_name='Valhala', room_type='Livingspace')
        ls = self.living.reallocate_livingspace(person_name="Elias Kanyi", room_name='Valhala')
        self.assertTrue(ls)

    def test_reallocate_livingspace_not_available(self):
        ls = self.living.reallocate_livingspace(person_name="Elias Kanyi", room_name='Ambercrombie')
        self.assertTrue(ls, 'Ambercrombie does not exist')

    def test_recall_allocated_livingspace(self):
        ls = self.living.recall_allocated_livingspace(person_name="Elias Kanyi")
        self.assertTrue(ls)

    def test_recall_allocated_livingspace_again(self):
        ls = self.living.recall_allocated_livingspace(person_name="Elias Kanyi") 
        self.assertEqual(ls, '"Elias Kanyi not found')
import unittest
from app.livingspace import LivingSpace
from mock import patch


class TestLivingSpace(unittest.TestCase):
    def setUp(self):
        self.living = LivingSpace({})

    @patch.object('app.fellow.Fellow.fellow_names', ["Elias Kanyi"])
    def test_allocate_livingspace(self):
        ls = self.living.allocate_livingspace(person_name="Elias Kanyi")
        self.assertTrue(ls)

    def test_allocate_staff_livingspace(self):
        ls = self.living.allocate_livingspace(person_name="Elias Kanyi")
        self.assertEqual(ls, 'Only A fellow who can get Accomodation')

    @patch.dict('app.livingspace.LivingSpace.room_n_occupants',
                {'rm': ["Elias Kanyi"]})
    @patch.object('app.fellow.Fellow.fellow_names', ["Elias Kanyi"])
    def test_allocate_livingspace_again(self):
        ls = self.living.allocate_livingspace(person_name="Elias Kanyi")
        self.assertEqual(ls, '"Elias Kanyi has a livingspace already')

    @patch.dict('app.livingspace.LivingSpace.room_n_occupants',
                {'Valhala': []})
    def test_reallocate_livingspace(self):
        ls = self.living.reallocate_livingspace(
            person_name="Elias Kanyi", room_name='Valhala')
        self.assertTrue(ls)

    def test_reallocate_livingspace_not_available(self):
        ls = self.living.reallocate_livingspace(
            person_name="Elias Kanyi", room_name='Ambercrombie')
        self.assertTrue(ls, 'Ambercrombie does not exist')

    @patch.dict('app.livingspace.LivingSpace.room_n_occupants',
                {'rm': ["Elias Kanyi"]})
    def test_recall_allocated_livingspace(self):
        ls = self.living.recall_allocated_livingspace(
            person_name="Elias Kanyi")
        self.assertTrue(ls)

    def test_recall_allocated_livingspace_again(self):
        ls = self.living.recall_allocated_livingspace(
            person_name="Elias Kanyi")
        self.assertEqual(ls, 'Elias Kanyi not found')

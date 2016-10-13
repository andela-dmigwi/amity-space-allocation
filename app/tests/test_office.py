import unittest
from app.office import Office

from mock import patch


class TestOffice(unittest.TestCase):
    def setUp(self):
        self.office = Office({})

    @patch.object('app.staff.Staff.staff_names', ["Millicent Awis", "Jumbo juniuo"])
    def test_allocate_office(self):
        ls = self.office.allocate_office(person_name="Millicent Awis")
        self.assertTrue(ls)

        ls = self.office.allocate_office(person_name='Wikister Nyabwa')
        self.assertEqual(
            ls, 'Only staff and fellows that can be allocated livingspace')

        self.office.allocate_office(person_name="Jumbo juniuo")

        ls = self.office.allocate_office(person_name="Jumbo juniuo")
        self.assertEqual(ls, 'Jumbo juniuo has an Office already')

    @patch.object('app.fellow.Fellow.fellow_names', ['Patrick Njiru'])
    @patch.dict('app.office.Office.office_n_occupants', {'Valhala': []})
    def test_reallocate_office(self):
        res = self.office.reallocate_office(
            person_name='Patrick Njiru', room_name='Valhala')
        self.assertTrue(res)

        es = self.office.reallocate_office(
            person_name='Patrick Njiru', room_name='Kalahari')
        self.assertEqual(es, 'kalahari is not an office')

        es = self.office.reallocate_office(
            person_name='Patrice Njiru', room_name='Valhala')
        self.assertEqual(es, 'Patrice Njiru is not a fellow or a staff')

    @patch.object('app.fellow.Fellow.fellow_names', ['Jumbo juniuo'])
    def test_recall_allocated_office(self):
        ls = self.office.recall_allocated_office(person_name="Jumbo juniuo")
        self.assertTrue(ls)

    def test_recall_allocated_office_again(self):
        ls = self.office.recall_allocated_office(person_name="Jumbo juniuo")
        self.assertEqual(ls, 'Jumbo juniuo not found')

    def test_get_assigned_room(self):
        ret_val = self.office.get_assigned_room('Kimani')
        self.assertEqual(ret_val, 'None')

import unittest
from app.person import Person
from unittest.mock import patch


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person()

    # test add fellow who doesn't need living space or office
    @patch('app.person.Person.add')
    @patch('app.fellow.Fellow.fellow_names')
    @patch('app.room.Room.allocate_space')
    def test_add_fellow_who_dont_need_room(self, mock_allocate_space,
                                           mock_fellow_names, mock_add):
        mock_fellow_names.__iter__.return_value = []
        mock_allocate_space.return_value = """Kimani Ndegwa has been allocated Office:"""
        mock_add.return_value = True
        pers = self.person.add_person(person_name='Kimani Ndegwa',
                                      type_person='fellow',
                                      want_accomodation='n')
        self.assertIn('Kimani Ndegwa has been allocated Office:', pers)

    @patch('app.room.Room.get_room')
    @patch('app.person.Person.add')
    @patch('app.room.Room.allocate_space')
    @patch('app.staff.Staff.staff_names')
    def test_add_staff(self, mock_staff_names, mock_allocate_space,
                       mock_add, mock_get_room):
        mock_staff_names.__iter__.return_value = []
        mock_allocate_space.return_value = True
        mock_add.return_value = True
        mock_get_room.return_value = ' HAIL CESEAR!!'
        pers = self.person.add_person(person_name='Garbriel Mwata',
                                      type_person='staff',
                                      want_accomodation='n')
        self.assertIn('Allocated Office: HAIL CESEAR!!', pers)

    # test add staff and assign them livingspace
    def test_add_staff_assign_livingspace(self):
        pers = self.person.add_person(person_name='Njira', type_person='staff',
                                      want_accomodation='y')
        self.assertEqual(pers, 'staff cannot have accomodation')

    @patch('app.staff.Staff.staff_names')
    def test_add_two_people_who_share_name(self, mock_staff_names):
        mock_staff_names.__iter__.return_value = ['Joshua']
        pers = self.person.add_person(
            person_name='Joshua', type_person='staff')
        self.assertEqual(pers, 'Joshua already exists')

    @patch.dict('app.office.Office.office_n_occupants', {'Rm': ['we', 'ty']})
    def test_get_room_members(self):
        rm = self.person.get_room_members(room_name='Rm')
        self.assertEqual(rm, ['we', 'ty'])

import unittest
from app.person import Person
from unittest.mock import patch


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person()

    # test add fellow who doesn't need living space or office
    @patch('app.fellow.Fellow.add_fellow')
    @patch('app.office.Office.allocate_office')
    def test_add_fellow_who_dont_need_room(self, mock_add_fellow,
                                           mock_allocate_office):
        mock_add_fellow.return_value = True
        mock_allocate_office.return_value = True
        pers = self.person.add_person(person_name='Kimani Ndegwa',
                                      type_person='fellow',
                                      want_accomodation='n')
        self.assertIn('You have been allocated Office:', pers)

    @patch('app.staff.Staff.add_staff')
    @patch('app.office.Office.allocate_office')
    @patch('app.livingspace.LivingSpace.allocate_livingspace')
    def test_add_staff(self, mock_add_staff, mock_allocate_office,
                       mock_allocate_livingspace):
        mock_add_staff.return_value = True
        mock_allocate_office.return_value = True
        mock_allocate_office.return_value = True
        pers = self.person.add_person(person_name='Garbriel Mwata',
                                      type_person='staff',
                                      want_accomodation='n')
        self.assertIn('You have been allocated Office:', pers)

    # test add staff and assign them livingspace
    def test_add_staff_assign_livingspace(self):
        pers = self.person.add_person(person_name='Njira', type_person='staff',
                                      want_accomodation='y')
        self.assertEqual(pers, 'staff cannot have accomodation')

    @patch.object('app.staff.Staff.staff_name', ['Joshua'])
    def test_add_two_people_who_share_name(self):
        pers = self.person.add_person(
            person_name='Joshua', type_person='staff')
        self.assertEqual(pers, 'Joshua already exists')

    @patch.object('app.staff.Staff.staff_names', ["James Ndiga"])
    @patch('app.office.Office.office_n_occupants', {'Valhala': []})
    def test_reallocate_person(self, mock_staff, mock_room):
        pers = self.person.reallocate_person(
            room_name='Valhala', person_name='James Ndiga')
        self.assertTrue(pers)

    # test if staff can be assigned livingspace
    @patch.dict('app.livingspace.LivingSpace.room_n_occupants', {'Dojo': []})
    @patch.object('app.staff.Staff.staff_names', ["James Ndiga"])
    def test_if_staff_is_assigned_livingspace(self):
        pers = self.person.reallocate_person(
            person_name='James Ndiga', room_name='Dojo')
        self.assertEqual(pers, 'staff cannot have accomodation')

    # test if fellow can assigned office and livingspace
    @patch.object('app.fellow.Fellow.fellow_names', ['Stanley Ndiga'])
    def test_if_fellow_is_assigned_office_n_livingspace(self):
        person_name = 'Stanley Ndiga'
        pers_1 = self.person.reallocate_person(person_name, 'Dojo')
        pers_2 = self.person.reallocate_person(person_name, 'Valhala')

        self.assertEqual([pers_2, pers_1], [True, True])

    @patch.dict('app.office.Office.office_n_occupants', {'Krypton': []})
    @patch.object('app.staff.Staff.staff_names', ["Zuckerberg"])
    def test_if_staff_is_assigned_2_officespace(self):
        '''staff will hold last room assigned to him /her'''
        person_name = 'Zuckerberg'
        self.person.reallocate_person(person_name, room_name='Valhala')
        self.person.reallocate_person(person_name, room_name='Krypton')

        rm1 = self.person.get_room_members('Valhala')
        rm2 = self.person.get_room_members('Krypton')

        self.assertEqual(
            ['Zuckerberg' in rm1, 'Zuckerberg' in rm2], [False, True])

    @patch.dict('app.livingspace.LivingSpace.room_n_occupants', {'Amity': []})
    @patch.object('app.fellow.Fellow.fellow_names', ['Sass'])
    def test_if_fellow_is_assigned_2_livingspaces(self):
        '''fellow will hold last room assigned to him /her'''

        person_name = 'Sass'
        self.person.reallocate_person(person_name, room_name='Amity')
        self.person.reallocate_person(person_name, room_name='Dojo')

        rm1 = self.person.get_room_members('Amity')
        rm2 = self.person.get_room_members('Dojo')

        self.assertEqual(
            ['Sass' in rm1, 'Sass' in rm2], [True, False])

    @patch.dict('app.office.Office.office_n_occupants', {'Rm': ['we', 'ty']})
    def test_get_room_members(self):
        rm = self.person.get_room_members(room_name='Rm')
        self.assertEqual(rm, ['we', 'ty'])

import unittest
from app.room import Room
from mock import patch


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room()

    @patch.dict('app.office.Office.office_n_occupants', {"Dojo": []})
    def test_create_room(self):
        res = self.room.create_room(room_name='Valhala', room_type='office')
        self.assertEqual(res, 'Valhala was created as an Office')

        # create duplicate room (With same name)
    @patch.dict('app.office.Office.office_n_occupants', {"Dojo": []})
    @patch.dict('app.livingspace.LivingSpace.room_n_occupants',
                {"Valhala": []})
    def test_create_duplicate_room(self):
        res = self.room.create_room(
            room_name='Valhala', room_type='LivingSpace')
        self.assertEqual(res, 'Valhala already exists ')

        # create a room without a name
    def test_create_room_without_name(self):
        res = self.room.create_room(room_name='', room_type='Office')
        self.assertEqual(res, 'Room name used is invalid')

        # create type of room not available
    def test_create_room_type_not_available(self):
        res = self.room.create_room(room_name='Valhala', room_type='game room')
        self.assertEqual(
            res, "Create a room of type 'LivingSpace' or 'Office'  ONLY!")

    @patch('app.room.Room.randomly_allocate_rooms')
    @patch('app.room.Room.get_room')
    @patch('app.fellow.Fellow.fellow_names')
    def test_allocate_space(self, mock_fellow_names, mock_get_room,
                            mock_randomly_allocate_rooms):
        mock_fellow_names.__iter__.return_value = ['Gaamuwa']
        mock_randomly_allocate_rooms.return_value = True
        mock_get_room.return_value = 'None'
        value = self.room.allocate_space('Gaamuwa', 'y')
        mock_get_room.return_value = 'None'
        self.assertEqual(
            'Allocated Office Space :None \n Allocated Living Space :None',
            value)

    def test_randomly_allocate(self):
        capacity = 1
        data = {'Krypton': []}
        person_name = 'MIgwi'
        ret_val = self.room.randomly_allocate_rooms(
            capacity, data, person_name)
        self.assertTrue(ret_val)

        person_name = 'Zainab'
        ret_val = self.room.randomly_allocate_rooms(
            capacity, data, person_name)
        self.assertEqual('All rooms are full to capacity', ret_val)

    @patch('app.staff.Staff.staff_names')
    @patch.dict('app.office.Office.office_n_occupants', {'Narnia': []})
    @patch('app.fellow.Fellow.fellow_names')
    @patch.dict('app.livingspace.LivingSpace.room_n_occupants', {'Dojo': []})
    @patch('app.room.Room.reallocate')
    def test_reallocate_room(self, mock_reallocate, mock_fellow_names,
                             mock_staff_names):
        mock_reallocate.return_value = True
        mock_fellow_names.__iter__.return_value = ['njoroge']
        mock_staff_names.__iter__.return_value = ['James_Ndiga']
        person_name, room_name = 'James_Ndiga', 'Narnia'
        ret_val = self.room.reallocate_room(person_name, room_name)
        self.assertIn(person_name, ret_val)
        self.assertIn(room_name, ret_val)
        self.assertIn('was allocated an Office', ret_val)

        person_name, room_name = 'James_Ndiga', 'Dojo'
        ret_val = self.room.reallocate_room(person_name, room_name)
        self.assertEqual(
            'Living Spaces are allocated to fellows ONLY', ret_val)

        person_name, room_name = 'njoroge', 'Php'
        ret_val = self.room.reallocate_room(person_name, room_name)
        self.assertEqual('Room Not Found in the system', ret_val)

        person_name, room_name = 'njoroge', 'Dojo'
        ret_val = self.room.reallocate_room(person_name, room_name)
        self.assertIn(person_name, ret_val)
        self.assertIn(room_name, ret_val)
        self.assertIn('was allocated a Living Space', ret_val)

    @patch.dict('app.livingspace.LivingSpace.room_n_occupants', {'Mars': []})
    @patch('app.livingspace.LivingSpace.living_capacity')
    @patch('app.room.Room.get_room')
    def test_reallocate(self, mock_get_room, mock_living_capacity):
        mock_get_room.return_value = 'None'
        mock_living_capacity.return_value = 1

        value = self.room.reallocate('david', 'Mars', 'livingspace')
        self.assertTrue(value)

        value = self.room.reallocate('Stan', 'Mars', 'livingspace')
        self.assertEqual('Mars has a max of 1 person(s) currently', value)

    @patch.dict('app.office.Office.office_n_occupants',
                {'Alien-Planet': ['Sam', 'Edwin', 'Steve']})
    def test_get_room(self):
        assign = self.room.get_room(person_name='Steve', type_space='office')
        self.assertEqual('Alien-Planet', assign)

    @patch('app.room.Room.compute')
    @patch('amity.Amity.print_file')
    def test_get_allocations(self, mock_compute, mock_print_file):
        mock_compute.return_value = {'Amity': ['Eston Mwaura']}
        mock_print_file.return_value = 'Successful'
        room_details = self.room.get_allocations('test.txt')

        details1 = [{'Amity': ['Eston Mwaura']}, {'Amity': ['Eston Mwaura']}]
        details2 = ['Successful', 'Successful']

        self.assertIn(details1, room_details)
        self.assertIn(details2, room_details)

    @patch('app.room.Room.compute')
    @patch('amity.Amity.print_file')
    def test_get_unallocated(self, mock_compute, mock_print_file):
        mock_compute.return_value = ['Amity']
        mock_print_file.return_value = 'Successful'

        rum = self.room.get_unallocated('sample.txt')

        response1 = [['Amity'], ['Amity']]
        response2 = ['Successful', 'Successful']

        self.assertIn(response1, rum)
        self.assertIn(response2, rum)

    def test_compute(self):
        data = {'m55': ['Aubrey, Chiemeka', 'Mayowa'],
                'Amity': [],
                'Dojo': ['Migwi', 'Elsis']}
        computed = self.room.compute(data, 'allocated')

        tesd = {'m55': ['Aubrey, Chiemeka', 'Mayowa'],
                'Dojo': ['Migwi', 'Elsis']}
        self.assertEqual(computed, tesd)

        computed = self.room.compute(data, 'unallocated')
        self.assertEqual(computed, ['Amity'])

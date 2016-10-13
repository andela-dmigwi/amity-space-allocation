import unittest
from app.room import Room
from mock import patch
# from app.staff import Staff


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room()
        # self.staff = Staff([])

    @patch.dict('app.office.Office.office_n_occupants', {"Dojo": []})
    def test_create_room(self):
        res = self.room.create_room(room_name='Valhala', room_type='office')
        self.assertEqual(res, 'Valhala successfully created as Office')

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
            res, """Create a room of type 'LivingSpace' or 'Office'  ONLY!""")

    @patch.dict('app.office.Office.office_n_occupants',
                {'Alien-Planet': []})
    @patch('app.office.Office.reallocate_office')
    def test_allocate_office_space(self, mock_reallocate_office):
        mock_reallocate_office.return_value = True
        value = self.room.allocate_space('Alien-Planet', 'Gaamuwa')
        self.assertIn('Alien-Planet', value)
        self.assertIn('Gaamuwa', value)
        self.assertIn('was Successfully allocated an Office', value)

    @patch.dict('app.livingspace.LivingSpace.room_n_occupants', {'Mars': []})
    @patch('app.livingspace.LivingSpace.reallocate_livingspace')
    def test_allocate_living_space(self, mock_reallocate_livingspace):
        mock_reallocate_livingspace.return_value = True

        value = self.room.allocate_space('Mars', 'david')
        self.assertIn('Mars', value)
        self.assertIn('david', value)
        self.assertIn('was Successfully allocated a Living Space', value)

    def test_allocate_unknown_space(self):
        ret_values = self.room.allocate_space('Seschachewan', 'david')
        self.assertEqual('Room Not Found in the system', ret_values)

    def test_recall_rooms(self):
        ret_val = self.room.recall_allocated_space('Migwi')
        self.assertEqual(ret_val, 'All rooms have been recalled')

    @patch('app.office.Office.get_assigned_room')
    @patch('app.livingspace.LivingSpace.get_allocated_room')
    def test_get_assigned_room(self, mock_get_assigned_room,
                               mock_get_allocated_room):
        mock_get_assigned_room.return_value = 'Valhala'
        mock_get_allocated_room.return_value = 'Krypton'
        assign = self.room.get_assigned_room(person_name='Super Socky')
        self.assertIn('Valhala', assign)
        self.assertIn('Krypton', assign)

    @patch('app.room.Room.compute')
    @patch('app.room.Room.print_file')
    def test_get_allocations(self, mock_compute, mock_print_file):
        mock_compute.return_value = {'Amity': ['Eston Mwaura']}
        mock_print_file.return_value = 'Successful'
        room_details = self.room.get_allocations('test.txt')

        details1 = [{'Amity': ['Eston Mwaura']}, {'Amity': ['Eston Mwaura']}]
        details2 = ['Successful', 'Successful']

        self.assertIn(details1, room_details)
        self.assertIn(details2, room_details)

    @patch('app.room.Room.compute')
    @patch('app.room.Room.print_file')
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

    # @patch('app.room.Room.open')
    # @patch('builtins.open',open('sample.txt', 'w'))
    # def test_print_file(self):

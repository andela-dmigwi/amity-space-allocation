import unittest
from app.room import Room
from app.staff import Staff

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room()
        self.staff = Staff([])
        
    def test_create_room(self):
        res = self.room.create_room(room_name='Valhala', room_type='Office')
        self.assertEqual(res, 'Valhala has been created as Office')

        #create duplicate room (With same name)
    def test_create_duplicate_room(self):
        res = self.room.create_room(room_name='Valhala', room_type='LivingSpace')
        self.assertEqual(res, 'Valhala already exists ')

        #create a room without a name
    def test_create_room_without_name(self):
        res = self.room.create_room(room_name='', room_type='Office')
        self.assertEqual(res, 'Room name is too short')

        #create type of room not available
    def test_create_room_type_not_available(self):
        res = self.room.create_room(room_name='Valhala', room_type='game room')
        self.assertEqual(res, 'Create a room of type \'LivingSpace\' '+
            'or \'Office\'  ONLY!')

    def test_get_allocations(self):
        rm = self.room.get_allocations()
        self.assertEqual(type(rm),'dict')

    def test_get_unallocated(self):
        rm = self.room.get_unallocated()
        self.assertEqual(type(rm),'dict')    

    def test_get_assigned_room(self):        
        self.staff.add_staff(person_name = 'Super Socky' ) 
        assign = self.room.get_assigned_room(person_name = 'Super Socky' )
        self.assertEqual(type(assign), 'dict')  
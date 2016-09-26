import unittest
from app.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room()
        
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

    def test_get_room(self):
        rm = self.room.get_room('xxxx')
        self.assertEqual([type(rm)], ['dict'])
import unittest
from app.office import Office
from app.staff import Staff 
from app.fellow import Fellow
from app.room import Room

class TestOffice(unittest.TestCase):
    def setUp(self):
        self.office = Office({})
        self.staff = Staff([])
        self.fellow = Fellow({})
        self.room = Room()
        
    def test_allocate_office(self):
        self.staff.add_staff("Millicent Awis")
        ls = self.office.allocate_office(person_name="Millicent Awis")
        self.assertTrue(ls)
    
        ls = self.office.allocate_office(person_name='Wikister Nyabwa')
        self.assertEqual(ls,'Only staff and fellows that can be allocated livingspace')
    
        self.staff.add_staff("Jumbo juniuo")
        self.office.allocate_office(person_name="Jumbo juniuo")

        ls = self.office.allocate_office(person_name="Jumbo juniuo")
        self.assertEqual(ls, 'Jumbo juniuo has an Office already')

    def test_reallocate_office(self):
        self.fellow.add_fellow(person_name='Patrick Njiru')
        self.room.create_room(room_name='Valhala', room_type='Office')
        res = self.office.reallocate_office(person_name='Patrick Njiru', room_name='Valhala')
        self.assertTrue(res)

        es = self.office.reallocate_office(person_name='Patrick Njiru', room_name='Kalahari')
        self.assertEqual(es, 'kalahari is not an office')
    
        es = self.office.reallocate_office(person_name='Patrice Njiru', room_name='Valhala')
        self.assertEqual(es, 'Patrice Njiru is not a fellow or a staff')

    def test_recall_allocated_office(self):
        ls = self.office.recall_allocated_office(person_name="Jumbo juniuo")
        self.assertTrue(ls)

    def test_recall_allocated_office_again(self):
        ls = self.office.recall_allocated_office(person_name="Jumbo juniuo")
        self.assertEqual(ls, 'Jumbo juniuo not found')  

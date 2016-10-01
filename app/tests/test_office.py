import unittest
from app.office import Office
from app.staff import Staff 

class TestOffice(unittest.TestCase):
    def setUp(self):
        self.office = Office()
        self.staff = Staff()
        
    def test_allocate_office(self):
        self.staff.add_staff("Millicent Awis")
        ls = self.office.allocate_office(room_name='Narnia', person_name="Millicent Awis")
        self.assertTrue(ls)

    def test_allocate_office_again(self):
        self.staff.add_staff("Jumbo juniuo")
        self.office.allocate_office(room_name='Krypton', person_name="Jumbo juniuo")

        ls = self.office.allocate_office(room_name='Krypton', person_name="Jumbo juniuo")
        self.assertEqual(ls, 'Jumbo juniuo has an Office already')

    def test_recall_allocated_office(self):
        ls = self.office.recall_allocated_office(person_name="Jumbo juniuo")
        self.assertEqual(ls, 'Room has been recalled')

    def test_recall_allocated_office_again(self):
        ls = self.office.recall_allocated_office(person_name="Jumbo juniuo")
        self.assertEqual(ls, 'Jumbo juniuo not found')

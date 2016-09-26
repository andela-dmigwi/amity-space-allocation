import unittest
from app.person import Person
from app.staff import Staff
from app.room import Room
from app.fellow import Fellow

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person()
        self.staff = Staff()
        self.room  = Room()
        self.fellow = Fellow()

    #test add fellow who doesn't need living space or office
    def test_add_fellow_who_dont_need_room(self):
        pers = self.person.add_person(person_name='Kimani Ndegwa', type_person='fellow')
        self.assertTrue(pers)
        
    #test add fellow who needs a living space
    def test_add_fellow_who_need_livingspace(self):
        pers = self.person.add_person(person_name='Arnold', type_person='fellow', type_room='LivingSpace')
        self.assertTrue(pers) 

    #test add staff to livingspace
    def test_add_staff_to_livingspace(self):
        pers = self.person.add_person(person_name='Njira', type_person='staff', type_room='LivingSpace')
        self.assertFalse(pers)


    def test_add_two_people_who_share_name(self):
        #Adding person one
        self.person.add_person(person_name='Joshua', type_person='staff')
        #Adding person two 
        pers = self.person.add_person(person_name='Joshua', type_person='staff')
        self.assertFalse(pers)


    def test_load_people(self):
        pers = self.person.load_people('people.txt')
        self.assertTrue(pers)


    def test_reallocate_person(self):       
        self.staff.add_staff(person_name='James Ndiga' , person_id=5)
        self.room.create_room(room_name='Valhala', room_type='Office')

        pers = self.person.reallocate_person(person_id=5, room_name='Valhala') 
        self.assertTrue(pers)


    #test if staff can be assigned livingspace
    def test_if_staff_is_assigned_livingspace(self):
        #self.staff.add(person_name='James Ndiga' , person_id=5)
        self.room.create_room(room_name='Dojo', room_type='LivingSpace')

        pers = self.person.reallocate_person(person_id=5, room_name='Dojo') 
        self.assertFalse(pers)

        
    #test if fellow can assigned office and livingspace 
    def test_if_fellow_is_assigned_office_n_livingspace(self):
        self.fellow.add_fellow(person_name='Stanley Ndiga', person_id=7)

        pers_1 = self.person.reallocate_person(person_id=7, room_name='Dojo') 
        pers_2 = self.person.reallocate_person(person_id=7, room_name='Valhala') 

        self.assertEqual([pers_2,pers_1], [True,True])


    #test if staff can be assigned 2 office spaces
    def test_if_staff_is_assigned_2_officespace(self):
        '''staff will hold last room assigned to him /her'''

        #self.fellow.add_fellow(person_name='James Ndiga', person_id=5)
        self.room.create_room(room_name='Krypton', room_type='Office')
        pers_1 = self.person.reallocate_person(person_id=5, room_name='Valhala') 
        pers_2 = self.person.reallocate_person(person_id=5, room_name='Krypton')

        rm1 = self.room.get_room('Valhala') 
        rm2 = self.room.get_room('Krypton')

        self.assertEqual([5 in rm1, 5 in rm2], [False,True])


    #test if fellow can be assigned 2 livingspaces
    def test_if_fellow_is_assigned_2_livingspaces(self):
        '''fellow will hold last room assigned to him /her'''

        #self.fellow.add_fellow(person_name='Stanley Ndiga', person_id=7)
        self.room.create_room(room_name='Amity', room_type='LivingSpace')
        pers_1 = self.person.reallocate_person(person_id=7, room_name='Amity') 
        pers_2 = self.person.reallocate_person(person_id=7, room_name='Dojo')
        
        rm1 = self.room.get_room('Amity') 
        rm2 = self.room.get_room('Dojo')

        self.assertEqual([7 in rm1, 7 in rm2], [False,True])

    def test_get_person_id(self):
        id = self.person.get_person_id(person_name='Stanley Ndiga')
        self.assertEqual(id, 7)
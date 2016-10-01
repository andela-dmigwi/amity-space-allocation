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
        pers = self.person.add_person(person_name='Kimani Ndegwa', type_person='fellow',
                want_accomodation='n')
        self.assertTrue(pers)
        
    #test add fellow who needs a living space
    def test_add_fellow_who_need_livingspace(self):
        pers = self.person.add_person(person_name='Arnold', type_person='fellow', 
            want_accomodation='y')
        self.assertTrue(pers) 

    #test add staff and assign them livingspace
    def test_add_staff_assign_livingspace(self):
        pers = self.person.add_person(person_name='Njira', type_person='staff',
            want_accomodation='y')
        self.assertEqual(pers, 'Failed, staff cannot have accomodation')


    def test_add_two_people_who_share_name(self):
        #Adding person one
        self.person.add_person(person_name='Joshua', type_person='fellow')
        #Adding person two 
        pers = self.person.add_person(person_name='Joshua', type_person='staff')
        self.assertEqual(pers, 'Person name cannot be shared')

    def test_reallocate_person(self):       
        self.staff.add_staff(person_name='James Ndiga')
        self.room.create_room(room_name='Valhala', room_type='Office')

        pers = self.person.reallocate_person(room_name='Valhala',person_name='James Ndiga') 
        self.assertTrue(pers)


    #test if staff can be assigned livingspace
    def test_if_staff_is_assigned_livingspace(self):
        self.room.create_room(room_name='Dojo', room_type='LivingSpace')

        pers = self.person.reallocate_person(person_name='James Ndiga', room_name='Dojo') 
        self.assertEqual(pers, 'staff cannot have accomodation')

        
    #test if fellow can assigned office and livingspace 
    def test_if_fellow_is_assigned_office_n_livingspace(self):
        person_name='Stanley Ndiga'
        self.fellow.add_fellow(person_name)

        pers_1 = self.person.reallocate_person(person_name, room_name='Dojo') 
        pers_2 = self.person.reallocate_person(person_name, room_name='Valhala') 

        self.assertEqual([pers_2, pers_1], [True,True])


    #test if staff can be assigned 2 office spaces
    def test_if_staff_is_assigned_2_officespace(self):
        '''staff will hold last room assigned to him /her'''

        person_name='James Ndiga'
        self.room.create_room(room_name='Krypton', room_type='Office')
        pers_1 = self.person.reallocate_person(person_name, room_name='Valhala') 
        pers_2 = self.person.reallocate_person(person_name, room_name='Krypton')

        rm1 = self.person.get_room_members('Valhala') 
        rm2 = self.person.get_room_members('Krypton')

        self.assertEqual(['James Ndiga' in rm1, 'James Ndiga' in rm2], [False,True])


    #test if fellow can be assigned 2 livingspaces
    def test_if_fellow_is_assigned_2_livingspaces(self):
        '''fellow will hold last room assigned to him /her'''

        person_name='Stanley Ndiga'
        self.room.create_room(room_name='Amity', room_type='LivingSpace')
        pers_1 = self.person.reallocate_person(person_name, room_name='Amity') 
        pers_2 = self.person.reallocate_person(person_name, room_name='Dojo')
        
        rm1 = self.person.get_room_members('Amity') 
        rm2 = self.person.get_room_members('Dojo')

        self.assertEqual(['Stanley Ndiga' in rm1, 'Stanley Ndiga' in rm2], [False,True])

    def test_get_room_members(self):
        self.room.create_room(room_name='Dojo', room_type='Office')
        rm = self.person.get_room_members(room_name='Dojo')
        self.assertEqual(type(rm), 'list')     
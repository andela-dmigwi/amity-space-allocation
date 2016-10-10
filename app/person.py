from app.fellow import Fellow
from app.staff import Staff
from app.office import Office
from app.livingspace import LivingSpace

class Person(object):
    '''Validate input data and undertake basic operaions
     ''' 
    def __init__(self):
        self.staf = Staff([])
        self.fello = Fellow([])
        self.offy = Office({})
        self.living = LivingSpace({})

    def add_person(self, person_name, type_person, want_accomodation ='n'):
        '''By default someone needs an Office '''
        if person_name in Staff.staff_name or person_name in Fellow.fellow_name:
            return person_name+' already exists'

        elif type_person is 'staff':
            if 'y' in want_accomodation:
                return 'staff cannot have accomodation'

            create_staff = self.staff.add_staff(person_name) 
            if create_staff != True:                   
                return create_staff 

            allocate_office = self.offy.allocate_office(person_name)
            if allocate_office:
                return 'You have been allocated Office:'+self.offy.get_room(person_name)
            return allocate_office

        create_fellow = self.fello.add_fellow(person_name)
        if create_fellow != True:        
            return create_fellow

        allocate_office = self.offy.allocate_office(person_name)
        if allocate_office != True:
            return allocate_office

        elif 'y' in want_accomodation:
            allocate_livingspace = self.living.allocate_livingspace(person_name)
            if allocate_livingspace != True:
                return allocate_livingspace
        assigned_office = self.offy.get_room(person_name)
        assigned_living = self.living.get_allocated_room(person_name)
        return 'You have been allocated Office:'+assigned_office' and Living Space:'+assigned_living


                

    def load_people(self, filename = 'people.txt'):
        pass

    def reallocate_person(self, person_name, room_name):
        pass

    def get_room_members(self, room_name):
        '''Return members of a room'''
        return {}    
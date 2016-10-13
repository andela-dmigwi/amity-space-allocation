from app.fellow import Fellow
from app.staff import Staff
from app.office import Office
from app.livingspace import LivingSpace
from app.room import Room


class Person(object):
    '''Validate input data and undertake basic operaions
    '''

    def __init__(self):
        self.staf = Staff([])
        self.fello = Fellow([])
        self.offy = Office({})
        self.living = LivingSpace({})
        self.room = Room()

    def add_person(self, person_name, type_person, want_accomodation='n'):
        '''By default someone needs an Office '''
        if person_name in Staff.staff_names or person_name in Fellow.fellow_names:
            return person_name + ' already exists'

        elif type_person is 'staff':
            if 'y' in want_accomodation:
                return 'staff cannot have accomodation'

            create_staff = self.staf.add_staff(person_name)
            if create_staff is not True:
                return create_staff

            allocate_office = self.offy.allocate_office(person_name)
            if allocate_office:
                return 'You have been allocated Office:' + self.offy.get_room(person_name)
            return allocate_office

        create_fellow = self.fello.add_fellow(person_name)
        if create_fellow is not True:
            return create_fellow

        allocate_office = self.offy.allocate_office(person_name)
        if allocate_office is not True:
            return allocate_office

        elif 'y' in want_accomodation:
            allocate_livingspace = self.living.allocate_livingspace(
                person_name)
            if allocate_livingspace is not True:
                return allocate_livingspace
        assigned_office = self.offy.get_assigned_room(person_name)
        assigned_living = self.living.get_allocated_room(person_name)
        return 'You have been allocated Office:' + assigned_office + ' and Living Space:' + assigned_living    

    def reallocate_person(self, person_name, room_name):
        '''Call a method in room class'''
        return self.room.allocate_space(room_name, person_name)

    def get_room_members(self, room_name):
        if room_name in list(self.offy.office_n_occupants.keys()):
            return self.offy.office_n_occupants[room_name]
        elif room_name in list(self.living.room_n_occupants.keys()):
            return self.living.room_n_occupants[room_name]
        return 'Room not Found'

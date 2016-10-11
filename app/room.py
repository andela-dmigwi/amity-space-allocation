from app.livingspace import LivingSpace
from app.office import Office


class Room(object):
    '''do basic operations and validate input data  '''

    def __init__(self):
        self.off = Office()
        self.liv = LivingSpace()

    def create_room(self, room_name, room_type):
        if room_name in list(Office. office_n_occupants.keys()) or
                    room_name in list(LivingSpace.room_n_occupants.keys()):
            return room_name + " already exists "

        elif room_name is 'office':
            Office.office_n_occupants[room_name] = []
            return room_name + ' successfully created as Office'

        elif room_name is 'livingspace':
            LivingSpace.room_n_occupants[room_name] = []
            return room_name + ' successfully created as Living Space'

        return 'Unknown room type used'

    def allocate_space(self, room_name, person_name):
        '''uses methods in livingspace and office'''
        if room_name in list(Office. office_n_occupants.keys()):
            resp = self.off.reallocate_office(person_name,room_name)
            if resp:
                return person_name+' was Successfully allocates an Office '+room_name
            return resp
        elif room_name in ist(LivingSpace.room_n_occupants.keys()):
            ret = self.liv.reallocate_livingspace(person_name,room_name)
            if ret:
                return person_name+' was Successfully allocates a Living Space '+room_name
        return 'Room Not Found in the system'

    def recall_allocated_space(self, person_name):
        '''uses methods in livingspace and office'''
        ret_off=self.off.recall_allocated_office(person_name)
        ret_liv = self.liv.recall_allocated_livingspace(person_name)
        
    def get_assigned_room(self, person_name):
        '''return room(s) assigned'''
        pass

    # def get_allocations(self, filename=''):
    def get_allocations(self):
        pass

    # def get_unallocated(self, filename):
    def get_unallocated(self):
        pass

from app.livingspace import LivingSpace 
from app.office import Office 

class Room(object): 
    '''do basic operations and validate input data  '''

    def __init__(self):
        pass

    def create_room(self, room_name, room_type):
        pass    

    def allocate_space(self, room_name, person_name):
        '''uses methods in livingspace and office'''
        pass

    def recall_allocated_space(self, person_name):
        '''uses methods in livingspace and office'''
        pass
    
    def get_assigned_room(self, person_name):
        '''return room(s) assigned'''
        pass

    # def get_allocations(self, filename=''):
    def get_allocations(self):
        pass

    # def get_unallocated(self, filename):
    def get_unallocated(self):
        pass   
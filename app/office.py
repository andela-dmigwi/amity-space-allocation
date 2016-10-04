from random import random
from app.fellow import fellow
from app.staff import Staff

class Office(object):
    '''class allocates office to a person and recall an allocated
       office from an individual
       record = {'room_name:[List of Occupants]}
    '''
    office_n_occupants = {}

    def __init__(self, **kwrags):
        Office.office_n_occupants.extend(kwrags)
        self.fello = Fellow()
        self.stf = Staff()
                

    def allocate_office(self, person_name):
        '''An office will be allocated randomly'''

        pass
        
    def reallocate_office(self, person_name, room_name):
        pass

    def recall_allocated_office(self, person_name):
        pass   
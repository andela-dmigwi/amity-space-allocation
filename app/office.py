import random
from app.fellow import Fellow
from app.staff import Staff

class Office(object):
    '''class allocates office to a person and recall an allocated
       office from an individual
       record = {'room_name:[List of Occupants]}
    '''
    office_n_occupants = {}

    def __init__(self, kwrags):        
        self.fello = Fellow({})
        self.stf = Staff([])
        Office.office_n_occupants.update(kwrags)
                

    def allocate_office(self, person_name):
        '''An office will be allocated randomly'''
        if person_name in self.fello.fellow_names or person_name in self.stf.staff_names:
            room = self.get_room(person_name)
            if room != '':
                return person_name+' has an Office already'
            total_rooms = len(Office.office_n_occupants)
            for rm_office in xrange(1, total_rooms + 1):
                offy = random.choices(list(Office.office_n_occupants.items()))
                if len(offy.values()) < 6:
                    Office.office_n_occupants[offy.keys()].append(person_name)
                    return True
                elif rm_office == total_rooms:
                    return 'All Offices are full'
        return 'Offices are allocated to staff and fellows ONLY'

    def reallocate_office(self, person_name, room_name):
        if person_name in self.fello.fellow_names or person_name in self.stf.staff_names:
            self.recall_allocated_office(person_name)            
            try:
                Occupants = Office.office_n_occupants[room_name]
                if len(Occupants) < 6:
                    Office.office_n_occupants[room_name].append(person_name)
                    return True
                return room_name+' has a maximum of 6 people'
            except:
                return ''
        return 'Offices are allocated to staff and fellows ONLY'


    def recall_allocated_office(self, person_name):
        rm_name = ''
        try:
            rm_name = self.get_room(person_name)
            Office.office_n_occupants.remove(rm_name)
            return True
        except:
            return person_name+' not found'
              

    def get_room(self, person_name):
        room_name = ''
        for rm in Office.office_n_occupants:
            if person_name in rm.value():
               room_name = rm.key()
        return room_name  
from random import random
from fellow import Fellow 

class LivingSpace(object):
    '''class allocates a living space to an individual and 
       recalls it from the individual when need arises
       record = {'room_name:[List of Occupants]}
      '''
    room_n_occupants = {}

    def __init__(self,**kwargs):
        '''retrieve all the  livingspaces with their occupants'''
        LivingSpace.room_n_occupants.extend(kwargs)
        self.fellow = Fellow()

    def allocate_livingspace(self, person_name):
        '''livingspaces are allocated randomly''' 
        if person_name in self.fellow.fellow_names:                
            total_rooms = len(room_n_occupants)

            for room_no in xrange(1, total_rooms + 1):                                 
                room = LivingSpace[random(1, total_rooms)]
                list_of_occupants = room[room_name]

                # A room can only accomodate a maximum of 4 fellows
                if len(list_of_occupants) < 4: 
                    list_of_occupants.append(person_name)
                    return True #break the loop

                elif room_no == total_rooms:
                    return 'All Living Space Rooms are full, Create more rooms!!!' 

        return 'Only A fellow who can get Accomodation'

    def reallocate_livingspace(self, person_name, room_name):
        pass       

    def recall_allocated_livingspace(self, person_name): 
        '''If an error is raised the person_name doesn't have a livingspace '''
        room_name = '' 
        for room in room_n_occupants:
            if person_name in room.value():
                room_name = room.key()

        try:
            room_n_occupants[room_name].remove(person_name)
            return True
        except:
            return person_name+' not found'
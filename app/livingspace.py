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
        #check if the fellow has already been assigned a room
        assigned_room = get_allocated_room(person_name)
        if assigned_room != '':
            return person_name+' has a livingspace already'

        elif person_name in self.fellow.fellow_names:                
            total_rooms = len(LivingSpace.room_n_occupants)
        
            for room_no in xrange(1, total_rooms + 1):                                 
                room = LivingSpace.room_n_occupants[random(1, total_rooms)]
                list_of_occupants = room[room_name]

                # A room can only accomodate a maximum of 4 fellows
                if len(list_of_occupants) < 4: 
                    list_of_occupants.append(person_name)
                    return True #break the loop

                elif room_no == total_rooms:
                    return 'All Living Space Rooms are full, Create more rooms!!!' 

        return 'Only A fellow who can get Accomodation'


    def reallocate_livingspace(self, person_name, room_name):
        '''recall allocated space then assign new livingspace'''
        recall_allocated_livingspace(person_name):
        try:
            LivingSpace.room_n_occupants[room_name].append(person_name)
            return True
        except:
            return room_name' does not exist'


    def recall_allocated_livingspace(self, person_name): 
        '''If an error is raised the person_name doesn't have a livingspace '''
        room_name = get_allocated_room(person_name)     
        try:
            LivingSpace.room_n_occupants[room_name].remove(person_name)
            return True
        except:
            return person_name+' not found'


    def get_allocated_room(self, person_name):
        '''Retrieve the room assigned'''
        rm = ''
        for room in LivingSpace.room_n_occupants:
            if person_name in room.value():
                rm = room.key()
        return rm 
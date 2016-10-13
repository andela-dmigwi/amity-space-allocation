import random
from app.fellow import Fellow


class LivingSpace(object):
    '''class allocates a living space to an individual and
       recalls it from the individual when need arises
       record = {'room_name:[List of Occupants]}
    '''
    room_n_occupants = {}

    def __init__(self, data):
        '''retrieve all the  livingspaces with their occupants'''
        self.data = data
        LivingSpace.room_n_occupants.update(self.data)
        self.fellow = Fellow({})

    def allocate_livingspace(self, person_name):
        '''livingspaces are allocated randomly'''
        if person_name in self.fellow.fellow_names:
            # check if the fellow has already been assigned a room
            assigned_room = self.get_allocated_room(person_name)
            if assigned_room != '':
                return person_name + ' has a livingspace already'
            total_rooms = len(LivingSpace.room_n_occupants)
            for room_no in xrange(1, total_rooms + 1):
                room = random.choices(LivingSpace.room_n_occupants.items())

                # A Livingspace can only accomodate a maximum of 4 fellows
                if len(room.values()) < 4:
                    LivingSpace.room_n_occupants[
                        room.keys()].append(person_name)
                    return True  # break the loop
                elif room_no == total_rooms:
                    return """All Living Space Rooms are full, Create more rooms!!!"""
        return 'Only A fellow who can get Accomodation'

    def reallocate_livingspace(self, person_name, room_name):
        '''recall allocated space then assign new livingspace'''
        self.recall_allocated_livingspace(person_name)
        try:
            room_members = LivingSpace.room_n_occupants[room_name]
            if len(room_members) < 4:
                room_members.append(person_name)
                return True
            return room_name + ' has a maximum of 4 fellows'
        except:
            return room_name + ' does not exist'

    def recall_allocated_livingspace(self, person_name):
        '''If an error is raised the person_name doesn't have a livingspace '''
        room_name = self.get_allocated_room(person_name)
        try:
            LivingSpace.room_n_occupants[room_name].remove(person_name)
            return True
        except:
            return person_name + ' not found'

    def get_allocated_room(self, person_name):
        '''Retrieve the room assigned'''
        rm = 'None'
        for room_name, occupants in LivingSpace.room_n_occupants.items():
            if person_name in occupants:
                rm = room_name
        return rm

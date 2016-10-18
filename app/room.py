from app.livingspace import LivingSpace as livin
from app.office import Office
from app.fellow import Fellow
from app.staff import Staff


import random


class Room(Office, livin):
    '''do basic operations and validate input data  '''

    def __init__(self):
        pass

    def create_room(self, room_name, room_type):
        offices = list(Office.office_n_occupants.keys())
        livingspaces = list(livin.room_n_occupants.keys())
        if room_name in offices or room_name in livingspaces:
            return room_name + " already exists "

        elif room_name == '' or type(room_name) is not str:
            return 'Room name used is invalid'

        elif room_type == 'office':
            Office.office_n_occupants[room_name] = []
            return room_name + ' was created as an Office'

        elif room_type == 'livingspace':
            livin.room_n_occupants[room_name] = []
            return room_name + ' was created as Living Space'

        return """Create a room of type 'LivingSpace' or 'Office'  ONLY!"""

    def allocate_space(self, person_name, want_accomodation='n'):
        felo = list(Fellow.fellow_names)
        staff = list(Staff.staff_names)
        if person_name in felo or person_name in staff:
            room_offy = self.get_room(person_name, 'office')
            if room_offy != 'None':
                return person_name + ' has an Office already'

            else:
                ret_val = self.randomly_allocate_rooms(
                    Office.office_capacity,
                    Office.office_n_occupants, person_name)

                # Incase of an error return it
                if ret_val is not True:
                    return ret_val

            if 'y' == want_accomodation:
                room_offy = self.get_room(person_name, 'livingspace')
                if room_offy != 'None':
                    return person_name + ' has a Living Space already'
                else:
                    resp_val = self.randomly_allocate_rooms(
                        livin.living_capacity,
                        livin.room_n_occupants, person_name)

                    # Incase of an error return it
                    if resp_val is not True:
                        return resp_val

            office_ass = self.get_room(person_name, 'office')
            livingspace_as = self.get_room(person_name, 'livingspace')
            return 'Allocated Office Space :' + office_ass + ' \n Allocated Living Space :' + livingspace_as

        return 'Offices are allocated to staff and fellows ONLY'

    def randomly_allocate_rooms(self, capacity, data, person_name):
        total_rooms = len(data)
        for rm in range(1, total_rooms + 1):
            selected = random.choice(list(data.items()))
            if len(selected[1]) < capacity:
                data[selected[0]].append(person_name)
                return True
            elif rm == total_rooms:
                return 'All rooms are full to capacity'

    def reallocate_room(self, person_name, room_name):
        felo = list(Fellow.fellow_names)
        staf = list(Staff.staff_names)

        if room_name in list(Office.office_n_occupants.keys()):
            if person_name not in felo and person_name not in staf:
                return 'Offices are allocated to staff and fellows ONLY'

            resp = self.reallocate(person_name, room_name, 'office')
            if resp is not True:
                return resp
            return person_name + ' was allocated an Office ' + room_name

        elif room_name in list(livin.room_n_occupants.keys()):
            if person_name not in felo:
                return 'Living Spaces are allocated to fellows ONLY'

            ret = self.reallocate(person_name, room_name, 'livingspace')
            if ret is not True:
                return ret
            return person_name + ' was allocated a Living Space ' + room_name

        return 'Room Not Found in the system'

    def reallocate(self, person_name, room_name, type_space):
        # recall allocated room first
        rm_name = self.get_room(person_name, type_space)
        if type_space == 'office':
            capacity = Office.office_capacity
            if rm_name != 'None':
                Office.office_n_occupants[rm_name].remove(person_name)
            occupants = Office.office_n_occupants[room_name]
        else:
            capacity = livin.living_capacity
            if rm_name != 'None':
                livin.room_n_occupants[rm_name].remove(person_name)
            occupants = livin.room_n_occupants[room_name]
        # int() to convert magic mock object to int object
        capacity = int(capacity)

        if len(occupants) < capacity:
            if type_space == 'office':
                Office.office_n_occupants[room_name].append(person_name)
            else:
                livin.room_n_occupants[room_name].append(person_name)
            return True
        return room_name + ' has a max of ' + str(capacity) + ' person(s) currently'

    def get_room(self, person_name, type_space):
        '''Retrieve the room assigned'''
        rm = 'None'
        if type_space == 'office':
            data = Office.office_n_occupants
        else:
            data = livin.room_n_occupants

        for room_name, occupants in data.items():
            if person_name in occupants:
                rm = room_name
        return rm

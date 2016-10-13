from app.livingspace import LivingSpace
from app.office import Office


class Room(object):
    '''do basic operations and validate input data  '''

    def __init__(self):
        self.off = Office({})
        self.liv = LivingSpace({})

    def create_room(self, room_name, room_type):
        offices = list(Office. office_n_occupants.keys())
        livingspaces = list(LivingSpace.room_n_occupants.keys())
        if room_name in offices or room_name in livingspaces:
            return room_name + " already exists "

        elif room_name is '' or type(room_name) is not str:
            return 'Room name used is invalid'

        elif room_type is 'office':
            Office.office_n_occupants[room_name] = []
            return room_name + ' successfully created as Office'

        elif room_type is 'livingspace':
            LivingSpace.room_n_occupants[room_name] = []
            return room_name + ' successfully created as Living Space'

        return """Create a room of type 'LivingSpace' or 'Office'  ONLY!"""

    def allocate_space(self, room_name, person_name):
        '''uses methods in livingspace and office'''
        if room_name in list(Office.office_n_occupants.keys()):
            resp = self.off.reallocate_office(person_name, room_name)
            if resp:
                return person_name+' was Successfully allocated an Office ' + room_name
            return resp
        elif room_name in list(LivingSpace.room_n_occupants.keys()):
            ret = self.liv.reallocate_livingspace(person_name, room_name)
            if ret:
                return person_name+' was Successfully allocated a Living Space ' + room_name
        return 'Room Not Found in the system'

    def recall_allocated_space(self, person_name):
        '''uses methods in livingspace and office'''
        self.off.recall_allocated_office(person_name)
        self.liv.recall_allocated_livingspace(person_name)
        return 'All rooms have been recalled'

    def get_assigned_room(self, person_name):
        '''return room(s) assigned'''
        office_ass = self.off.get_assigned_room(person_name)
        livingspace_as = self.liv.get_allocated_room(person_name)
        return 'Office :' + office_ass + ' Living Space :' + livingspace_as

    def get_allocations(self, filename=None):
        '''Display allocated rooms and print to a file if a file is provided'''
        allocated_office = self.compute(Office.office_n_occupants, 'allocated')
        allocated_livin = self.compute(
            LivingSpace.room_n_occupants, 'allocated')

        ret_resp = []
        if filename is not None:
            resp1 = self.print_file(
                filename, 'RnO-Allo-Office', allocated_office)
            resp2 = self.print_file(
                filename, 'RnO-Allo-Livin', allocated_livin)
            ret_resp.append(resp1)
            ret_resp.append(resp2)

        return [ret_resp, [allocated_office, allocated_livin]]

    def get_unallocated(self, filename=None):
        '''Display unallocated rooms and print to a file
          if filename is provided'''
        allocated_office = self.compute(
            Office.office_n_occupants, 'unallocated')
        allocated_livin = self.compute(
            LivingSpace.room_n_occupants, 'unallocated')

        un_resp = []
        if filename is not None:
            resp1 = self.print_file(filename, 'Empty-Office', allocated_office)
            resp2 = self.print_file(filename, 'Empty-Livin', allocated_livin)
            un_resp.append(resp1)
            un_resp.append(resp2)

        return [un_resp, [allocated_office, allocated_livin]]

    def compute(self, data, return_type):
        '''Compute allocated rooms and unallocated rooms'''
        allocated = {}
        unallocated = []
        for key, value in data.items():
            if len(value) > 0:
                allocated[key] = value
            else:
                unallocated.append(key)
        if return_type is 'allocated':
            return allocated
        return unallocated

    def print_file(self, filename, type, data):
        '''Assign .txt extension'''
        filename = filename + '-' + type + '.txt'
        try:
            with open(filename, 'w') as file:
                if 'allocated' in type:
                    # Print room names and Occupants dict
                    for key, value in data.items():
                        temp = 'Room Name: ' + key + \
                            '  Occupants:' + str(value)
                        file.write(temp)
                else:
                    # Print empty rooms list
                    file.write('Empty Rooms:' + str(data))
                file.close()
                return filename + ' successfully saved'
        except:
            return 'Failed to save ' + filename + ' successfully.'

from app.fellow import Fellow
from app.staff import Staff

class Person(object):
    '''Validate input data and undertake basic operaions
     ''' 
    def __init__(self):
        pass

    def add_person(self, person_name, type_person, want_accomodation ='n'):
        '''By default someone needs an Office 
           Two people should never share a name
        '''
        pass

    def load_people(self, filename = 'people.txt'):
        pass

    def reallocate_person(self, person_name, room_name):
        pass

    def get_room_members(self, room_name):
        '''Return members of a room'''
        return {}

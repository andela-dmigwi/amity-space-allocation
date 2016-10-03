from app.fellow import Fellow
from app.staff import Staff

class Person(object):
    '''Validate input data and undertake basic operaions
     ''' 
    def __init__(self):
        self.staf = Staff()
        self.fello = Fellow()

    def add_person(self, person_name, type_person, want_accomodation ='n'):
        '''By default someone needs an Office            
        '''
        if person_name in Staff.staff_name or person_name in Fellow.fellow_name:
            return person_name+' already exists'

        elif type_person is 'staff':
            if 'y' in want_accomodation:
                return 'staff cannot have accomodation'

            create_staff = self.staff.add_staff(person_name) 
            if create_staff:
                # assign staff a 
                
            else:
                #return the error message then   
                return create_staff 

        create_fellow = self.fello.add_fellow(person_name)
        if create_fellow != True:

        else:
            #return the error
            return create_fellow

        

    def load_people(self, filename = 'people.txt'):
        pass

    def reallocate_person(self, person_name, room_name):
        pass

    def get_room_members(self, room_name):
        '''Return members of a room'''
        return {}

    def create

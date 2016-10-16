class LivingSpace(object):
    '''class allocates a living space to an individual
       record = {'room_name:[List of Occupants]}
    '''
    room_n_occupants = {}
    living_capacity = 4

    def load_livingspaces(self, data_from_db):
        '''add the  livingspaces with their occupants'''
        LivingSpace.room_n_occupants.update(data_from_db)
        return '\t\t LivingSpaces details loaded successfully'

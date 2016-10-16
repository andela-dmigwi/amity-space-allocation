class Office(object):
    '''class allocates office to a person
       record = {'room_name:[List of Occupants]}
    '''
    office_n_occupants = {}
    office_capacity = 6

    def load_offices(self, data_from_db):
        Office.office_n_occupants.update(data_from_db)
        return '\t\tOffices details loaded successfully'

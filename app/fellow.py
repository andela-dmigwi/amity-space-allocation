class Fellow(object):
    '''This class creates, deletes and assign a fellow a level
       record = [List of Fellow Names]
    '''
    fellow_names = []

    def load_fellows(self, fellows):
        '''Assigned fellows stored in db'''
        Fellow.fellow_names.extend(fellows)
        return '\t\tFellow names loaded successfully'

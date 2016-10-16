class Fellow(object):
    '''This class creates, deletes and assign a fellow a level
       record = [List of Fellow Names]
    '''
    fellow_names = []

    def load_fellows(self, fellows):
        '''Assigned fellows stored in db'''
        if type(fellows) is list:
            Fellow.fellow_names.extend(fellows)
            return '\t\t Fellow names loaded successfully'
        else:
            return '\t\t Failed: Incorrect Fellow details'

    def add_one_fellow(self, name):
        if type(name) is str:
            Fellow.fellow_names.append(name)
            return True
        else:
            return '\t\t Failed: Incorrect Fellow details'

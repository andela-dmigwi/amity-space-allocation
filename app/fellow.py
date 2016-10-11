class Fellow(object):
    '''This class creates, deletes and assign a fellow a level
       record = [List of Fellow Names]
    '''
    fellow_names = []

    def __init__(self, fellows):
        '''Assigned fellows stored in db'''
        self.fellows = fellows
        Fellow.fellow_names.extend(self.fellows)

    def add_fellow(self, person_name):
        if person_name is '' or type(person_name) != 'string':
            return 'Invalid Person name used'

        elif len(person_name) > 21:
            return 'Person Name is too long'

        Fellow.fellow_names.append(person_name)
        return True

    def delete_fellow(self, person_name):
        if person_name in Fellow.fellow_names:
            Fellow.fellow_names.remove(person_name)
            return True

        return person_name + ' not Found'

class Staff(object):
    '''This class adds, deletes and assigns a staff a department
       maintain record of staff name(person_name)
       record = [list of staff_names]
      '''
    staff_names = []

    def __init__(self, staffs):     
        Staff.staff_names.extend(staffs)

    def add_staff(self, person_name):
        if person_name is '' or type(person_name) not 'string':
            return 'Invalid Staff name type'

        elif len(person_name) > 21:
            return 'Too long Staff name'

        Staff.staff_names.append(person_name)
        return True
        
    def delete_staff(self, person_name):
        if person_name in Staff.staff_names:
            Staff.staff_names.remove(person_name)
            return True
            
        return person_name+' not found'
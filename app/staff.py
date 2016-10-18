class Staff(object):
    ''' maintain record of staff name(person_name)
       record = [list of staff_names]
      '''
    staff_names = []

    def load_staffs(self, staffs):
        if type(staffs) is list:
            Staff.staff_names.extend(staffs)
            return '\t\t Staffs details loaded successfully'
        else:
            return '\t\t Failed: Incorrect Staffs details'

    def add_one_staff(self, name):
        if type(name) is str:
            Staff.staff_names.append(name)
            return True
        else:
            return '\t\t Failed: Incorrect Staffs details'

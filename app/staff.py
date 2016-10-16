class Staff(object):
    ''' maintain record of staff name(person_name)
       record = [list of staff_names]
      '''
    staff_names = []

    def load_staffs(self, staffs):
        Staff.staff_names.extend(staffs)
        return '\t\t Staffs details loaded successfully'

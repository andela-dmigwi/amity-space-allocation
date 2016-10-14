class Staff(object):
    ''' maintain record of staff name(person_name)
       record = [list of staff_names]
      '''
    staff_names = []

    def __init__(self, staffs):
        Staff.staff_names.extend(staffs)

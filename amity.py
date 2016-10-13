
from app.staff import Staff
from app.fellow import Fellow
from app.office import Office
from app.livingspace import LivingSpace
import sqlite3 as lite


class Amity(object):
    '''This class will contain the docopt commandline interactive framework'''
    db = 'amity.db'

    def __init__(self):
        self.con = ''
        self.cur = ''

    def connect_db(self):
        self.con = lite.connect(Amity.db)
        with self.con:
            self.cur = self.con.cursor()

    def save_state(self, db):
        self.dump_databases_and_create_new()

        self.save_data_into_db(data=Staff.staff_names, 'fellow_n_ staff_details')
        self.save_data_into_db(data=Fellow.fellow_names, 'fellow_n_ staff_details')
        self.save_data_into_db(data=Office.office_n_occupants, 'office_details')
        self.save_data_into_db(data=LivingSpace.room_n_occupants, 'living_details')

    def load_state(self, db):
        self.connect_db()

        pass

    def load_people(self, filename='people.txt'):
        with open(filename, 'r') as input_file:
            people = input_file.readlines()
            for person in people:
                person = person.split()
                if person:
                    is_fellow = True
                    is_staff = False
                    wants_accomodation = None

                    if 'STAFF' in person:
                        is_fellow = False
                        is_staff = True

                    if 'Y' in person:
                        wants_accomodation = 'Y'

                    arg_dict = ({
                        "<first_name>": person[0],
                        "<last_name>": person[1],
                        "Staff": is_staff,
                        "Fellow": is_fellow,
                        "<wants_accomodation>": wants_accomodation
                    })

    def dump_databases_and_create_new(self):
        try:
            print 'Initialize database Creation'

            con = lite.connect(r'amity.db')
            cur = con.cursor()
            cur.executescript("""
                DROP TABLE IF EXISTS fellow_n_ staff_details;
                CREATE TABLE fellow_n_ staff_details(person_name TEXT,
                            type_person TEXT);

                DROP TABLE IF EXISTS office_details;
                CREATE TABLE office_details(room_name TEXT,
                            occuppants TEXT);

                DROP TABLE IF EXISTS living_details;
                CREATE TABLE living_details(room_name TEXT,
                            occuppants TEXT); """
                              )
            con.commit()

            print 'Databases creation finished successfully!!'

        except lite.Error, e:
            print 'Error %s ocurred : Databases Creation failed!!!' % e.arg[0]

        def save_data_into_db(self, data, table):
            self.connect_db()
            row = []

            for key, val in data.items():
                row.append(key)
                if type(val) is list:
                    row.append(val.join('|'))
                row.append(val)

            self.cur.execute("INSERT INTO +'table'+ VALUES(?,?)", tuple(row))
            self.con.commit()
            self.con.close()
            return True

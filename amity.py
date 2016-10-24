
from app.staff import Staff
from app.fellow import Fellow
from app.office import Office
from app.person import Person
from app.livingspace import LivingSpace
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, Sequence, Column, Integer,
                        String, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    '''class mapper for table user'''
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    person_name = Column(String(30))
    type_person = Column(String(30))

    def __repr__(self):
        return "<User(person_name='%s', type_person='%s')>" % (
            self.type_person, self.type_person)


class Room(Base):
    '''class mapper for table room'''
    __tablename__ = 'room'
    id = Column(Integer, Sequence('room_id_seq'), primary_key=True)
    room_type = Column(String(20))
    room_name = Column(String(30))
    occupant1 = Column(String(30), ForeignKey('user.id'))
    occupant2 = Column(String(30), ForeignKey('user.id'))
    occupant3 = Column(String(30), ForeignKey('user.id'))
    occupant4 = Column(String(30), ForeignKey('user.id'))
    occupant5 = Column(String(30), ForeignKey('user.id'))
    occupant6 = Column(String(30), ForeignKey('user.id'))

    def __repr__(self):
        if self.room_type.lower() == 'office':
            return """<Room(room name='%s', occupant1='%s',
            occupant2='%s', occupant3='%s', occupant4='%s',
            occupant5='%s', occupant6='%s')>""" % (self.room_name,
                                                   self.occupant1,
                                                   self.occupant2,
                                                   self.occupant3,
                                                   self.occupant4,
                                                   self.occupant5,
                                                   self.occupant6)

        return """<Room(room name='%s',
         occupant1='%s',occupant2='%s',
          occupant3='%s', occupant4='%s')>""" % (self.room_name,
                                                 self.occupant1,
                                                 self.occupant2,
                                                 self.occupant3,
                                                 self.occupant4)


class Amity(object):

    def __init__(self):
        self.engine = ''
        self.fellow = Fellow()
        self.staff = Staff()
        self.living_space = LivingSpace()
        self.office = Office()

    def connect_db(self, db_name=None):
        if db_name is not None:
            name = 'sqlite:///' + db_name[:db_name.index('.')] + '.db'
        else:
            name = 'sqlite:///amity.db'
        # db_name = db_name[:db_name.index('.')] or 'amity'
        # return create_engine(db_name+'.db')
        return create_engine(name)

    def create_tables(self):
        engine = self.connect_db()

        # check if the tables exist then drop them all if they exist
        if engine.dialect.has_table(engine.connect(), "user"):
            User.__table__.drop(engine)
        if engine.dialect.has_table(engine.connect(), "room"):
            Room.__table__.drop(engine)

        Base.metadata.create_all(engine)

    def load_state(self):
        '''copy data from the database to the application'''
        engine = self.connect_db()

        print("Please Wait... This may take some few minutes.")
        # do something
        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        session = Session()

        print("\tReading data from the database")
        # populate the various lists and dicts
        self.retrieve_data_from_db(session)

        session.commit()
        session.flush()

        print("Load State successfully completed")

    def retrieve_data_from_db(self, session):
        query_room = session.query(Room).all()
        query_user = session.query(User).all()
        fellows = [
            user.person_name for user in query_user
            if user.type_person == 'fellow']
        staffs = [
            user.person_name for user in query_user
            if user.type_person == 'staff']

        offices = {}
        livingspaces = {}
        query_room = session.query(Room).all()
        for room in query_room:
            livingspace_occupants = []
            office_occupants = []
            if room.room_type.lower() == 'office':
                office_occupants.append(room.occupant1)
                office_occupants.append(room.occupant2)
                office_occupants.append(room.occupant3)
                office_occupants.append(room.occupant4)
                office_occupants.append(room.occupant5)
                office_occupants.append(room.occupant6)
                # remove all '' entries
                office_occupants = [
                    ocupant for ocupant in office_occupants if ocupant != '']

                offices[room.room_name] = office_occupants

            else:
                livingspace_occupants.append(room.occupant1)
                livingspace_occupants.append(room.occupant2)
                livingspace_occupants.append(room.occupant3)
                livingspace_occupants.append(room.occupant4)

                # remove all '' entries
                livingspace_occupants = [
                    ocupant for ocupant in livingspace_occupants
                    if ocupant != '']
                livingspaces[room.room_name] = livingspace_occupants
        # load data from db
        text = self.fellow.load_fellows(fellows)
        text = text + '\n%s' % self.staff.load_staffs(staffs)
        text = text + \
            '\n%s' % self.living_space.load_livingspaces(livingspaces)
        text = text + '\n%s' % self.office.load_offices(offices)

        print(text)

    def save_state(self, db=None):
        engine = self.connect_db(db)
        print("Please Wait... This may take some few minutes.")
        self.create_tables()

        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        session = Session()

        print("\tInitiating database population....")
        # populate table users
        # populate table rooms
        self.order_data_ready_for_saving(session)
        print("\tFinalizing database population....")

        session.commit()
        session.flush()
        print("Save State successfully completed.")

    def order_data_ready_for_saving(self, session):
        people = []
        people.extend(list(Fellow.fellow_names))
        people.extend(list(Staff.staff_names))
        ordered_users = []
        for person in people:
            if person is not None and person != 'None':
                user = User()
                user.person_name = person
                if person in list(Fellow.fellow_names):
                    user.type_person = 'fellow'
                elif person in list(Staff.staff_names):
                    user.type_person = 'staff'
                ordered_users.append(user)

        session.add_all(ordered_users)

        Total_rooms = {}
        Total_rooms.update(Office.office_n_occupants)
        Total_rooms.update(LivingSpace.room_n_occupants)
        ordered_rooms = []
        for key, value in list(Total_rooms.items()):
            room = Room()
            room.room_name = key
            room.occupant1 = '' if len(value) < 1 else value[0]
            room.occupant2 = '' if len(value) < 2 else value[1]
            room.occupant3 = '' if len(value) < 3 else value[2]
            room.occupant4 = '' if len(value) < 4 else value[3]
            if room.room_name in LivingSpace.room_n_occupants:
                room.room_type = 'livingspace'
            else:
                room.room_type = 'office'
                room.occupant5 = '' if len(value) < 5 else value[4]
                room.occupant6 = '' if len(value) < 6 else value[5]
            ordered_rooms.append(room)

        session.add_all(ordered_rooms)

    def load_people(self, filename='people.txt'):
        '''loads people into the database'''
        with open(filename, 'r') as input_file:
            people = input_file.readlines()
            data = []
            for persn in people:
                persn = persn.split(' ')
                if persn:
                    wants_accomodation = 'n'
                    person_name = persn[0]
                    if 'STAFF' in persn:
                        type_person = 'staff'
                    else:
                        type_person = 'fellow'

                    if len(persn) > 2:
                        ps = persn[2]
                        if '\n' in ps:
                            wants_accomodation = ps[:ps.index('\n')].lower()
                        else:
                            wants_accomodation = ps.lower()

                    arg_dict = {
                        "person_name": person_name,
                        "type_person": type_person,
                        "wants_accomodation": wants_accomodation
                    }
                data.append(arg_dict)
        for entry in data:
            ret_val = Person().add_person(
                person_name=entry["person_name"],
                type_person=entry["type_person"],
                want_accomodation=entry["wants_accomodation"])
            if ret_val == 'None':
                print ('No Rooms Available')
            else:
                print(ret_val)

    def get_allocations(self, filename=None):
        '''Display allocated rooms and print to a file if a file is provided'''
        allo_office = self.compute(Office.office_n_occupants, 'allocated')
        allo_livin = self.compute(LivingSpace.room_n_occupants, 'allocated')

        resp1 = 'No File Saved'
        resp2 = 'No File Saved'
        if filename is not None:
            resp1 = Amity().print_file(filename, 'RnO-Office', allo_office)
            resp2 = Amity().print_file(filename, 'RnO-Livin', allo_livin)

        if type(allo_office) is dict and type(allo_livin) is dict:
            allo_office.update(allo_livin)
        return [allo_office, resp1, resp2]

    def get_unallocated(self, filename=None):
        '''Display unallocated rooms and print to a file
          if filename is provided'''
        allo_offices = self.compute(Office.office_n_occupants, 'unallocated')
        allo_livins = self.compute(LivingSpace.room_n_occupants, 'unallocated')

        response1 = 'No File Saved'
        response2 = 'No File Saved'
        if filename is not None:
            response1 = Amity().print_file(
                filename, 'Empty-Office', allo_offices)
            response2 = Amity().print_file(
                filename, 'Empty-Livin', allo_livins)

        if type(allo_offices) is list and type(allo_livins) is list:
            allo_offices.extend(allo_livins)
        return [allo_offices, response1, response2]

    def compute(self, data, return_type):
        '''Compute allocated rooms and unallocated rooms'''
        allocated = {}
        unallocated = []
        for key, value in data.items():
            if len(value) > 0:
                allocated[key] = value
            else:
                unallocated.append(key)
        if return_type == 'allocated':
            return allocated
        return unallocated

    def get_all_unallocated_people(self, filename=None):
        fellows = list(Fellow.fellow_names)
        staff = list(Staff.staff_names)

        occupants = []
        for key, value in LivingSpace.room_n_occupants.items():
            occupants.extend(value)

        for key, value in Office.office_n_occupants.items():
            occupants.extend(value)

        set_occupants = set(occupants)
        fell = set(fellows) - set_occupants
        sta = set(staff) - set_occupants

        resp1 = 'No File Saved'
        resp2 = 'No File Saved'
        if filename is not None:
            resp1 = Amity().print_file(filename, 'unallo_fellows', fell)
            resp2 = Amity().print_file(filename, 'unallo_staff', sta)

        return [fell, resp1, sta, resp2]

    def print_file(self, filename, type, data):
        '''Assign .txt extension'''
        filename = filename + '-' + type + '.txt'
        try:
            with open(filename, 'w') as file:
                temp = ''
                if 'RnO' in type:
                    # Print room names and Occupants dict
                    for key, value in data.items():
                        temp = 'Room Name: ' + key + \
                            '  Occupants:' + str(value) + \
                            '\n\r'
                        file.write(temp)
                elif 'Empty' in type:
                    # Print empty rooms list
                    temp = 'Empty Rooms:' + str(data) + '\n\r'
                    file.write(temp)
                elif 'unallo_' in type:
                    temp = 'Unallocated people\n' + str(data)
                    file.write(temp)
                file.close()
                return '"' + filename + '"" successfully saved'
        except:
            return 'Failed to save ' + filename + ' successfully.'

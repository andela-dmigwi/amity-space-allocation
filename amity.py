
from app.staff import Staff
from app.fellow import Fellow
from app.office import Office
from app.person import Person
from app.livingspace import LivingSpace
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, Sequence, Column, Integer,
                        String, ForeignKey, MetaData)
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
        self.felo = Fellow()
        self.staf = Staff()
        self.livin = LivingSpace()
        self.offy = Office()

    def connect_db(self):
        return create_engine('sqlite:///amity.db')

    def create_tables(self):
        engine = self.connect_db()
        status_user = engine.dialect.has_table(
            engine.connect(), "user")
        status_room = engine.dialect.has_table(
            engine.connect(), "room")

        print(status_room)
        print(status_user)
        # If any of the two tables is available drop them
        # if status_room or status_user:
        #     Base.metadata.drop_all()

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
        fellows = []
        staffs = []
        print(User)
        print(Room)
        query_room = session.query(Room).all()
        query_user = session.query(User).all()
        for user in query_user:
            if user.type_person.lower() == 'fellow':
                fellows.append(user.person_name)
            else:
                staffs.append(user.person_name)

        offices = {}
        livingspaces = {}
        query_room = session.query(Room).all()
        for room in query_room:
            if room.room_type.lower() == 'office':
                offices[room.room_name] = [room.occupant1, room.occupant2,
                                           room.occupant3, room.occupant4,
                                           room.occupant5, room.occupant6]
            else:
                livingspaces[room.room_name] = [room.occupant1, room.occupant2,
                                                room.occupant3, room.occupant4]
        # print(fellows)
        # print(staffs)
        # print(livingspaces)
        # print(offices)
        # load data from db
        print(self.felo.load_fellows(fellows))
        print(self.staf.load_staffs(staffs))
        print(self.livin.load_livingspaces(livingspaces))
        print(self.offy.load_offices(offices))

    def save_state(self):
        engine = self.connect_db()
        print("Please Wait... This may take some few minutes.")
        self.create_tables()

        # do something
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
            user = User()
            user.person_name
            user.type_person
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
            if room.room_name in Office.office_n_occupants:
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
            for person in people:
                person = person.split(' ')
                if person:
                    person_name = person[0]
                    wants_accomodation = 'N'

                    if 'STAFF' in person:
                        type_person = 'STAFF'
                    else:
                        type_person = 'FELLOW'

                    if 'Y' in person:
                        wants_accomodation = 'Y'

                    arg_dict = {
                        "person_name": person_name,
                        "type_person": type_person,
                        "wants_accomodation": wants_accomodation
                    }
                data.append(arg_dict)
        for entry in data:
            ret_val = Person.add_person(
                person_name=entry["person_name"],
                type_person=entry["type_person"],
                want_accomodation=entry["wants_accomodation"])
            print(ret_val)

    def get_allocations(self, filename=None):
        '''Display allocated rooms and print to a file if a file is provided'''
        allo_office = self.compute(Office.office_n_occupants, 'allocated')
        allo_livin = self.compute(LivingSpace.room_n_occupants, 'allocated')
        allo_office.update(allo_livin)

        resp1 = 'No File Saved'
        resp2 = 'No File Saved'
        if filename is not None:
            resp1 = Amity().print_file(filename, 'RnO-Office', allo_office)
            resp2 = Amity().print_file(filename, 'RnO-Livin', allo_livin)
        return [allo_office, resp1, resp2]

    def get_unallocated(self, filename=None):
        '''Display unallocated rooms and print to a file
          if filename is provided'''
        allo_office = self.compute(Office.office_n_occupants, 'unallocated')
        allo_livin = self.compute(LivingSpace.room_n_occupants, 'unallocated')
        allo_office.extend(allo_livin)

        resp1 = 'No File Saved'
        resp2 = 'No File Saved'
        if filename is not None:
            resp1 = Amity().print_file(filename, 'Empty-Office', allo_office)
            resp2 = Amity().print_file(filename, 'Empty-Livin', allo_livin)
        return [allo_office, resp1, resp2]

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

    def print_file(self, filename, type, data):
        '''Assign .txt extension'''
        filename = filename + '-' + type + '.txt'
        try:
            with open(filename, 'w') as file:
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
                file.close()
                return '"' + filename + '"" successfully saved'
        except:
            return 'Failed to save ' + filename + ' successfully.'

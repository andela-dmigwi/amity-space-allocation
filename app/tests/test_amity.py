import unittest
from app.livingspace import LivingSpace
from app.fellow import Fellow
from amity import Amity
from mock import patch, mock_open
import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Table, create_engine, Sequence, Column, Integer,
                        String, ForeignKey, MetaData)
from sqlalchemy.ext.declarative import declarative_base


class TestAmity(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        session = sessionmaker(self.engine)
        session.configure(bind=self.engine)
        self.session = session()
        sys.stdout = StringIO()
        self.amity = Amity()
        self.Base = declarative_base()
        # Base.metadata.create_all(self.engine)
        # self.panel = Panel(1, 'ion torrent', 'start')
        # self.session.add(self.panel)
        # self.session.commit()

    def test_type_of_amity(self):
        self.assertIsInstance(Amity(), object)

    @patch('amity.Amity.connect_db')
    def test_create_tables(self, mock_connect_db):
        mock_connect_db.return_value = self.engine
        self.amity.create_tables()
        # assert table user exists
        self.assertTrue(self.engine.dialect.has_table(
            self.engine.connect(), "user"))
        # assert table room exists
        self.assertTrue(self.engine.dialect.has_table(
            self.engine.connect(), "room"))

    @patch('amity.Amity.connect_db')
    @patch('amity.Amity.retrieve_data_from_db')
    def test_load_state(self, mock_connect_db, mock_retrieve_data_from_db):
        mock_connect_db.return_value = self.engine
        mock_retrieve_data_from_db.return_value = True
        self.amity.load_state()
        printed = sys.stdout.getvalue()
        self.assertIn(
            "Please Wait... This may take some few minutes.", printed)
        self.assertIn("\tReading data from the database", printed)
        self.assertIn("Load State successfully completed", printed)
        self.assertIn('', printed)

    def test_retrieve_data_from_db(self):
        class User(self.Base):
            '''class mapper for table user'''
            __tablename__ = 'user'
            id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
            person_name = Column(String(30))
            type_person = Column(String(30))

        class Room(self.Base):
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

        self.Base.metadata.create_all(self.engine)

        if self.engine.dialect.has_table(self.engine.connect(), "user"):
            print('user')
            test_User = Table("user", MetaData(self.engine), autoload=True)
            sample_data = {'person_name': 'andela-jkariuki',
                           'type_person': 'fellow'}
            test_User.insert().execute(sample_data)

        elif self.engine.dialect.has_table(self.engine.connect(), "room"):
            test_Room = Table("room", MetaData(self.engine), autoload=True)
            sample_data = {'room_name': 'php', 'room_type': 'livingspace',
                           'occupant1': 'Morris', 'occupant2': 'Migwi'}
            test_Room.insert().execute(sample_data)

        self.amity.retrieve_data_from_db(self.session)
        self.assertIn('andela-jkariuki', Fellow.fellow_names)
        self.assertNotIn('php', list(LivingSpace.room_n_occupants.keys()))

    @patch('amity.Amity.connect_db')
    @patch('amity.Amity.create_tables')
    @patch('amity.Amity.order_data_ready_for_saving')
    def test_save_state(self, mock_connect_db, mock_create_tables,
                        mock_order_data_ready_for_saving):
        mock_connect_db.return_value = self.engine
        mock_create_tables.return_value = True
        mock_order_data_ready_for_saving.return_value = True

        sys.stdout = StringIO()
        self.amity.save_state()
        printed = sys.stdout.getvalue()
        self.assertIn(
            "Please Wait... This may take some few minutes.", printed)
        self.assertIn("\tInitiating database population....", printed)
        self.assertIn("\tFinalizing database population....", printed)
        self.assertIn("Save State successfully completed.", printed)

    @patch('app.fellow.Fellow.fellow_names')
    @patch('app.staff.Staff.staff_names')
    @patch.dict('app.office.Office.office_n_occupants',
                {'Round_Table': ['Sass', 'Joshua', 'Jeremy'],
                 'Krypton': ['Percila', 'Kimani', 'Whitney'],
                 'Valhala': ['Migwi']
                 })
    @patch.dict('app.livingspace.LivingSpace.room_n_occupants',
                {'php': ['Andela1', 'andela2', 'Mr know it all'],
                 'amity': ['chiemeka', 'mayowa', 'chioma'],
                 'm55': ['adeleke']
                 })
    def test_order_data_ready_for_saving(self, mock_fellow_names,
                                         mock_staff_names):
        class User(self.Base):
            '''class mapper for table user'''
            __tablename__ = 'user'
            id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
            person_name = Column(String(30))
            type_person = Column(String(30))

        class Room(self.Base):
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

        self.Base.metadata.create_all(self.engine)

        mock_fellow_names.__iter__.return_value = ['chiemeka', 'mayowa',
                                                   'Andela1', 'andela2',
                                                   'adeleke']
        mock_staff_names.__iter__.return_value = ['Sass', 'Joshua', 'Jeremy',
                                                  'chioma', 'Mr know it all']
        self.amity.order_data_ready_for_saving(self.session)
        self.session.commit()
        self.session.flush()
        # check if table user exists
        all_rooms = {}
        all_users = []
        if self.engine.dialect.has_table(self.engine.connect(), "user"):
            test_User = Table("user", MetaData(self.engine), autoload=True)
            all_users = test_User.select().execute()
            print(all_rooms)
        elif self.engine.dialect.has_table(self.engine.connect(), "room"):
            test_Room = Table("room", MetaData(self.engine), autoload=True)
            all_rooms = test_Room.select().execute()
            print(all_users)

        self.assertNotIn(frozenset({'Valhala': ['Migwi']}), all_rooms)
        self.assertNotIn(['Mr know it all', 'adeleke'], all_users)

    def test_print_file(self):
        data = {'The_Key': 'The value'}
        sample_text = 'Room Name: The_Key Occupants:The value \n\r'
        with patch("builtins.open",
                   mock_open(read_data=sample_text)) as mock_file:
            self.amity.print_file('sample', 'allocated', data)
            mock_file.assert_called_with('sample-allocated.txt', 'w')
            # mock_file.write.assert_called_once_with(sample_text, 'w')
            assert open('sample-allocated.txt', 'w').read() == sample_text

    @patch('app.person.Person.add_person')
    def test_load_people(self, mock_add_person):
        sample_read_text = 'andela-dmigwi FELLOW Y'
        mock_add_person.return_value = 'Successful'

        with patch("builtins.open",
                   mock_open(read_data=sample_read_text)) as mock_file:
            self.amity.load_people()
            # assert open("people.txt", 'r').readlines() == sample_read_text
            mock_file.assert_called_with("people.txt", 'r')

        printed = sys.stdout.getvalue()
        self.assertIn('Successful', printed)

    @patch('amity.Amity.compute_rooms')
    @patch('amity.Amity.print_file')
    def test_get_allocations(self, mock_print_file, mock_compute_rooms):
        mock_compute_rooms.return_value = {'Amity': ['Eston Mwaura']}
        mock_print_file.return_value = 'Successful'
        room_details = self.amity.get_allocations('test.txt')

        office_details = {'Amity': ['Eston Mwaura']}
        livingspace_details = 'Successful'

        self.assertIn(office_details, room_details)
        self.assertIn(livingspace_details, room_details)

    @patch('amity.Amity.compute_rooms')
    @patch('amity.Amity.print_file')
    def test_get_unallocated(self, mock_print_file, mock_compute_rooms):
        mock_compute_rooms.return_value = ['Amity']
        mock_print_file.return_value = 'Successful'

        room_details = self.amity.get_unallocated('sample.txt')

        response_office = ['Amity', 'Amity']
        response_livingspace = 'Successful'

        self.assertIn(response_office, room_details)
        self.assertIn(response_livingspace, room_details)

    def test_compute(self):
        rooms = {'m55': ['Aubrey, Chiemeka', 'Mayowa'],
                 'Amity': [],
                 'Dojo': ['Migwi', 'Elsis']}
        computed = self.amity.compute_rooms(rooms, 'allocated')

        rooms_1 = {'m55': ['Aubrey, Chiemeka', 'Mayowa'],
                   'Dojo': ['Migwi', 'Elsis']}
        self.assertEqual(computed, rooms_1)

        computed = self.amity.compute_rooms(rooms, 'unallocated')
        self.assertEqual(computed, ['Amity'])

    @patch.dict('app.office.Office.office_n_occupants',
                {'Dojo': ['Njira']})
    @patch.dict('app.livingspace.LivingSpace.room_n_occupants',
                {'Valhala': ['Edwin']})
    @patch('app.staff.Staff.staff_names')
    @patch('app.fellow.Fellow.fellow_names')
    def test_get_all_unallocated_people(self,
                                        mock_fellow_names, mock_staff_names):
        mock_fellow_names.__iter__.return_value = ['Lolo', 'Edwin']
        mock_staff_names.__iter__.return_value = ['Eston', 'Njira']

        check = self.amity.get_all_unallocated_people()
        self.assertIn('Lolo', check[0])
        self.assertIn('Eston', check[2])


# if __name__ == '__main__':
#     unittest.main()

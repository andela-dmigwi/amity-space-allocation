import unittest
from amity import Amity

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, Sequence, Column, Integer,
                        String, ForeignKey, metadata)
from sqlalchemy.ext.declarative import declarative_base


class TestAmity(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = sessionmaker(self.engine)
        # Base = declarative_base()
        # Base.metadata.create_all(self.engine)
        # self.panel = Panel(1, 'ion torrent', 'start')
        # self.session.add(self.panel)
        # self.session.commit()

    def test_connect_db(self):
        print(Amity.connect_db())

    def test_type_of_amity(self):
        self.assertIsInstance(Amity(), object)

    def test_create_tables(self):
        pass

    def test_load_state(self):
        pass

    def test_retrieve_data_from_db(self):
        pass

    def test_save_state(self):
        pass

    def test_order_data_ready_for_saving(self):
        pass

    def test_print_file(test):
        pass

    def test_load_people(self):
        pass
if __name__ == '__main__':
    unittest.main()
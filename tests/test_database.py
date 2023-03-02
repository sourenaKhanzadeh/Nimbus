# Unit tests for the database component in Nimbus

import unittest
from database.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.create_tables()

    def test_insert_data(self):
        # TODO: Add unit test for inserting data
        pass

    def test_update_data(self):
        # TODO: Add unit test for updating data
        pass

    def test_delete_data(self):
        # TODO: Add unit test for deleting data
        pass

    def test_get_data(self):
        # TODO: Add unit test for getting data
        pass

    def tearDown(self):
        self.db.close()

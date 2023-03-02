# Code for managing the database in Nimbus

import sqlite3

class Database:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # TODO: Add code to create tables
        pass

    def insert_data(self, data):
        # TODO: Add code to insert data
        pass

    def update_data(self, data):
        # TODO: Add code to update data
        pass

    def delete_data(self, data_id):
        # TODO: Add code to delete data
        pass

    def get_data(self, data_id):
        # TODO: Add code to get data
        pass

    def close(self):
        self.conn.close()

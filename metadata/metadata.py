# Code for managing the metadata in Nimbus

import sqlite3

class Metadata:
    def __init__(self, metadata_db):
        self.conn = sqlite3.connect(metadata_db)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # TODO: Add code to create tables
        pass

    def insert_metadata(self, metadata):
        # TODO: Add code to insert metadata
        pass

    def update_metadata(self, metadata):
        # TODO: Add code to update metadata
        pass

    def delete_metadata(self, metadata_id):
        # TODO: Add code to delete metadata
        pass

    def get_metadata(self, metadata_id):
        # TODO: Add code to get metadata
        pass

    def close(self):
        self.conn.close()

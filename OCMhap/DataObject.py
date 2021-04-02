import pandas as pd


class DataObject(object):
    """
    A DataObject is an object that stores tabular data.
    """
    def __init__(self):
        """Initialize a DataObject"""
        self.attributes = list()
        self.data = pd.DataFrame()

    def import_from_file(self, file):
        """
        Import tabular data from a file
        :param file: a readable file handle
        """
        self.data = pd.read_csv(file)
        self.attributes = self.data.columns

    def export_to_file(self, file):
        """
        Export the tabular data in this object to a file in csv format
        :param file: a writable file handle
        """
        self.data.to_csv(file)
        self.attributes = self.data.columns

    def copy(self):
        """
        Create a copy of this object
        :return: a new DataObject
        """
        new_obj = DataObject()

        new_obj.data = self.data.copy()
        new_obj.attributes = self.attributes.copy()

        return new_obj

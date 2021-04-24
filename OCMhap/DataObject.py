import pandas


class DataObject(object):
    """
    A DataObject is an object that stores tabular data.
    """
    def __init__(self):
        """Initialize a DataObject"""
        self.data = pandas.DataFrame()

    def import_from_file(self, file):
        """
        Import tabular data from a file
        :param file: a readable file handle
        """
        self.data = pandas.read_csv(file)

    @property
    def attributes(self):
        return list(self.data.columns)

    def copy(self):
        """
        Create a copy of this object
        :return: a new DataObject
        """
        new_obj = DataObject()

        new_obj.data = self.data.copy()

        return new_obj

import pandas as pd


class DataObject(object):
    def __init__(self):
        self.attributes = list()
        self.data = pd.DataFrame()

    def import_from_file(self, file):
        self.data = pd.read_csv(file)
        self.attributes = self.data.columns

    def export_to_file(self, file):
        self.data.to_csv(file)
        self.attributes = self.data.columns

    def copy(self):
        new_obj = DataObject()

        new_obj.data = self.data.copy()
        new_obj.attributes = self.attributes.copy()

        return new_obj

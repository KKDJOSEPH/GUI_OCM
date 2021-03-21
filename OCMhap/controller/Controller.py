import sys
import webbrowser
from tkinter import filedialog

from OCMhap.Data import DataObject
from OCMhap.gui.DataImportPage import DataImportPage
from OCMhap.gui.MainPage import MainPage


class MainController(object):
    """
    A GUIController represents a controller for the GUI of the
    OCM Advisory Health Analytics Platform.
    """
    def __init__(self, data):
        """
        Initialize the GUIController by initializing its component frames.
        """
        self.page = MainPage(self)
        self.data = data

    def analysis(self, event):
        """
        Serve the analysis import interface.
        """
        self.page.stop()

    def data_import(self, event):
        """
        Serve the data import interface.
        """
        self.page.stop()
        controller = DataImportController(self, self.data)

    def about(self, event):
        """
        Fetch the OCM advisory webpage.
        """
        webbrowser.open("https://ocmadvisory.com/", new=0)

    def return_home(self, event):
        """
        Return to the main page from a separate window
        """
        self.page = MainPage(self)
        self.page.run()

    def gogogo(self):
        """Start the application"""
        self.page.run()


class DataImportController(object):
    """
    A DataImportController is a controller for the data import GUI.
    """
    def __init__(self, controller, data):
        """
        Initialize the data import page.
        :param controller: the parent controller of this object
        """
        self.controller = controller
        self.data = data

        self.page = DataImportPage(self)
        self.page.run()

    def import_from_file(self, event):
        """
        Import tabular data from a file
        """
        file = filedialog.askopenfile(filetypes=[('csv', '*.csv'), ('tsv', '*.tsv')])
        self.data.import_from_file(file)

    def export_to_file(self, event):
        """
        Export the currently in use data to a file
        """
        file = filedialog.asksaveasfile(defaultextension='csv')
        self.data.export_to_file(file)

    def return_home(self, event):
        """
        Return to the main page
        """
        self.controller.return_home(event)


def main():
    """
    The main entry point for the application.

    Also serves as a console-entry point via command OCMhap.
    """
    data = DataObject()
    controller = MainController(data)
    controller.gogogo()
    sys.exit(0)


if __name__ == "__main__":
    main()

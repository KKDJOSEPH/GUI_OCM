import sys
import webbrowser

from OCMhap.gui.DataImportPage import DataImportPage
from OCMhap.gui.MainPage import MainPage


class MainController(object):
    """
    A GUIController represents a controller for the GUI of the
    OCM Advisory Health Analytics Platform.
    """
    def __init__(self):
        """
        Initialize the GUIController by initializing its component frames.
        """
        self.page = MainPage(self)

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
        controller = DataImportController(self)

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
    def __init__(self, controller):
        """
        Initialize the data import page.
        :param controller: the parent controller of this object
        """
        self.controller = controller

        self.page = DataImportPage(self)
        self.page.run()

    def import_from_file(self, event):
        """
        Import additional data from a file
        """
        pass

    def import_manually(self, event):
        """
        Import data by entering into corresponding text boxes
        """
        pass

    def view_data(self, event):
        """
        View the data currently in use by the application
        """
        pass

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
    controller = MainController()
    controller.gogogo()
    sys.exit(0)


if __name__ == "__main__":
    main()

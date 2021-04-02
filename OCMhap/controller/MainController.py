import sys
import tkinter
import webbrowser

from OCMhap.DataObject import DataObject
from OCMhap.controller.AnalysisController import AnalysisController
from OCMhap.gui.MainFrame import MainFrame


class MainController(object):
    """
    A GUIController represents a controller for the GUI of the
    OCM Advisory Health Analytics Platform.
    """

    def __init__(self, root, data):
        """
        Initialize the GUIController by initializing its component frames.
        :param root: the root tk interpreter.
        :param data:
        """
        self.page = MainFrame(root, self)
        self.data = data

    def analysis(self):
        """
        Serve the analysis import interface.
        """
        self.page.stop()
        AnalysisController(self, self.data)

    def about(self):
        """
        Fetch the OCM advisory webpage.
        """
        webbrowser.open("https://ocmadvisory.com/", new=0)

    def help(self):
        """
        Provide help information regarding the application
        """
        self.page.dialog_box('For app related questions or problems please email Haoyang Ding at \n'
                             'ding.haoya@northeastern.edu')

    def return_home(self):
        """
        Return to the main page from a separate window
        """
        self.page = MainFrame(self)
        self.page.run()

    def gogogo(self):
        """Start the application"""
        self.page.run()


def main():
    """
    The main entry point for the application.

    Also serves as a console-entry point via command OCMhap.
    """
    root = tkinter.Tk()
    data = DataObject()
    controller = MainController(root, data)
    controller.gogogo()
    sys.exit(0)


if __name__ == "__main__":
    main()

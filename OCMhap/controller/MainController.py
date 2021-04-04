import sys
import webbrowser

from OCMhap.DataObject import DataObject
from OCMhap.controller.AnalysisController import AnalysisController
from OCMhap.gui.MainFrame import MainFrame
from OCMhap.gui.RootFrame import RootFrame


class MainController(object):
    """
    A GUIController represents a controller for the GUI of the
    OCM Advisory Health Analytics Platform.
    """

    def __init__(self, data):
        """
        Initialize the GUIController by initializing its component frames.
        :param data:
        """
        self.data = data

        self.root = RootFrame()

        self.frame = MainFrame(self.root, self)
        self.analysis_controller = AnalysisController(self.root, self, self.data)
        self.analysis_controller.hide()

    def display(self):
        """Display the main frame"""
        self.frame.display()

    def hide(self):
        """Hide the main frame"""
        self.frame.hide()

    def analysis(self):
        """
        Serve the analysis import interface.
        """
        self.hide()
        self.analysis_controller.display()

    def about(self):
        """
        Fetch the OCM advisory webpage.
        """
        webbrowser.open("https://ocmadvisory.com/", new=0)

    def help(self):
        """
        Provide help information regarding the application
        """
        self.frame.dialog_box('For app related questions or problems please email Haoyang Ding at \n'
                              'ding.haoya@northeastern.edu')

    def return_home(self):
        """
        Return to the main page from a separate window
        """
        self.display()

    def gogogo(self):
        """Start the application"""
        self.display()
        self.root.mainloop()


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

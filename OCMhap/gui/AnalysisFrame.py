import tkinter
from pandastable import Table
import matplotlib

from OCMhap.gui.AbstractOCMFrame import AbstractOCMFrame

matplotlib.use('TkAgg')


class AnalysisFrame(AbstractOCMFrame):
    """
    An AnlysisFrame represents a frame for doing analysis in the OCM
    advisory health analytics platform.
    """
    WIDTH = 900
    HEIGHT = 600

    canvas_width = 660
    canvas_height = 500

    def __init__(self, root, controller, data):
        """
        Initialize an AnalysisFrame.
        :param controller: the controller controlling this frame
        :param data: the data object
        """
        super().__init__(root)

        self.controller = controller
        self.data = data

        self.dataBt = tkinter.Button(self, text="Import Data",
                                     height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                     command=self.import_data)
        self.dataBt.pack(expand=True, anchor=tkinter.CENTER)

        self.backBt = tkinter.Button(self, text="Back",
                                     height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                     command=self.return_home)
        self.backBt.pack(expand=True, anchor=tkinter.CENTER)

        self.canvas = tkinter.Canvas(self, bg="gray89",
                                     height=self.canvas_height, width=self.canvas_width)
        self.canvas.pack(expand=True, anchor=tkinter.CENTER)
        self.canvas_frame = tkinter.Frame(self.canvas)
        self.canvas_frame.pack(fill=tkinter.BOTH, expand=1)

        self.pack(expand=True, anchor=tkinter.CENTER)

    def import_data(self):
        """Import data into the model"""
        self.controller.import_data(self.data)

    def refresh(self):
        """Refresh the contents displayed on this page"""
        table = Table(self.canvas_frame, dataframe=self.data.data,
                      showtoolbar=True, showstatusbar=True)
        table.show()

    def return_home(self):
        """Return to the home page"""
        self.controller.return_home()

import tkinter as tk
from tkinter import *
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

    def __init__(self, controller, data):
        """
        Initialize an AnalysisFrame.
        :param controller: the controller controlling this frame
        :param data: the data object
        """
        super().__init__()

        self.controller = controller
        self.data = data

        self.frame.geometry("{}x{}".format(self.WIDTH, self.HEIGHT))

        self.dataBt = tk.Button(self.frame, text="Import Data",
                                height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                command=self.import_data)
        self.dataBt.place(x=10, y=80)

        self.backBt = tk.Button(self.frame, text="Back",
                                height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                command=self.return_home)
        self.backBt.place(x=10, y=550)

        self.canvas = tk.Canvas(self.frame, bg="gray89",
                                height=self.canvas_height, width=self.canvas_width)
        self.canvas.place(x=200, y=10)
        self.canvas_frame = Frame(self.canvas)
        self.canvas_frame.pack(fill=BOTH, expand=1)

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

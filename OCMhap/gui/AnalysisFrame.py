import tkinter
from pandastable import Table

from OCMhap.gui.AbstractOCMFrame import AbstractOCMFrame


class AnalysisFrame(AbstractOCMFrame):
    """
    An AnlysisFrame represents a frame for doing analysis in the OCM
    advisory health analytics platform.
    """

    def __init__(self, root, controller, data):
        """
        Initialize an AnalysisFrame.
        :param controller: the controller controlling this frame
        :param data: the data object
        """
        super().__init__(root)

        self.controller = controller
        self.data = data

        self.grid(sticky="NESW")

        # The frame on which to place the pandas Table
        self.table_frame = tkinter.Frame(self, relief=tkinter.RAISED, borderwidth=1)
        self.table_frame.grid(column=1, row=1, columnspan=5, rowspan=5, sticky="NESW",
                              padx=self.PADDING, pady=self.PADDING)

        self.table = Table(self.table_frame, dataframe=self.data.data,
                           showtoolbar=True, showstatusbar=True)
        self.table.show()

        # The frame on which to place the import data and back buttons
        self.data_frame = tkinter.Frame(self)
        self.data_frame.grid(column=0, row=0, columnspan=1, rowspan=5, sticky="NESW",
                             padx=self.PADDING, pady=self.PADDING)

        # The data import button
        self.dataBt = tkinter.Button(self.data_frame, text="Import Data",
                                     height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                     command=self.import_data)
        self.dataBt.grid(column=0, row=0, padx=self.PADDING, pady=self.PADDING)

        # The back button
        self.backBt = tkinter.Button(self.data_frame, text="Back",
                                     height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                     command=self.return_home)
        self.backBt.grid(column=0, row=1, padx=self.PADDING, pady=self.PADDING)

        # The frame on which to place the animated map controls
        self.map_frame = tkinter.Frame(self, relief=tkinter.RAISED, borderwidth=1,
                                       padx=5, pady=5)
        self.map_frame.grid(column=1, row=6, columnspan=5, rowspan=1, sticky="NESW",
                            padx=self.PADDING, pady=self.PADDING)

        self.mapBt = tkinter.Button(self.map_frame, text="Generate Map",
                                    height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                    command=self.return_home)
        self.mapBt.grid(column=0, row=0, padx=self.PADDING, pady=self.PADDING)

    def import_data(self):
        """Import data into the model"""
        self.controller.import_data(self.data)

    def refresh(self):
        """Refresh the contents displayed on this page"""
        self.table.model.df = self.data.data
        self.table.redraw()

    def return_home(self):
        """Return to the home page"""
        self.controller.return_home()

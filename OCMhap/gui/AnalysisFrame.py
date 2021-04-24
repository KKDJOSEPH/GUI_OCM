import tkinter
from tkinter.ttk import Combobox
import pandastable

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

        self.table = pandastable.Table(self.table_frame, dataframe=self.data.data,
                                       showtoolbar=True, showstatusbar=True)
        self.table.show()

        # The frame on which to place the import data and back buttons
        self.data_frame = tkinter.Frame(self)
        self.data_frame.grid(column=0, row=0, columnspan=1, rowspan=5, sticky="NESW",
                             padx=self.PADDING, pady=self.PADDING)

        # The data import button
        self.data_button = tkinter.Button(self.data_frame, text="Import Data",
                                          height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                          command=self.import_data)
        self.data_button.grid(column=0, row=0, padx=self.PADDING, pady=self.PADDING)

        # The back button
        self.back_button = tkinter.Button(self.data_frame, text="Back",
                                          height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                          command=self.return_home)
        self.back_button.grid(column=0, row=1, padx=self.PADDING, pady=self.PADDING)

        # The frame on which to place the animated map controls
        self.map_frame = tkinter.LabelFrame(self, relief=tkinter.RAISED, borderwidth=1,
                                            padx=5, pady=5, text="Animated Map")
        self.map_frame.grid(column=1, row=6, columnspan=5, rowspan=1, sticky="NESW",
                            padx=self.PADDING, pady=self.PADDING)

        self.map_button = tkinter.Button(self.map_frame, text="Generate Map",
                                         height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                         command=self.controller.map)
        self.map_button.grid(column=0, row=0, padx=self.PADDING, pady=self.PADDING)

        self.map_combo_box_frame = tkinter.Frame(self.map_frame, padx=5, pady=5)
        self.map_combo_box_frame.grid(column=1, row=0, padx=self.PADDING, pady=self.PADDING)

        self.map_combo_box_label = tkinter.Label(self.map_combo_box_frame, text="Data to Map:",
                                                 padx=5, pady=5)
        self.map_combo_box_label.grid(column=0, row=0, padx=self.PADDING, pady=self.PADDING)

        self.map_combo_box = Combobox(self.map_combo_box_frame, values=self.data.attributes,
                                      height=10, width=self.BUTTON_WIDTH,
                                      postcommand=self.refresh_combo_box)
        self.map_combo_box.grid(column=0, row=1, padx=self.PADDING, pady=self.PADDING)

        self.help_button = tkinter.Button(self.map_frame, text="Help",
                                          height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                          command=self.controller.map_help)
        self.help_button.grid(column=2, row=0, padx=self.PADDING, pady=self.PADDING)

    def import_data(self):
        """Import data into the model"""
        file = tkinter.filedialog.askopenfile(filetypes=[('csv', '*.csv'), ('tsv', '*.tsv')])
        self.controller.import_data(self.data, file)

    def refresh_combo_box(self):
        self.map_combo_box["values"] = self.data.attributes

    def refresh(self):
        """Refresh the contents displayed on this page"""
        self.table.model.df = self.data.data
        self.table.redraw()
        self.refresh_combo_box()

    def return_home(self):
        """Return to the home page"""
        self.controller.return_home()

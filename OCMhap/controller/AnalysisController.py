from OCMhap.gui.AnalysisFrame import AnalysisFrame
from OCMhap.gui.Map import AnimatedMapController


class AnalysisController(object):
    """
    An AnalysisController is a controller for the analysis page in
    """

    def __init__(self, root, controller, data):
        """
        Initialize the AnalysisController.
        :param root: the root frame.
        :param controller: the main controller responsible for this controller.
        :param data: the data object.
        """
        self.controller = controller
        self.data = data
        self.frame = AnalysisFrame(root, self, data=data)
        self.map_controller = AnimatedMapController(self, self.data)

    def display(self):
        """Display the main frame"""
        self.frame.display()

    def hide(self):
        """Hide the main frame"""
        self.frame.hide()

    def import_data(self, data, file):
        """
        Import data into the provided data object.
        :param data: the data object to import data into
        :param file: the file to import data from
        """
        if file is None:
            return
        data.import_from_file(file)
        self.frame.refresh()

    def return_home(self):
        """
        Return to the main page
        """
        self.hide()
        self.controller.return_home()

    def message(self, text):
        """
        Display the text as an infobox message.
        :param text: the text to display.
        """
        self.frame.dialog_box(text)

    def map(self):
        """
        Generate an animated map using the current data and the selected
        column.
        """
        self.map_controller.column_name = self.frame.map_combo_box.get()

    def map_help(self):
        """
        Display help for the map widget.
        """
        self.frame.dialog_box("Generate an Animated Map using the selected column. "
                              "The data must have the following columns: "
                              "FIPS_County_Code, Year.")

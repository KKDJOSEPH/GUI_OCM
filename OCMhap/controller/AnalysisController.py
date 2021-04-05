from OCMhap.gui.AnalysisFrame import AnalysisFrame


class AnalysisController(object):
    """
    An AnalysisController is a controller for the analysis page in
    """

    def __init__(self, root, controller, data):
        """
        Initialize the AnalysisController.
        :param root:
        :param controller:
        :param data:
        """
        self.controller = controller
        self.data = data
        self.frame = AnalysisFrame(root, self, data=data)

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

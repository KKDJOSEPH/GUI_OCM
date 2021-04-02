from tkinter import filedialog

from OCMhap.gui.AnalysisFrame import AnalysisFrame


class AnalysisController(object):

    def __init__(self, controller, data):
        """
        Initialize the GUIController by initializing its component frames.
        """

        self.controller = controller
        self.data = data
        self.page = AnalysisFrame(self, data=data)
        self.page.run()

    def import_data(self, data):
        """
        Import data into the provided data object.
        :param data: the data object to import data into
        """
        file = filedialog.askopenfile(filetypes=[('csv', '*.csv'), ('tsv', '*.tsv')])
        if file is None:
            return
        data.import_from_file(file)
        self.page.refresh()

    def return_home(self):
        """
        Return to the main page
        """
        self.page.stop()
        self.controller.return_home()

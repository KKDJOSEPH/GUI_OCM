import tkinter as tk

import pkg_resources


class DataImportPage(object):
    """
    A DataImportPage represents the data import screen for the OCM Advisory
    Health Analytics Platform.
    """
    def __init__(self, controller):
        """
        Initialize the DataImportPage.

        Tha DataImportPage includes options to import data from a file or
        to manually enter data. It also incldues an option to view the
        data that is present.

        :param controller: the controller handling events on this page
        """
        self.controller = controller

        self.frame = tk.Tk()
        self.frame.title("OCM Advisory Health Analytics Platform")
        self.frame.geometry("300x300")
        self.frame.iconphoto(True, tk.PhotoImage(
            file=pkg_resources.resource_filename(__name__, "../resources/images/ocm_icon.png")
        ))

        self.analysisBt = tk.Button(self.frame, text="Import From File", height=3, width=18)
        self.analysisBt.pack(expand=True, anchor=tk.CENTER)
        self.analysisBt.bind("<Button-1>", self.import_from_file)

        self.dataBt = tk.Button(self.frame, text="Export To File", height=3, width=18)
        self.dataBt.pack(expand=True, anchor=tk.CENTER)
        self.dataBt.bind("<Button-1>", self.export_to_file)

        self.aboutBt = tk.Button(self.frame, text="Back", height=3, width=18)
        self.aboutBt.pack(expand=True, anchor=tk.CENTER)
        self.aboutBt.bind("<Button-1>", self.return_home)

        self.frame.mainloop()

    def run(self):
        """Display this page"""
        self.frame.mainloop()

    def stop(self):
        """Disable this page"""
        self.frame.destroy()

    def import_from_file(self, event):
        """Import data from a file"""
        self.controller.import_from_file(event)

    def export_to_file(self, event):
        """Export data to a file"""
        self.controller.export_to_file(event)

    def return_home(self, event):
        """Return to the home page"""
        self.frame.destroy()
        self.controller.return_home(event)

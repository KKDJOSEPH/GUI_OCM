from tkinter import *
import tkinter as tk
import pkg_resources


class MainPage(object):
    """
    A MainPage represents the main page for the OCM Advisory
    Health Analytics Platform.
    """
    def help(self, event):
        self.controller.help(event)

    def __init__(self, controller):
        """
        Initialize the MainPage.

        Tha MainPage includes the OCM Advisory logo, as well as buttons
        for data import, analysis, and about.

        :param controller: the controller handling events on this page
        """
        self.controller = controller

        self.frame = tk.Tk()
        self.frame.title("OCM Advisory Health Analytics Platform")
        self.frame.geometry("500x300")
        self.frame.iconphoto(True, tk.PhotoImage(
            file=pkg_resources.resource_filename(__name__, "../resources/images/ocm_icon.png")
        ))

        self.photo = tk.PhotoImage(
            file=pkg_resources.resource_filename(__name__, "../resources/images/ocm_logo.png")
        )
        self.imgLabel = tk.Label(self.frame, image=self.photo)
        self.imgLabel.pack(expand=True, anchor=tk.CENTER)

        self.analysisBt = tk.Button(self.frame, text="Analysis", height=3, width=18)
        self.analysisBt.pack(expand=True, anchor=tk.CENTER)
        self.analysisBt.bind("<Button-1>", self.analysis)

        self.aboutBt = tk.Button(self.frame, text="OCM Website", height=3, width=18)
        self.aboutBt.pack(expand=True, anchor=tk.CENTER)
        self.aboutBt.bind("<Button-1>", self.about)

        # Add Help Button Feature
        self.helpBt = tk.Button(self.frame, text="Help", height=1, width=6)
        self.helpBt.place(relx=.85, rely=.01)
        self.helpBt.bind("<Button-1>", self.help)

    def run(self):
        """Display this page"""
        self.frame.mainloop()

    def stop(self):
        """Disable this page"""
        self.frame.destroy()

    def analysis(self, event):
        """The analysis button was clicked"""
        self.controller.analysis(event)

    def data_import(self, event):
        """The data import button was clicked"""
        self.controller.data_import(event)

    def about(self, event):
        """The about button was clicked"""
        self.controller.about(event)




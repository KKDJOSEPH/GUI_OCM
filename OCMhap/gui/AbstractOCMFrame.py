from abc import ABC

import tkinter.messagebox
import tkinter as tk

import pkg_resources


class AbstractOCMFrame(ABC):
    """
    An AbstractOCMFrame is a Frame in the OCM advisory health analytics
    platform.
    """

    DEFAULT_HEIGHT = 500
    DEFAULT_WIDTH = 300

    BUTTON_WIDTH = 18
    BUTTON_HEIGHT = 3

    def __init__(self, root):
        """
        Initialize an AbstractOCMFrame with a default height and width,
        as well as a title and an icon photo

        :param root: the root tk interpreter
        """
        self.root = root
        self.root.title("OCM Advisory Health Analytics Platform")
        self.root.geometry("{}x{}".format(self.DEFAULT_HEIGHT, self.DEFAULT_WIDTH))
        self.root.iconphoto(True, tk.PhotoImage(
            file=pkg_resources.resource_filename(__name__, "../resources/images/ocm_icon.png")
        ))

        self.frame = tk.Frame(self.root)

    def run(self):
        """Display this page"""
        self.root.mainloop()

    def stop(self):
        """Disable this page"""
        self.root.destroy()

    def dialog_box(self, message):
        """Display the provided message in a dialog box"""
        tkinter.messagebox.showinfo(message=message)

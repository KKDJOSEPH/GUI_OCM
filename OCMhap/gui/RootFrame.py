import tkinter

import pkg_resources


class RootFrame(tkinter.Tk):
    """
    A RootFrame represents the root window of the OCM application.
    """
    def __init__(self):
        """
        Initialize the RootFrame.
        """
        super().__init__()
        self.title("OCM Advisory Health Analytics Platform")
        self.iconphoto(True, tkinter.PhotoImage(
            file=pkg_resources.resource_filename(__name__, "../resources/images/ocm_icon.png")
        ))

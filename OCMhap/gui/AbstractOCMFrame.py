import tkinter.messagebox
import tkinter


class AbstractOCMFrame(tkinter.Frame):
    """
    An AbstractOCMFrame is a Frame in the OCM advisory health analytics
    platform.
    """

    BUTTON_WIDTH = 18
    BUTTON_HEIGHT = 3

    PADDING = 3

    def __init__(self, master):
        """
        Initialize an AbstractOCMFrame.

        :param master: the master of this frame
        """
        super().__init__(master)

    def display(self):
        """Display this frame"""
        self.grid()

    def hide(self):
        """Hide this frame"""
        self.grid_remove()

    def dialog_box(self, message):
        """Display the provided message in a dialog box"""
        tkinter.messagebox.showinfo(message=message)

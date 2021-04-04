import tkinter.messagebox
import tkinter


class AbstractOCMFrame(tkinter.Frame):
    """
    An AbstractOCMFrame is a Frame in the OCM advisory health analytics
    platform.
    """

    BUTTON_WIDTH = 18
    BUTTON_HEIGHT = 3

    def __init__(self, root):
        """
        Initialize an AbstractOCMFrame with a default height and width,
        as well as a title and an icon photo

        :param root: the root tk interpreter
        """
        super().__init__(root)

    def display(self):
        """Display this frame"""
        # self.pack(expand=True, anchor=tk.CENTER)
        self.pack()

    def hide(self):
        """Hide this frame"""
        self.pack_forget()

    def dialog_box(self, message):
        """Display the provided message in a dialog box"""
        tkinter.messagebox.showinfo(message=message)

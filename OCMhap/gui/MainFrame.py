import tkinter
import pkg_resources

from OCMhap.gui.AbstractOCMFrame import AbstractOCMFrame


class MainFrame(AbstractOCMFrame):
    """
    A MainPage represents the main page for the OCM Advisory
    Health Analytics Platform.
    """

    def __init__(self, root, controller):
        """
        Initialize the MainPage.

        Tha MainPage includes the OCM Advisory logo, as well as buttons
        for data import, analysis, and about.

        :param root: the root tk interpreter
        :param controller: the controller handling events on this page
        """
        super().__init__(root)

        self.controller = controller

        self.photo = tkinter.PhotoImage(
            file=pkg_resources.resource_filename(__name__, "../resources/images/ocm_logo.png")
        )
        self.imgLabel = tkinter.Label(self, image=self.photo)
        self.imgLabel.pack(expand=True, anchor=tkinter.CENTER)

        self.analysisBt = tkinter.Button(self, text="Analysis",
                                         height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                         command=self.analysis)
        self.analysisBt.pack(expand=True, anchor=tkinter.CENTER)

        self.aboutBt = tkinter.Button(self, text="OCM Website",
                                      height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,
                                      command=self.about)
        self.aboutBt.pack(expand=True, anchor=tkinter.CENTER)

        self.helpBt = tkinter.Button(self, text="Help",
                                     height=round(self.BUTTON_HEIGHT/3)+1, width=round(self.BUTTON_WIDTH/3),
                                     command=self.help)
        self.helpBt.pack(expand=True, anchor=tkinter.CENTER, pady=10)

        # self.pack(expand=True, anchor=tkinter.CENTER)
        self.pack()

    def help(self):
        """Provide the help dialog"""
        self.controller.help()

    def analysis(self):
        """The analysis button was clicked"""
        self.controller.analysis()

    def about(self):
        """The about button was clicked"""
        self.controller.about()




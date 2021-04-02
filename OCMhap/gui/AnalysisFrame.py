import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pandastable import Table, TableModel
import pkg_resources
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd


class AnalysisFrame(object):
    window_width = 900
    window_height = 600
    canvas_width = 660
    canvas_height = 500

    def __init__(self, controller, data):
        self.controller = controller
        self.data
        self.width = self.window_width
        self.height = self.window_height
        self.frame = tk.Tk()
        self.frame.title("OCM Advisory Health Analytics Platform")
        self.frame.geometry("900x600")

        self.scatterBt = tk.Button(self.frame, text="Scatter Plot", height=3, width=18)
        # self.scatterBt.place(x=10, y=10)
        self.scatterBt.place(relx=.01, rely=.01)
        self.scatterBt.bind("<Button-1>", self.scatterPlot)

        self.dataBt = tk.Button(self.frame, text="Import Data", height=3, width=18,
                                command=self.call_cancvas)
        self.dataBt.place(x=10, y=80)
        # self.dataBt.bind("<Button-1>", self.call_cancvas)

        # self.mapBt = tk.Button(self.frame, text="Interactive Map", height=3, width=18.,
        #                        command = print(self.data))
        # self.mapBt.place(x=10, y=150)
        # # self.aboutBt.bind("<Button-1>", self.about)

        self.backBt = tk.Button(self.frame, text="Back", height=2, width=14)
        self.backBt.place(x=10, y=550)
        self.backBt.bind("<Button-3>", self.return_home)

    def run(self):
        """Display this page"""
        self.frame.mainloop()

    def stop(self):
        """Disable this page"""
        self.frame.destroy()

    def call_cancvas(self):
        self.create_canvas(tk.Canvas(self.frame, bg="gray89", height=self.canvas_height, width=self.canvas_width))

    def create_canvas(self, canvas):
        canvas.place(x=200, y=10)

        f = Frame(canvas)
        f.pack(fill=BOTH, expand=1)
        file = filedialog.askopenfile(filetypes=[('csv', '*.csv'), ('tsv', '*.tsv')])
        if file is None:
            return
        df = pd.read_csv(file)
        self.data = df
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()

    def return_home(self, event):
        """Return to the home page"""
        self.frame.destroy()
        self.controller.return_home(event)

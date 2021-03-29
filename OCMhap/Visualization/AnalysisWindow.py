import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pandastable import Table, TableModel
import pkg_resources
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd


class AnalysisWindow(object):
    window_width = 900
    window_height = 600
    canvas_width = window_width - 200
    canvas_height = window_height - 100

    def __init__(self, controller):
        self.controller = controller
        self.width = self.window_width
        self.height = self.window_height
        self.frame = tk.Tk()
        self.frame.title("OCM Advisory Health Analytics Platform")
        self.frame.geometry("{}x{}".format(self.window_width, self.window_height))

        self.dataBt = tk.Button(self.frame, text="Import Data", height=3, width=18)
        self.dataBt.place(relx=.01, rely=.01)
        self.dataBt.bind("<Button-1>", self.create_canvas)

        self.backBt = tk.Button(self.frame, text="Back", height=2, width=14)
        self.backBt.place(relx=.01, rely=.92)
        self.backBt.bind("<Button-1>", self.return_home)

    def run(self):
        """Display this page"""
        self.frame.mainloop()

    def stop(self):
        """Disable this page"""
        self.frame.destroy()

    def create_variable_lists(self, df):
        chosen_vars = []

        def store_var_1(variable1):
            chosen_vars.append(variable1)

            default_menu_option2 = StringVar(self.frame)
            default_menu_option2.set("Select Variable 2")

            second_var_menu = OptionMenu(self.frame, default_menu_option2, *vars, command=store_var_2)
            second_var_menu.place(x=10, y=160)

        def store_var_2(variable2):
            chosen_vars.append(variable2)
            ###GRAPH

        default_menu_option1 = StringVar(self.frame)
        default_menu_option1.set("Select Variable 1")

        vars = df.columns

        first_var_menu = OptionMenu(self.frame, default_menu_option1, *vars, command=store_var_1)
        first_var_menu.place(x=10, y=130)

    def create_canvas(self, event):
        canvas = (tk.Canvas(self.frame, bg="gray89", height=self.canvas_height, width=self.canvas_width))

        canvas.place(x=300, y=10)

        f = Frame(canvas)
        f.pack(fill=BOTH, expand=1)
        file = filedialog.askopenfile(filetypes=[('csv', '*.csv'), ('tsv', '*.tsv')])
        if file is None:
            return
        df = pd.read_csv(file)
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()

        analysis_types = ("Scatter Plot", "Principal Component Analysis", "Bar Chart", "Interactive Map")

        variable = StringVar(self.frame)
        variable.set("Select the analysis option")  # default value

        self.drop_menu = OptionMenu(self.frame, variable, *analysis_types, command=self.create_variable_lists(df))
        self.drop_menu.place(x=10, y=80)


    def scatterPlot(self, file='/OCMhap/resources/data/data.csv', variable1='Suicide', variable2='Asthma'):
        """
        PLACE HOLDER FOR SCATTER PLOT
            fig = Figure(figsize=(6, 6),
                         dpi=100)

            # list of squares
            y = [i ** 2 for i in range(101)]

            # adding the subplot
            plot1 = fig.add_subplot(111)

            # plotting the graph
            plot1.plot(y)

            # creating the Tkinter canvas
            # containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(fig,
                                       master=self.frame)
            canvas.draw()
            canvas.get_tk_widget().pack()
        """

    def return_home(self, event):
        """Return to the home page"""
        self.frame.destroy()
        self.controller.return_home(event)

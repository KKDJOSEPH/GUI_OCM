import tkinter as tk
import os


# TODO: Create a visualization page
# TODO: Create visualizations to display
# https://datatofish.com/matplotlib-charts-tkinter-gui/
# above link provides demonstration of using matplotlib along with tkinter
class visual(object):
    def __init__(self):
        self.frame = tk.Toplevel()
        self.frame.title("OCM advisory")
        self.frame.geometry("500x300")

        self.photo = tk.PhotoImage(file="./images/ocm_logo.png")
        self.imgLabel = tk.Label(self.frame, image=self.photo)
        self.imgLabel.grid(row=0, column=1, sticky="")

        self.v1 = tk.Button(self.frame, text="Method 1", height=4, width=12)
        self.v1.grid(row=1, column=0, sticky="w")
        self.v1.bind("<Button-1>", self.visual1)

        self.v2 = tk.Button(self.frame, text="Method 2", height=4, width=12)
        self.v2.grid(row=1, column=3, sticky="e")
        self.v2.bind("<Button-1>", self.visual2)

        self.v3 = tk.Button(self.frame, text="Method 3", height=4, width=12)
        self.v3.grid(row=2, column=0, sticky="w")
        self.v3.bind("<Button-1>", self.visual3)

        self.v4 = tk.Button(self.frame, text="Method 4", height=4, width=12)
        self.v4.grid(row=2, column=3, sticky="e")
        self.v4.bind("<Button-1>", self.visual4)

    def run(self):
        self.frame.mainloop()

    def visual1(self, event):
        path = os.path.dirname(os.path.realpath(__file__))
        print(path)
        path2 = path + r"\images\Chinaco2emission-gdp.png"
        print(path2)
        os.system(path2)

    def visual2(self, event):
        path = os.path.dirname(os.path.realpath(__file__))
        print(path)
        path2 = path + r"\images\developed-ing.jpg"
        print(path2)
        os.system(path2)

    def visual3(self, event):
        path = os.path.dirname(os.path.realpath(__file__))
        print(path)
        path2 = path + r"\images\wordcloud.jpg"
        print(path2)
        os.system(path2)

    def visual4(self, event):
        path = os.path.dirname(os.path.realpath(__file__))
        print(path)
        path2 = path + r"\images\treemap.html"
        print(path2)
        os.system(path2)


if __name__ == '__main__':
    mp = visual()
    mp.run()

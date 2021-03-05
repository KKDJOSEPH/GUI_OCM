from tkinter import *
import tkinter as tk
import webbrowser
import FilePage

class mainpage(object):
    def __init__(self):
        self.frame = tk.Tk()
        self.frame.title("OCM advisory")
        self.frame.geometry("500x300")
        self.frame.iconphoto(True, tk.PhotoImage(file = "./images/ocm_icon.png"))

        self.photo = tk.PhotoImage(file="./images/ocm_logo.png")
        self.imgLabel = tk.Label(self.frame, image = self.photo)
        self.imgLabel.pack(expand = True, anchor = CENTER)

        self.startBt = tk.Button(self.frame, text = "Start", height = 4, width = 18)
        self.startBt.pack(expand = True, anchor = CENTER)
        self.startBt.bind("<Button-1>", self.redirect)

        self.aboutBt = tk.Button(self.frame, text = "About", height = 4, width = 18)
        self.aboutBt.pack(expand = True, anchor = CENTER)
        self.aboutBt.bind("<Button-1>", self.about)

    def run(self):
        self.frame.mainloop()

    def about(self, event):
        webbrowser.open("https://ocmadvisory.com/", new=0)

    def redirect(self, event):
        self.frame.destroy()
        app = FilePage.Application()
        app.addmenu(FilePage.MyMenu)
        app.mainloop()

if __name__ == '__main__':

    mp = mainpage()
    mp.run()
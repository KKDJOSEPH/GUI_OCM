import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import Visualizations


# TODO: Refactor to enable data import from file
# add a corresponding controller for this page as well
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.createWidgets()

    def createWidgets(self):
        self.title('Select Files')
        self.columnconfigure(0, minsize=50)

        self.entryvar = tk.StringVar()
        self.keyvar = tk.StringVar()
        self.keyvar.set('KeyWord')
        items = ['.xlsx', '.py', '.png', '.json', '.csv']
        topframe = tk.Frame(self, height=80)
        contentframe = tk.Frame(self)
        topframe.pack(side=tk.TOP)
        contentframe.pack(side=tk.TOP)

        glabel = tk.Label(topframe, text='Current folder:')
        gentry = tk.Entry(topframe, textvariable=self.entryvar)
        gbutton = tk.Button(topframe, command=self.__opendir, text='Choose')
        gcombobox = ttk.Combobox(topframe, values=items, textvariable=self.keyvar)

        gentry.bind('<Return>', func=self.__refresh)

        glabel.grid(row=0, column=0, sticky=tk.W)
        gentry.grid(row=0, column=1)
        gbutton.grid(row=0, column=2)
        gcombobox.grid(row=0, column=3)

        rightbar = tk.Scrollbar(contentframe, orient=tk.VERTICAL)
        bottombar = tk.Scrollbar(contentframe, orient=tk.HORIZONTAL)
        self.textbox = tk.Text(contentframe, yscrollcommand=rightbar.set, xscrollcommand=bottombar.set)

        rightbar.pack(side=tk.RIGHT, fill=tk.Y)
        bottombar.pack(side=tk.BOTTOM, fill=tk.X)
        self.textbox.pack(side=tk.LEFT, fill=tk.BOTH)

        rightbar.config(command=self.textbox.yview)
        bottombar.config(command=self.textbox.xview)

    def __opendir(self):

        self.textbox.delete('1.0', tk.END)
        self.dirname = filedialog.askdirectory()
        self.entryvar.set(self.dirname)
        if not self.dirname:
            messagebox.showwarning('Warning', message='Choose a folder first！')
        self.dirlist = os.listdir(self.entryvar.get())
        for eachdir in self.dirlist:
            self.textbox.insert(tk.END, eachdir + '\r\n')
        self.textbox.update()

    def __refresh(self, event=None):

        self.textbox.delete('1.0', tk.END)
        self.dirlist = os.listdir(self.entryvar.get())
        for eachdir in self.dirlist:
            self.textbox.insert(tk.END, eachdir + '\r\n')
        self.textbox.update()

    def addmenu(self, Menu):
        Menu(self)


class MyMenu():

    def __init__(self, root):
        self.menubar = tk.Menu(root)

        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.file_open)
        filemenu.add_command(label="New", command=self.file_new)
        filemenu.add_command(label="Save", command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        editmenu = tk.Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=self.edit_cut)
        editmenu.add_command(label="Copy", command=self.edit_copy)
        editmenu.add_command(label="Paste", command=self.edit_paste)

        helpmenu = tk.Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.help_about)

        funcmenu = tk.Menu(self.menubar, tearoff=0)
        funcmenu.add_command(label="Visual", command=self.func_redirect)
        funcmenu.add_command(label="Map", command=self.func_map)

        self.menubar.add_cascade(label="File", menu=filemenu)
        self.menubar.add_cascade(label="Edit", menu=editmenu)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        self.menubar.add_cascade(label="Func", menu=funcmenu)
        root.config(menu=self.menubar)

    def file_open(self):
        messagebox.showinfo('Open', 'File-Open！')
        pass

    def file_new(self):
        messagebox.showinfo('New', 'File-New！')
        pass

    def file_save(self):
        messagebox.showinfo('Save', 'File-Save！')
        pass

    def edit_cut(self):
        messagebox.showinfo('Cut', 'Edit-Cut！')
        pass

    def edit_copy(self):
        messagebox.showinfo('Copy', 'Edit-Copy！')
        pass

    def edit_paste(self):
        messagebox.showinfo('Paste', 'Edit-Paste！')
        pass

    def help_about(self):
        messagebox.showinfo('About',
                            'Author：Hoayang Ding \n verion 1.0 \n Thank you for using it！ \n ding.haoya@northeastern.edu')

    def func_redirect(self):
        mp = Visualizations.visual()
        mp.run()

    def func_map(self):
        path = os.path.dirname(os.path.realpath(__file__))
        print(path)
        path2 = path + r"\images\temperature_map.gif"
        print(path2)
        os.system(path2)


if __name__ == '__main__':
    app = Application()
    app.addmenu(MyMenu)
    app.mainloop()

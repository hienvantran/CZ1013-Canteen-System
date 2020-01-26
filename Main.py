import tkinter as tk                # import tkinter
from tkinter import font as tkfont  # import font
from PIL import ImageTk, Image
from time import strftime
from datetime import date
import subprocess
from tkinter import font as tkfont
from tkinter import messagebox
from menu import *
from startPage import *
from mainpage import *
from MyDatePicker import *
from startPage1 import *



import sys

class Base(tk.Tk):  # class to put your method/function and inherit tk.TK

    # init - initilise use __init__, following strong convention, can pass anything, dictionary
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)  # initialise Tkinter
        
        self.title_font = tkfont.Font(family='Café Françoise', size=10, weight="bold", slant="italic")
        self.title_font1 = tkfont.Font(family='Café Françoise', size=20, weight="bold", slant="italic")
        self.sentence_font = tkfont.Font(family='Café Françoise', size=10, weight="bold", slant="italic")
        self.stall_font = tkfont.Font(family='Café Françoise', size=40, weight="bold")
        self.mainpage_font = tkfont.Font(family='Café Françoise', size=50, weight="bold")
        self.time_font = tkfont.Font(family='Café Françoise', size=10)
        self.select_time_date=tkfont.Font(family='Café Françoise', size=30)
        self.select_timedate=tkfont.Font(family='Café Françoise', size=20)
        self.date_smallfont=tkfont.Font(family='Café Françoise', size=20)
        self.button =tkfont.Font(family='Café Françoise',size=14)
        self.blue_button=tkfont.Font(family='Café Françoise',size=8)
        self.word_font=tkfont.Font(family='Café Françoise',size=10)
        self.cal_font = tkfont.Font(family='Café Françoise',size=10)
        self.empty_font= tkfont.Font(size=40)
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        # built-in Frame, frame put inside the container
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        
        self.frames = {}  # empty dictionary
        # using a FOR loop to keep your pages together
        
        self.frames1 = {}
        
        for Menu_stack in (MainPage, StartPage, submenu,  MyDatePicker, StartPage1):
            page_name = Menu_stack.__name__
            frame = Menu_stack(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            # just set up grid, north-south-east-west expand to the max
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(0, weight=1)
        self.show_frame("MainPage")  # firstPage


        
        for frame1 in (StartPage, submenu, StartPage1, MainPage):
            page_name = frame1.__name__
            frame = frame1(parent=container,controller=self)
            self.frames1[page_name] = frame

            
        self.resizable(0,0)
    def show_frame(self, page):
        '''Show a frame for the given page name'''
        frame = self.frames[page]
        frame.tkraise()

    def show_frame1(self, page, Date1, Time1):
        '''show a frame updated with its date and time'''
        frame = self.frames1[page]
        
        frame.time = Time1
        frame.date = Date1
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        print(frame.date)
        frame.tkraise()

    

if __name__ == "__main__":
    app = Base()
    
    app.title("Canteen Master")
    app.iconbitmap("donut.ico")
    app.wm_attributes('-transparentcolor','green')
    app.mainloop()
    

import tkinter as tk                # import tkinter
from tkinter import font as tkfont  # import font

from PIL import ImageTk, Image
from tkinter import ttk
from time import strftime
from datetime import date


from tkinter import messagebox
from submenu import *


class StartPage(tk.Frame):
    date = today
    time = str_now1
    ''' This startPage  is use for today store'''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        
        # Set background image
        image = Image.open("menu_bg.jpg")
        
        photo = ImageTk.PhotoImage(image)
        label0 = tk.Label(self, image=photo)
        label0.image = photo  # keep a reference!
        label0.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame0 = tk.Frame(self, padx=10, pady=10, border=4, relief=tk.GROOVE, bg="black")
        frame0.grid(row=0, column=0)

        frame1 = tk.Frame(self, padx=10,pady=10, border=4, relief=tk.GROOVE, bg="black")
        frame1.grid(row = 2, column = 0,sticky = "ns")
        

        # set position for the time
        #self.label = tk.Label(self, text="")
        #self.label.grid(row=1, column=0,  sticky="n")
        #self.update_clock()

        # set position for the day

        self.label1 = tk.Label(frame0, text="",bg="burlywood1")
        self.label1.grid(row = 0, column = 0, sticky = "n")
        self.update_date()
        
        
        # button to go the menu page
        button1 = tk.Button(frame1, text="McDonald's", font=self.controller.button, command=lambda: self.show_frame1(
            submenu, self.date, self.time, stall1,"McDonald's"  ,"mac_bg.jpeg", "mac.jpg", "pink", Mac_Menu))  # button 1
        button2 = tk.Button(frame1, text="Koufu", font=self.controller.button, command=lambda: self.show_frame1(
            submenu, self.date, self.time, stall2,"Koufu","koufu_bg.jpeg", "koufu.png", "SteelBlue1", Koufu_Menu))  # button 2
        button3 = tk.Button(frame1, text="Subway", font=self.controller.button, command=lambda: self.show_frame1(
            submenu, self.date, self.time, stall3, "Subway", "subway_bg.jpeg", "Subway.png", "gold", Sub_Menu))  # button 3
        button4 = tk.Button(frame1, text="Pizza Hut", font=self.controller.button, command=lambda: self.show_frame1(
            submenu, self.date, self.time, stall4, "Pizza Hut", "pizza_bg.jpeg", "Pizza_Hut.png", "ivory2", Pizza_Menu))  # button 4
        button5 = tk.Button(frame1, text="KFC", font=self.controller.button, command=lambda: self.show_frame1(
            submenu, self.date, self.time, stall5,"KFC", "kfc_bg.jpeg", "KFC.PNG", "firebrick1", KFC_Menu))  # button 5
        button6 = tk.Button(frame1, text="Starbucks", font=self.controller.button, command=lambda: self.show_frame1(
            submenu, self.date, self.time, stall6,"Starbucks",  "starbucks_bg.jpeg", "Starbucks.png", "Seagreen2", Starbucks_Menu))  # button 6

        
        button1.config(height=0, width=10)
        button2.config(height=0, width=10)
        button3.config(height=0, width=10)
        button4.config(height=0, width=10)
        button5.config(height=0, width=10)
        button6.config(height=0, width=10)


        button1.grid(row=0, column=0, padx= 20, pady =15)
        button2.grid(row=0, column=1, padx= 20, pady =15)
        button3.grid(row=0, column=2, padx= 20, pady =15)
        button4.grid(row=1, column=0, padx= 20, pady =15)
        button5.grid(row=1, column=1, padx= 20, pady =15)
        button6.grid(row=1, column=2, padx= 20, pady =15)

        
        
        
        

        # button to back previous page
        
        back_button = tk.Button(self, text=""u"Back to previous page\u2b8c""",font=self.controller.button, command=lambda: controller.show_frame(
                "MainPage"))
        back_button.grid(row=3, pady = 10)
        
        

        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        frame0.grid_rowconfigure(0, weight = 1)
        frame0.grid_rowconfigure(1, weight=1)
        frame0.grid_columnconfigure(0, weight=1)
        

        frame1.grid_rowconfigure(0, weight = 1)
        frame1.grid_rowconfigure(1, weight=1)
        frame1.grid_rowconfigure(2, weight=1)
        frame1.grid_columnconfigure(0, weight=1)

    #def update_clock(self):
        #self.label.configure(text=self.time, font="arial", background="yellow")
        #self.after(50, self.update_clock)

    def update_date(self):
        self.label1.configure(text="Available stores on " + self.date +" ", font=self.controller.title_font1)
        self.after(10, self.update_date)

    def show_frame1(self, frame1, Date1, Time1, stall, name, bgimage, image, bg, menu):
        frame = frame1(parent=self.parent, controller=self.controller, date=Date1, time=Time1, stall = stall, name=name,
                       bgimage = bgimage, image = image, bg = bg, menu = menu)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.tkraise()

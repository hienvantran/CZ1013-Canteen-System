import tkinter as tk                # import tkinter
from PIL import ImageTk, Image
from tkinter import ttk
from time import strftime
import datetime 
import subprocess
import time
from tkinter import messagebox



class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.date = None
        self.time = None
        self.data = {}
        # Set background image
        image = Image.open("canteen_master.jpg")
        photo = ImageTk.PhotoImage(image)
        label0 = tk.Label(self, image=photo)
        label0.image = photo  # keep a reference!
        label0.place(x=0, y=0, relwidth=1, relheight=1)

        

        # Frame0 contains current tiem and date, select date and time, view menu
        frame0 = tk.Frame(self, border=4, relief=tk.RIDGE, bg="pink")
        frame0.grid(row=1, column=0, padx=5, pady=5)
        # Set position for current time and date
        self.label = tk.Label(frame0, text="", font=controller.time_font)
        self.label.grid(row=0, column=0, sticky="nsew")
        self.update_clock()

        # Button to set date and time
        btn = tk.Button(frame0, text = "View stores at another date", font=self.controller.button, 
                        command=lambda: controller.show_frame("MyDatePicker"))
        btn.grid(row = 1, column = 0, sticky = "nsew")
        

        # Button to link with menu for the set date and time

        btn1 = tk.Button(frame0, text="View stores now", font=self.controller.button,
                         command=lambda: controller.show_frame("StartPage"))
        btn1.grid(row=2, column=0, sticky="nsew")

        # Description about application
        frame2 = tk.Frame(self, border=4, relief=tk.RIDGE, bg="pink")
        frame2.grid(row=2, column=0, padx=5, pady=5, columnspan=4)

        label2 = tk.Label(frame2,
        text="Canteen Master is an application for users to \n reference the daily menu of the stalls in North \n Spine @ NTU. It also provides the ability to  \n estimate the waiting time and calculate the cost of food.",
        font = self.controller.button, background = "pink")
        label2.grid(row=0, column=4, columnspan=2, sticky = "nsew")

        image = Image.open("Nanyang.png")
        img = image.resize((90, 120), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        label1 = tk.Label(frame2, image=photo)
        label1.image = photo  # keep a reference!
        label1.grid(row=0, column=0, columnspan=1, sticky='nw')

        frame2.columnconfigure(0, weight=1)
        frame2.columnconfigure(3, weight=3)
        
    
        
    def update_clock(self):
        now = time.strftime("%A, %d %B %Y, %H:%M:%S" )
        self.label.configure(text=now, font=self.controller.button, background="deep sky blue")
        self.after(1000, self.update_clock)

    

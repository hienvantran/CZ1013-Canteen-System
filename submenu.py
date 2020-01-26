import tkinter as tk                # import tkinter
from tkinter import font as tkfont  # import font
from menu import *
from PIL import ImageTk, Image
from tkinter import ttk
import sys
from tkinter import messagebox
class submenu(tk.Frame):
    date = None
    time = None
    def __init__(self, parent, controller, stall = stall1, name = "Macdonald", bgimage = "mac_bg.jpeg", 
    image = "mac.jpg", bg = "pink", date = today, time = str_now1, menu = Mac_Menu):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.stall = stall
        self.name = name
        self.bgimage = bgimage
        self.image = image
        self.bg = bg
        self.date = date
        self.time = time
        self.menu = menu
        # Set background image
        image0 = Image.open(self.bgimage)
        image = image0.resize((1100,800))
        photo = ImageTk.PhotoImage(image)
        label0 = tk.Label(self, image=photo)
        label0.image = photo  # keep a reference!
        label0.place(x=0, y=0, relwidth=1, relheight=1)

        label1 = tk.Label(self, text="",
                           font=self.controller.empty_font,bg="green")
        label1.config(anchor=tk.CENTER)
        label1.grid(row=0, column=0, sticky="w")


        # format of self.date is : day_name, date-month-year
        # get the day name from self.date 
        day_name = self.date[0:self.date.index(",")]
        # format of self.time is: hour:min
        # get numeric value for time
        now1 = float(self.time[:2])  + float(self.time[3:5])/60

        
        
        """frame0 contains frame 1 and 2,
            frame 1 for the image and calculate waiting time,
            frame 2 for showing menu""" 

        # create frame0, 1, 2 and set position
        frame0 = tk.Frame(self, padx=10,pady=10, border=4, relief=tk.GROOVE, bg="black")
        frame0.grid(row=3, column=0, columnspan=5, rowspan=4, padx=100, pady=20, sticky="nsew") # row 3 of window

        self.frame1 = tk.Frame(frame0, border=4, relief=tk.RIDGE)
        self.frame1.grid(row=1, column=0, rowspan=4, columnspan =3, padx=5,sticky="nsew") # row 1, column 0 of frame0

        self.frame2 = tk.Frame(frame0, border=4, relief=tk.RAISED, bg=self.bg)
        self.frame2.grid(row=1, column=3, rowspan=4, columnspan=5, padx=5, sticky="nsew") # row 1, column 1 of frame0

        frame0.grid_columnconfigure(0, weight = 1)
        frame0.grid_columnconfigure(1, weight=1)
        frame0.grid_columnconfigure(2, weight = 1)
        frame0.grid_columnconfigure(3, weight=1)

        # set image for store
        image = Image.open(self.image)
        img = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)

        label3 = tk.Label(self.frame1, image=photo)
        label3.image = photo  # keep a reference!
        label3.grid(row=1, column=0, columnspan=3, sticky='nsew')


        # call self.stall from menu module
        # set date and time
        self.stall.get_dateTime(day_name, now1) #now1 must be numeric

        # get menu for specific time, date
        
        label0 = tk.Label(self.frame2, text="Menu for {} on {} at {}".format(self.name, day_name, self.time), bg=self.bg, font = self.controller.button)
        label0.config(anchor=tk.CENTER)
        label0.grid(row=0, column =0, pady=5, sticky="nw")

        label = tk.Label(self.frame2, text="Quantity", bg=self.bg,
                         font=self.controller.button)
        label.grid(row =0,column = 8, pady = 5, sticky = "n")

        self.entries = [] # create entries of number of food 
        row_index = 1 # set row for label menu
        list_cost = [] # list of string cost of food
        try: 
            TimeMenu = self.stall.get_timeMenu(self.menu)
            for men in TimeMenu.keys():
                menu = men # get menu
                list_cost.append(TimeMenu[men]) # get list
                cost = str(TimeMenu[men]) # get cost

                label1 = tk.Label(self.frame2, text=menu, bg=self.bg,font=self.controller.word_font)
                label1.config(anchor=tk.CENTER)
                label1.grid(row=row_index, column=0, pady=1, padx=5,columnspan=3, sticky="nw")

                label2 = tk.Label(self.frame2, text=cost, bg=self.bg,font=self.controller.word_font)
                label2.config(anchor=tk.CENTER)
                label2.grid(row=row_index, column=4, pady=1, padx=5, columnspan=3, sticky="nw")
                numMenu = tk.StringVar()
                # create entries list
                self.entries.append(tk.Entry(self.frame2, textvariable=numMenu, width = 10,))
                # grid layout the entries
                self.entries[row_index-1].grid(row=row_index, column=8, pady=3, padx=3, sticky = "w")
                # bind the entries return key pressed to an action
                row_index += 1 # increment row for next menu
        except:
            messagebox.showerror("Error", "Error message: Stall does not open")
        
        ''' calculate price '''

        self.price = 0  # set total price 0
        
        # set position showing total price
        
        totalPrice = tk.Button(self.frame2, text="Calculate Price", bg="#4750DF", font=self.controller.blue_button,
                               command=lambda: submenu.calPrice(self,  row_index, list_cost, self.price))
        totalPrice.grid(row=row_index + 2, column=0, sticky = "w")
       

        

        # get operating hours
        operaHour = tk.Label(self.frame1,font=self.controller.button, text="Operating Hours: {} - {}".format(self.stall.reprStarting, self.stall.reprClosing))
        operaHour.grid(row=0, column=0, columnspan=2, sticky="nw")

        


        '''calculate waiting time'''

        noPax = tk.Label(self.frame1, text="Enter no.of pax:",font=self.controller.button)
        noPax.grid(row=2, pady=3, sticky = "w")
        waitTime = tk.Label(self.frame1, text="Waiting time:",font=self.controller.button)
        waitTime.grid(row=3, pady=3, sticky = "n")
        
        
        # get input from entry
        numPax = tk.StringVar()
        e1 = tk.Entry(self.frame1, textvariable=numPax)
        e1.grid(row=2, column=1, pady=3, padx=3)
        # output time
        num = tk.StringVar()
        self.wait_label = tk.Label(self.frame1, textvariable=num,font=self.controller.button)
        self.wait_label.grid(row=3, column=1, pady=3, padx=3)
        
        # press button to calculate waiting time
        calTime = tk.Button(self.frame1, text="Calculate Time", bg="#4750DF", font=self.controller.blue_button,
                command=lambda: submenu.waitingTime(self, num, e1.get()))
        calTime.grid(row=2, column=2, padx=3, pady=3)
       

        

        # back to previous page
        
        if self.date == today and self.time == str_now1: 
            back_button = tk.Button(self, text=""u"Back to previous page\u2b8c""",font=self.controller.button,
                                    command=lambda: controller.show_frame("StartPage"))
            back_button.grid(row=7, pady=20)
        
        else:
            back_button = tk.Button(self, text=""u"Back to previous page\u2b8c""",font=self.controller.button,
                                    command=lambda: controller.show_frame1("StartPage1", self.date, self.time))
            back_button.grid(row=7, pady=20)
            
        
    def waitingTime(self, num,  numPax):
        # check the valid input in no.of pax
        try:
            num.set(str(int(numPax) * 5) + " minutes")
        except:
            messagebox.showerror("Error", "Error message: Invalid input! Must be number!")
            num.set("Enter again!")

    def calPrice(self,  row_index,list_cost, total_price):
        price_text = tk.StringVar()
        self.price_label = tk.Label(
                self.frame2, textvariable=price_text, bg=self.bg,font=self.controller.button)
        try:
            for m in range(row_index-1):
                text = self.entries[m].get()
                if text == "":
                    text = 0
                price = int(text) * float(list_cost[m][1:])
                total_price += price
            
            self.price_label.grid(row=row_index + 2, column=8)
            price_text.set("{0:.2f}".format(total_price))
        except:
            messagebox.showerror(
                "Error", "Error message: Invalid input! Must be number!")
            price_text.set("Enter again!")
      


    
        
            

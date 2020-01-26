import tkinter as tk                # import tkinter
  # import font

from PIL import ImageTk, Image
from tkinter import ttk
from time import strftime
from datetime import date

import time
from tkinter import messagebox
from startPage import *
from startPage1 import *
import calendar
import datetime
class MyDatePicker(tk.Frame):
    """
    Description:
        A tkinter GUI date picker.
    """

    def __init__(self, parent, controller, date = today, time = str_now):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.date = today
        self.full_date = None
        self.str_format = '%02d-%s-%s'
        
        # Set background image
        image = Image.open("Artboard 1.PNG")
        
        photo = ImageTk.PhotoImage(image)
        label0 = tk.Label(self, image=photo)
        label0.image = photo  # keep a reference!
        label0.place(x=0, y=0, relwidth=1, relheight=1)


        # set date and time page

        
        
        # create time scroll down

        HOURS = ["00", "01", "02", "03", "04", "05", "06",
                 "07", "08", "09", "10", "11", "12",
                 "13", "14", "15", "16", "17", "18",
                 "19", "20", "21", "22", "23"
                 ]  # et

        Mins = [
            "00","01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
            "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
            "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
            "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
            "51", "52", "53", "54", "55", "56", "57", "58", "59"
        ]

        self.Hour_variable = tk.StringVar()
        self.Hour_variable.set(HOURS[0])  # default value
        self.Minutes_variable = tk.StringVar()
        self.Minutes_variable.set(Mins[0])  # default value
        self.time = self.Hour_variable.get()+":"+self.Minutes_variable.get() # default value

        hour = ttk.Combobox(self, textvariable=self.Hour_variable, values=HOURS)
        hour.grid(row=3, column=1)

        Min = ttk.Combobox(self, textvariable=self.Minutes_variable, values=Mins)
        Min.grid(row=3, column=2)

        # make all rows and columns center 
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.num = tk.StringVar()
        self.wait_label = tk.Label(self, textvariable=self.num, font=controller.word_font)
        self.wait_label.grid(row=13, column=1)
        self.button = tk.Button(self, text="Confirm date and time",font=controller.word_font, command=self.accepttime)
        self.button.grid(row=14, column=1, sticky="") 
        
        # back and view button
        back_button = tk.Button(self, text=""u"Back to previous page\u2b8c""",font=self.controller.word_font,
                                command=lambda: controller.show_frame("MainPage"))
        back_button.grid(row=14, column=0, pady=20, padx=20, sticky="w")
        view_button = tk.Button(self, text="View Menu",font=self.controller.word_font,
                                command=lambda: self.get_date())
        view_button.grid(row=14, column=2, pady=20, padx=20, sticky="n")


        self.init_frames()
        self.init_needed_vars()
        self.init_month_year_labels()
        self.init_buttons()
        self.space_between_widgets()
        self.fill_days()
        self.make_calendar()

    def accepttime(self):
        y = self.Hour_variable.get()+":"+self.Minutes_variable.get() +" H"
        self.time = y
        label = tk.Label(self, text = self.time, font=self.controller.word_font)
        label.grid(row = 13, column = 2)
        self.changeDate( self.num, self.date)
    def set_date(self, clicked=None):
        """
        Description:
            Set the date from the calendar on button click.

        :param clicked: button clicked event.
        :type clicked: tkinter event
        """

        clicked_button = clicked.widget
        year = self.year_str_var.get()
        month = self.month_str_var.get()
        date = clicked_button['text']

        self.full_date = self.str_format % (date, month, year)
        full_date = datetime.datetime.strptime(self.full_date, '%d-%B-%Y').strftime(
            '%A, %d-%B-%Y') # return day, date-month-year for showing information
        
        self.date = full_date
        # update the date each time press date button
        

    def changeDate(self, num,fullDate):
        # update the date each time press date button
        # update the date each time press date button
        
        num.set(fullDate)
        
    def get_date(self):
        """
        Description:
            Get the date from the calendar on button click.

        """
        Time1 = self.time
        Date1 = self.date
        
        self.accepttime
        self.show_frame1(StartPage1, Date1, Time1)

    def show_frame1(self, frame1, Date1, Time1):
        frame = frame1(parent=self.parent,
                       controller=self.controller)
        frame.date = Date1
        frame.time = Time1
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.tkraise()

        
    def init_frames(self):
        
        self.frame1 = tk.Frame(self)
        self.frame1.grid(row=3)

        self.frame_days = tk.Frame(self)
        self.frame_days.grid(row = 4, rowspan = 6)

        self.frame2 = tk.Frame(self)
        self.frame2.grid(row =11)

    def init_needed_vars(self):
        self.month_names = tuple(calendar.month_name)
        self.day_names = tuple(calendar.day_abbr)
        self.year = time.strftime("%Y")
        self.month = time.strftime("%B")
        
        
    def init_month_year_labels(self):
        self.year_str_var = tk.StringVar()
        self.month_str_var = tk.StringVar()

        self.year_str_var.set(self.year)
        self.year_lbl = tk.Label(self.frame1, textvariable=self.year_str_var,font=self.controller.cal_font,
                                 width=3)
        self.year_lbl.grid(row=2, column=5)

        self.month_str_var.set(self.month)
        self.month_lbl = tk.Label(self.frame1, textvariable=self.month_str_var,font=self.controller.cal_font,
                                  width=8)
        self.month_lbl.grid(row=2, column=1)

    def init_buttons(self):
        self.left_yr = ttk.Button(self.frame1, text="←", width=5,command=self.prev_year)
        self.left_yr.grid(row=2, column=4)

        self.right_yr = ttk.Button(self.frame1, text="→", width=5,command=self.next_year)
        self.right_yr.grid(row=2, column=6)

        self.left_mon = ttk.Button(self.frame1, text="←", width=5,command=self.prev_month)
        self.left_mon.grid(row=2, column=0)

        self.right_mon = ttk.Button(self.frame1, text="→", width=5,command=self.next_month)
        self.right_mon.grid(row=2, column=2)

        
    def space_between_widgets(self):
        self.frame1.grid_columnconfigure(3, minsize=40)

    def prev_year(self):
        self.prev_yr = int(self.year_str_var.get()) - 1
        self.year_str_var.set(self.prev_yr)

        self.make_calendar()

    def next_year(self):
        self.next_yr = int(self.year_str_var.get()) + 1
        self.year_str_var.set(self.next_yr)

        self.make_calendar()

    def prev_month(self):
        index_current_month = self.month_names.index(self.month_str_var.get())
        index_prev_month = index_current_month - 1

        #  index 0 is empty string, use index 12 instead,
        # which is index of December.
        if index_prev_month == 0:
            self.month_str_var.set(self.month_names[12])
        else:
            self.month_str_var.set(self.month_names[index_current_month - 1])

        self.make_calendar()

    def next_month(self):
        index_current_month = self.month_names.index(self.month_str_var.get())

        try:
            self.month_str_var.set(self.month_names[index_current_month + 1])
        except IndexError:
            #  index 13 does not exist, use index 1 instead, which is January.
            self.month_str_var.set(self.month_names[1])

        self.make_calendar()

    def fill_days(self):
        col = 0
        #  Creates days label
        for day in self.day_names:
            self.lbl_day = tk.Label(self.frame_days, text=day,font=self.controller.cal_font)
            self.lbl_day.grid(row=0, column=col)
            col += 1

    def make_calendar(self):
        #  Delete date buttons if already present.
        #  Each button must have its own instance attribute for this to work.
        try:
            for dates in self.m_cal:
                for date in dates:
                    if date == 0:
                        continue

                    self.delete_buttons(date)

        except AttributeError:
            pass

        year = int(self.year_str_var.get())
        month = self.month_names.index(self.month_str_var.get())
        self.m_cal = calendar.monthcalendar(year, month)

        #  build dates buttons.
        for dates in self.m_cal:
            row = self.m_cal.index(dates) + 1
            for date in dates:
                col = dates.index(date)

                if date == 0:
                    continue

                self.make_button(str(date), str(row), str(col))

    def make_button(self, date, row, column):
        """
        Description:
            Build a date button.

        :param date: date.
        :type date: string

        :param row: row number.
        :type row: string

        :param column: column number.
        :type column: string
        """
        exec(
            "self.btn_" + date + " = ttk.Button(self.frame_days, text=" + date
            + ", width=5)\n"
            "self.btn_" + date + ".grid(row=" + row + " , column=" + column
            + ")\n"
            "self.btn_" + date + ".bind(\"<Button-1>\", self.set_date)"

        )

    def delete_buttons(self, date):
        """
        Description:
            Delete a date button.

        :param date: date.
        :type: string
        """
        exec(
            "self.btn_" + str(date) + ".destroy()"
        )
        


    

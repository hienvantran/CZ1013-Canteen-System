from time import strftime
import datetime 
import subprocess
import time


today = datetime.date.today().strftime("%A, %d-%B-%Y")
now = float(time.strftime("%H")) + float(strftime("%M"))/60



str_now =  time.strftime("%H:%M:%S")
str_now1 = time.strftime("%H:%M")



noon = 12
class foodStall:
    
    def __init__(self, name): 
        self.name = name
    
    def set_operating_hours(self, startingTime, closingTime):
        ''' Set operating hours'''
        "get numeric value"
        startingTime1 = float(startingTime[:2]) + float(startingTime[3:])/60
        closingTime1 = float(closingTime[:2]) + float(closingTime[3:])/60
        self.starting = startingTime1
        self.closing = closingTime1

        "get representation, string"
        self.reprStarting = startingTime
        self.reprClosing = closingTime

    def get_operating_hours(self):
        ''' Get operating hours '''
        return "Operating hours: \n Starting: {} \n Closing: {}".format(self.reprStarting, self.reprClosing)

    def get_dateTime(self, date, time):
        '''Get current date and time'''
        self.date = date
        self.time = time
    def get_DateMenu(self, DateMenu): 
        #DateMenu is a dictionary, key is group date and value is menu for these dates
        ''' Get menu (both morning and afternoon) in this date'''
        
        date_group = list(DateMenu.keys()) 
        # return a list of group date (Monday, Tuesday, Friday); (Wednesday, Thursday, Saturday)
        
        for i in range(len(date_group)):
            if self.date in date_group[i]:
                # return a dictionary with key is time and value is food & cost
                return DateMenu[date_group[i]] 

    def get_timeMenu(self, DataMenu):
        ''' Get menu for specific time '''
        DateMenu = self.get_DateMenu(DataMenu)
       
        
        if self.starting <= self.time <= noon: # morning: startingTime.00 - noon.00
            # return a dictionary with key is food, value is cost
            timeDateMenu = DateMenu["morning"]

        elif noon<= self.time <= self.closing: # afternoon: noon.00 - closingTime.00
            timeDateMenu = DateMenu["afternoon"]
            
        else:
            return {}
        
        return timeDateMenu
        
        
            
    

Mac_Menu = {('Monday', 'Wednesday', 'Friday', 'Sunday') :  #For all odd days 

            {"morning": {"Hotcakes with Sausage": "$7.40", "Egg McMuffin": "$5.90", "Sausage McMuffin" : "$5.40",
            "Coca-Cola":"$2.95","Sprite":"$2.95","Iced Lemon Tea":"$2.95",
            "Mudpie McFlurry":"$2.20","Strawberry Shortcake McFlurry":"$2.20","Hot Fudge Sundae":"$2.20",
            "Potato(6pc)" : "$2.30", "Apple Slices" : "$2.30", "Hashbrown":"$2.20"
            }, 

             "afternoon": {"Double McSpicy": "$6.30", "Double Filet-O-Fish": "$6.90", "Double Cheeseburger": "$7.60",
            "Coca-Cola":"$2.95","Sprite":"$2.95","Iced Lemon Tea":"$2.95",
            "Mudpie McFlurry":"$2.20","Strawberry Shortcake McFlurry":"$2.20","Hot Fudge Sundae":"$2.20",
            "Potato(6pc)" : "$2.30", "Apple Slices" : "$2.30", "Hashbrown":"$2.20"}},

            ('Tuesday', 'Thursday', 'Saturday') :  #For all even days #Morning
            {"morning" : {"Scrambled Egg Burger": "$6.30", "Breakfast Wrap Sausage": "$6.90", "Big Breakfast": "$7.60",
            "Coca-Cola":"$2.95","Sprite":"$2.95","Iced Lemon Tea":"$2.95",
            "Mudpie McFlurry":"$2.20","Strawberry Shortcake McFlurry":"$2.20","Hot Fudge Sundae":"$2.20",
            "Potato(6pc)" : "$2.30", "Apple Slices" : "$2.30", "Hashbrown":"$2.20"
            },
              #For all even days #Afternoon
             "afternoon": {"Buttermilk Crispy Chicken": "$9.65", "Chicken McNuggets": "$6.85", "Classic Angus Cheese": "$11.60",
            "Coca-Cola":"$2.95","Sprite":"$2.95","Iced Lemon Tea":"$2.95",
            "Mudpie McFlurry":"$2.20","Strawberry Shortcake McFlurry":"$2.20","Hot Fudge Sundae":"$2.20",
            "Potato(6pc)" : "$2.30", "Apple Slices" : "$2.30", "Hashbrown":"$2.20"}}}


Koufu_Menu = {('Monday', 'Wednesday', 'Friday', 'Sunday') : 
            {"morning": {"Lontong": "$2.50", "Mee Rebus": "$2.50", "Mee Siam": "$2.50",
            "Roasted Chicken Noodle": "$2.80", "3 Veg + Rice": "$2.00",
            "Teh": "$1.00", "Kopi": "$1.00","Milo":"$1.00",
            "Iced Teh": "$1.50", "Iced coffee": "1.50","Iced Milo":"$1.50"
            },
               
            "afternoon": {"Mee Soto": "$2.50", "Roasted Pork Rice": "$2.50", "Char Siew Rice": "$2.50",
            "Yi Mian / Koka Mian": "$2.80", "U Mian": "$2.80",
            "Teh": "$1.00", "Kopi": "$1.00","Milo":"$1.00",
            "Iced Teh": "$1.50", "Iced coffee": "$1.50","Iced Milo":"$1.50"

            }},

            ('Tuesday', 'Thursday', 'Saturday') :  
            {"morning": {"Roasted Duck Noodle": "$3.00", "Roasted Duck Rice": "$3.00", "Steamed Chicken Rice": "$2.80",
            "Ban Mian/ Mee Hoon Kway": "$2.80", "Bee Hoon": "$2.80",
            "Teh": "$1.00", "Kopi": "$1.00","Milo":"$1.00",
            "Iced Teh": "$1.50", "Iced coffee": "$1.50","Iced Milo":"$1.50"
            },         

            "afternoon": {"Roasted Chicken Rice": "$2.80", "1 Meat + 1 Veg + Rice -": "$2.30", "Curry Chicken Noodle": "$2.80",
            "Mushroom Minced Meat": "$3.00", "Lotus Root Pork Ribs Soup ": "2.80",
            "Teh": "$1.00", "Kopi": "$1.00","Milo":"$1.00",
            "Iced Teh": "$1.50", "Iced coffee": "$1.50","Iced Milo":"$1.50"
            }}}

Sub_Menu = {('Monday', 'Wednesday', 'Friday', 'Sunday','Tuesday', 'Thursday', 'Saturday') : 
            {"morning": {"Chicken Sausage, Egg & Cheese": "$4.00", "Egg & Cheese": "$4.00", 
            "Chicken Bacon, Egg & Cheese": "$4.00","Chicken Ham, Egg & Cheese": "$4.00",
            "coffee": "1.60","Fountain Soft Drink":"$1.60","Minute Maid Juice":"$1.80"
            },
               
            "afternoon": {"Veggie Delite": "$3.75", "Turkey Italiano Melt": "$4.25", "Tuna": "$4.25",
            "Subway Club": "$4.75", "Roast Beef": "$4.75",
            "Italian B.M.T.": "$4.25", "Chicken & Bacon Ranch Melt": "4.75","Black Forest Ham":"$3.75",
            "coffee": "1.60","Fountain Soft Drink":"$1.60","Minute Maid Juice":"$1.80"
            }}}


KFC_Menu = {('Monday', 'Wednesday', 'Friday', 'Sunday','Tuesday', 'Thursday', 'Saturday') : 
            {"morning": {"Mighty Zinger meal": "$8.95", "Mighty Zinger Box": "$10.55", "Family Feast": "$37.95",
            "5pcs Buddy Meal": "$19.95", "wing Snacks": "$4.20", "Tenders snacks": "4.20","Popcorn Snackers":"$4.20","Nugget Snackers":"$4.20",
            "Coca-Cola": "$2.00", "Iced Lemon Tea": "$2.00","Sprite":"$2.00"
            },
               
            "afternoon": {"Mighty Zinger meal": "$8.95", "Mighty Zinger Box": "$10.55", "Family Feast": "$37.95",
            "5pcs Buddy Meal": "$19.95", "wing Snacks": "$4.20", "Tenders snacks": "4.20","Popcorn Snackers":"$4.20","Nugget Snackers":"$4.20",
            "Coca-Cola": "$2.00", "Iced Lemon Tea": "$2.00","Sprite":"$2.00"
            }}}

Pizza_Menu = {('Monday', 'Wednesday', 'Friday', 'Sunday','Tuesday', 'Thursday', 'Saturday') : 
            {"morning": {"Hawaiian pizza": "$17.90", "Pepperoni pizza": "$17.90", "Veggie Lover pizaa": "$17.90",
            "Curry chickenn pizza": "$17.90", "Seafood Vongole": "$12.50", "Prawn Aglio Olio": "10.90","Creamy Mushroom":"$9.50",
            "Coca-Cola": "$2.00", "Iced Lemon Tea": "$2.00","Sprite":"$2.00"
            },
               
            "afternoon": {"Hawaiian pizza": "$17.90", "Pepperoni pizza": "$17.90", "Veggie Lover pizaa": "$17.90",
            "Curry chickenn pizza": "$17.90", "Seafood Vongole": "$12.50", "Prawn Aglio Olio": "10.90","Creamy Mushroom":"$9.50",
            "Coca-Cola": "$2.00", "Iced Lemon Tea": "$2.00","Sprite":"$2.00"
            }}}

Starbucks_Menu = {('Monday', 'Wednesday', 'Friday', 'Sunday','Tuesday', 'Thursday', 'Saturday') : 
                 {"morning": {"Caffe Latte": "$4.00", "Caffe Mocha": "$4.75", "White Chocolate Mocha": "$4.50",
                "Skinny Vanilla Latte": "$4.85", "Caramel Macchiato": "$3.40",
                "Skinny Peppermint Mocha": "$3.95", "Mocha Frappuccino": "$3.75"

                },
                   
                "afternoon": {"Caffe Latte": "$4.00", "Caffe Mocha": "$4.75", "White Chocolate Mocha": "$4.50",
                "Skinny Vanilla Latte": "$4.85", "Caramel Macchiato": "$3.40",
                "Skinny Peppermint Mocha": "$3.95", "Mocha Frappuccino": "$3.75"

                }}}

stall1 = foodStall("Mac")
stall1.set_operating_hours("07:00", "23:30")

stall2 = foodStall("Koufu")
stall2.set_operating_hours("07:00", "20:00")

stall3 = foodStall("Sub")
stall3.set_operating_hours("08:00", "21:00")

stall4 = foodStall("Pizza")
stall4.set_operating_hours("11:00", "22:00")

stall5 = foodStall("KFC")
stall5.set_operating_hours("11:00", "20:00")

stall6 = foodStall("Starbucks")
stall6.set_operating_hours("07:00", "22:00")





# Canteen-System
Design a canteen system for browsing the opening stalls in NTU north spine canteen and their current available menu at any date and time
## 1        INTRODUCTION

## 1.1     Objective  

The objective of this project is to create a python program that can show the real time menu of the stalls in north spine. The program is required to meet the following requirements:

> Store and display stall information
> Store and display stall menus
> Display stall information and menus based on current system date and time
> Display stall information and menus based on user defined date and time
> Calculate estimated waiting time for the stall by asking user to enter the number of people in the queue
> Allow to check the operating hours for all stalls

## 2        ALGORITHM DESIGN

## 2.1     Flowchart

Legend:
◇ = Start program
○ = Program Action
□ = User Action

### Scenario 1: Stall information now (McDonald’s)

Start Main.py --> Open mainpage.py --> Users select "View today store" --> Open startpage.py --> Users select "Macdonal's" --> Open submenu.py --> Call stall1 from menu.py using current device day and time input --> Display dictionary values 

### Scenario 2: Stall information on another date (McDonald’s)

Start Main.py --> Open mainpage.py --> Users select "View other day store" --> Open MyDatePicker.py --> Users slect date and time input, confirm and press "view menu" --> Open startpage1.py --> Users select "Macdonal's" --> Open submenu.py --> Call stall1 from menu.py using current device day and time input --> Display dictionary values 

## 2.2     Selection of GUI Package

Tkinter

For this project, we have decided to use tkinter as the Graphical User Interface (GUI) package because of its simplicity. It is also well documented and tutorials for it are easy to find. As tkinter also comes bundled with the installation of python, distribution of the final product will be much easier.

## 2.3     Program Flow

### Program Structure

For this project, we have gone with the extensive usage of different functions and modules, we are able to complete the project in a much shorter time without having to wait on each other to produce a working prototype. Moreover, the use of functions allowed us to edit a specific part of the code without it affecting the entire program.

Furthermore, we have used classes throughout our project. It is a qualified namespace that helps to create objects and frames in the program that has fixed attributes. This makes it easier to reuse the attributes, increases organisability and allows for us to edit the code more easily if we want to make any changes.


### Stall Information

Our program, the “Canteen Master” aims to show the menu of the many different stalls based on the time and day. Each of these stalls has a different menu depending on the time and day. In order to satisfy the requirements set before us, we have decided to split the menus by time and day. For the time we have split the menus into 2 categories, before 12 for breakfast and 12 onwards for both lunch and dinner. With regards to the day, we have split the days of the weeks into 2 categories, odd-numbered days, which includes Monday, Wednesday, Friday and Sunday, and even-numbered days which include Tuesday, Thursday and Saturday. The program also allows the user to check the opening hours of each of the stalls at any specified time and day.

The program also allows users to check the menu based on either the device’s time and day or the time and day inputted by the user. The program pulls the relevant data based on time and day input.

The input of other times and days is done via the selection of dates through a calendar and the selection of time is done via a drop-down menu.



Along with the menu, the opening hours of the stall are also displayed on the same page.



### Menu

The menu for each of the stalls is stored using a dictionary in the menu.py file. The menu uses a nested dictionary to call out the menu and the price of the items where the first key would be the day and the second key would be the time, either morning or afternoon.

### Waiting Time

Another feature of the program is the ability for the program to calculate the waiting time based on the number of people in the queue. The number of people requires an input of an integer by the user and the waiting time for each person is set to 5 minutes. The program will then show the number of minutes a user has to wait for their turn to purchase food.


## 2.4     Additional Features

### Costs Calculation

A feature that we have added to the Canteen Master is the costs calculation of various foods. This feature will allow the user to calculate the costs of the food that they would like to buy inputting the total quantity of the items they are purchasing. The program will then add the total cost of the items and display it at the bottom when the user presses “Calculate Price”.






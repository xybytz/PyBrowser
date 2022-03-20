# Import the required libraries
from tkinter import *
import webview

#Set Repeat Execution Variables
a = 1

# Create an instance of tkinter frame or window
win = Tk()


# Set the size of the window
win.geometry("700x350")

# Create a GUI window to view the HTML content
#Ask user for website
while a == 1:
    print("What website would you like to go to?")
    weburl = input()
    webview.create_window(weburl, weburl)
    webview.start()
    

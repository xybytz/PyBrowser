# Import the required libraries
from tkinter import *
import webview
from os.path import exists



#Set Repeat Execution Variables
a = 1

# Create an instance of tkinter frame or window
win = Tk()

bookmarks = 'bookmarks'
# Set the size of the window
win.geometry("700x350")

# Create a GUI window to view the HTML content
#Ask user for website
weburl = "https://www.google.com"


webview.create_window(weburl, weburl)
webview.start()

    

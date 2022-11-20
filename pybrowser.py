# Import the required libraries
from tkinter import *
import webview
from os.path import exists
###########
import tkinter as tk
from tkinter import simpledialog
ROOT = tk.Tk()
USER_INP =''
# the input dialog

USER_INP = simpledialog.askstring(title="URLBAR",
                                prompt="Enter Website URL:")

# check it out

##########



# Create an instance of tkinter frame or window

bookmarks = 'bookmarks'
# Set the size of the window

# Create a GUI window to view the HTML content
#Ask user for website

webview.create_window(USER_INP, USER_INP)
webview.start()



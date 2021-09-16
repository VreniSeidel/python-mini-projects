# This is simple program to show how print statement works
from tkinter import *


X = 400 # X coordinate
Y = 400 # Y coordinate

root=Tk()                   # Window it self
root.geometry(f"{X}x{Y}")   # Window size
root.title("Python")        # Title

Label(root, text="Hello python world!").place(x=X-270, y=Y-230) # Text from window

root.mainloop() # End of the main loop
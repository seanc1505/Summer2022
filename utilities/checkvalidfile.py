# Check if the file is valid, open dialog box if not
# returns file path

import os
from tkinter import *
from tkinter import filedialog


def checkValidFile(file="", check_name=""):
    if check_name != "":
        print("Checking for " + check_name + " at: "+file)
    if os.path.exists(file):
        pass
    else:
        print("Could not find file; " + file + ", \r Please select it")
        root = Tk()
        file = filedialog.askopenfilename()
        root.destroy()
    print("File selected: " + file)
    return file

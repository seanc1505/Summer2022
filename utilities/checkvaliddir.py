# Check if the directory is valid, open dialog box if not
# returns directory path

import os
from tkinter import *
from tkinter import filedialog


def checkValidDirectory(dir="", check_name="", make_if_fail=True):
    if check_name != "":
        print("Checking for " + check_name + " at: "+dir)
    if os.path.exists(dir):
        pass
    elif dir == "" or make_if_fail == False:
        print("Could not find directory; " + dir + ", \r Please select it")
        root = Tk()
        dir = filedialog.askdirectory()
        root.destroy()
    else:
        print("Could not find directory; " + dir + ", creating")
        os.mkdir(dir)
    print("Directory selected: " + dir)
    return dir

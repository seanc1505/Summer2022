# Check if the directory is valid, open dialog box if not
# returns directory path

import os
from tkinter import *
from tkinter import filedialog


def checkValidDirectory(dir="", make_if_fail=True):
    if os.path.exists(dir):
        pass
    elif dir == "" or make_if_fail == False:
        root = Tk()
        dir = filedialog.askdirectory()
        # Add error handling for if they don't pick a file
        root.destroy()
    else:
        os.mkdir(dir)
        # Add error handling for if the path can't be resolved
    return dir

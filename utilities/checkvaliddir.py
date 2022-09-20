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
        dir = checkValidDirectory(dir,make_if_fail)
        root.destroy()
    else:
        try:
            os.mkdir(dir)
        except OSError as e:
            print("Error found with dir" + str(e))
            dir = checkValidDirectory(dir="",make_if_fail=make_if_fail)
    return dir

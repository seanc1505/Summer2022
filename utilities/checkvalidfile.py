# Check if the file is valid, open dialog box if not
# returns file path

import os
from tkinter import *
from tkinter import filedialog


def checkValidFile(file=""):
    if os.path.exists(file):
        pass
    else:
        root = Tk()
        file = filedialog.askopenfilename()
        root.destroy()
    return file

import os
from tkinter import *
from tkinter import filedialog


def checkValidFile(file=""):
    """Checks if directory is valid, else open file dialog.
        Returns path to file
    """
    if os.path.exists(file):
        pass
    else:
        root = Tk()
        file = filedialog.askopenfilename()
        file = checkValidFile(file=file)
        root.destroy()
    return file

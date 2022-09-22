import os
from tkinter import *
from tkinter import filedialog


def checkValidDirectory(directory="", make_if_fail=True):
    """Checks if directory is valid, else open file dialog (make if fail = false), otherwise make directory.
    Returns directory path."""
    if os.path.exists(directory):
        pass
    elif directory == "" or make_if_fail == False:
        root = Tk()
        directory = filedialog.askdirectory()
        directory = checkValidDirectory(directory,make_if_fail)
        root.destroy()
    else:
        try:
            os.mkdirectory(directory)
        except OSError as e:
            print("Error found with directory" + str(e))
            directory = checkValidDirectory(directory="",make_if_fail=make_if_fail)
    return directory

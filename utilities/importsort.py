import os
import shutil

from utilities.checkvaliddir import checkValidDirectory
from utilities.createsavefolder import createSaveFolderPath
from utilities.goprorename import goproRename


def importSort(source_path="", save_location=""):
    date_string_format = '%Y_%m_%d'  # folder name format

    source_path = checkValidDirectory(source_path, "Source Path", False)
    file_list = os.listdir(source_path)

    for file_name in file_list:
        if file_name[-4:] == ".MP4" or file_name[-4:] == ".mp4":
            source_file = source_path + file_name
            save_path = createSaveFolderPath(source_file, save_location)
            file_name = goproRename(file_name)
            new_file_location = save_path + "/" + file_name
            print("Moving: "+file_name)
            # Move file to new location
            shutil.move(source_file, new_file_location)
        elif file_name[-4:] == ".lrv" or file_name[-4:] == ".thm":
            # delete all non mp4 files
            os.remove(source_path+file_name)
        else:
            pass

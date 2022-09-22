from utilities.checkvaliddir import checkValidDirectory
from utilities.createsavefolder import createSaveFolderPath
from utilities.goprorename import goproRename
from utilities.findfilename import findFileName
import os
import shutil


class SourceVideoDir():
    def __init__(self,source_path,save_location) -> None:
        self.importSortVideo(source_path,save_location)

    def importSortVideo(self, source_path="", save_location=""):
        """
        Imports all mp4 files from source to save location,
        Deletes all lrv and thm file types
        """
        source_path = checkValidDirectory(source_path, False)
        file_list = os.listdir(source_path)
        
        for file_name in file_list:
            if file_name[-4:] == ".MP4" or file_name[-4:] == ".mp4":
                source_file = source_path +"/"+ file_name
                save_path = createSaveFolderPath(source_file, save_location)
                file_name = goproRename(file_name)
                new_file_location = save_path + "/" + file_name
                # Move file to new location
                shutil.move(source_file, new_file_location)
            elif file_name[-4:] == ".lrv" or file_name[-4:] == ".thm":
                # delete all non mp4 files
                os.remove(source_path+file_name)
            else:
                pass

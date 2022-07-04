from utilities.checkvaliddir import checkValidDirectory
from utilities.createsavefolder import createSaveFolderPath
from utilities.goprorename import goproRename
from utilities.findfilename import findFileName
import os
import shutil


class SourceVideoDir():
    def __init__(self, defaults) -> None:
        self.importSortVideo(defaults)

    def importSortVideo(self, defaults):
        source_path = checkValidDirectory(defaults.user_settings["import_to_path"], False)
        file_list = os.listdir(source_path)
        for file_name in file_list:
            if file_name[-4:] == ".MP4" or file_name[-4:] == ".mp4":
                source_file = source_path +"/"+ file_name
                save_path = createSaveFolderPath(source_file, defaults.user_settings["import_from_path"])
                file_name = goproRename(file_name)
                new_file_location = save_path + "/" + file_name
                # Move file to new location
                shutil.move(source_file, new_file_location)
            elif file_name[-4:] == ".lrv" or file_name[-4:] == ".thm":
                # delete all non mp4 files
                os.remove(source_path+file_name)
            else:
                pass

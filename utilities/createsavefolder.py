from utilities.checkvaliddir import checkValidDirectory
import os
import datetime
#Creates a folder based on the date a file was created
def createSaveFolderPath(source_file,save_location):
    save_location = checkValidDirectory(save_location,True)
    recorded_time = os.path.getmtime(source_file)
    date_string_format = '%Y_%m_%d' #folder name format
    # get it in the right format
    date_recorded = datetime.datetime.utcfromtimestamp(recorded_time).strftime(date_string_format)
    file_save_location = save_location +"/"+ date_recorded
    file_save_location = checkValidDirectory(file_save_location,True)
    return file_save_location
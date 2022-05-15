# Current Functionality

Csv File Source is the main object class file now

## Csv file source

### importVideoCsv

File dialog to open the csv File.
Asks for the export video name.
File dialog to open the video path.
Reads in data and processes via processCsvData.

### exportVideoFromCsv

Exports videos per person from the csv file.
Video name is the base name + paddler

### ProcessCsvData

Removes all blank space and uses the row above to populate the entire csv.
Inserts the time into seconds from a string

## Supplementing function files

### Check valid Directory

    checkValidDirectory(dir="", check_name="", make_if_fail=True)

Checks if directory is valid, else open file dialog (make if fail = false), otherwise make directory.

### Create Save Folder

    createSaveFolderPath(source_file,save_location)

Creates a save folder based on date of creation of the source file.
Returns the save location path.

### GoproRename

Renames go pro file from GH119999.mp4 to GH9999_11.mp4

### ImportSort

    importSort(source_path="", save_location="")

Checks valid directory of source path.
Creates the path to new folder if needed. Renames the file and moves the file to the new folder, deletes the additional gopro file types.
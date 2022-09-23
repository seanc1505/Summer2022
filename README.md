# Video Editor

* Design of a fully automated editing process navigated by an interactive online GUI.
* Interacts with machine learning progams hosted on the cloud.
* Computation should probably be done on the cloud too but may require upload which would be slow.

# Main

### Repo Layout

Current Active branches:

* main
  * Hosts most up to date running code
* csv
* video
* defaults

### Code Laout

* Main.py will be main file that pulls everything together

#### Objects

* GUI
  * Algorithim
  * CSV editing
* Defaults
* Algorithim
* CSV file
* Source Video
* Export Video

# Data | Branch function

Renamed to Data
  Main information stored in Data.data

### Layout of code

All files contained within csv_files/

### Objects

* Data
  1. init
  2. importCsv
  3. createCsvManual
  4. createCsvAlgorithim
  5. processVideoDF

#### Init(default_settings)

* Imports default settings from json file

#### ImportCsv(path)
    def importFromCsv(self, path=""):

* Imports edit data from csv that is at path location or allows picking the file

#### createDataCsvManual

* Creates and opens and imports a csv file at the specified path named csv_name

#### createDataAlgorithim

* **DEV**Creates a csv based on the AI generated in/out points

#### processVideoDF

* Adjusts all empty cells
* If column is empty it uses the value in row above
* Converts start and end times floating point in seconds
* Sorts the files based on paddler then video name
* Adds subclip numbers to all rows for each paddler

# Default Templates

All files contained within defaults/

* User_settings
  * Contains the latest user settings
* Default settings
  * Contains the default settings for various default values

### Objects

* Defaults
  1. init
  2. importDefaults
  3. resetDefaults
  4. editDefaults
  5. saveDefaults

#### init

* imports default settings
  
#### importDefaults(user="user")

* Imports defaults from user_settings.json or default_settings.son
* Stores within default settings

#### resetDefaults

* Sets user settings to default settings

#### editDefaults(edits)

* Adjusts user_settings to the information included in edits dicitonary

#### saveDefaults

* Saves changed settings to user_settings.json
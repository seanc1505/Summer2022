# Video Editor

* Design of a fully automated editing process navigated by an interactive online GUI.
* Interacts with machine learning progams hosted on the cloud.
* Computation should probably be done on the cloud too but may require upload which would be slow.

## Repo Layout

Current Active branches:

* main
  * Hosts most up to date running code
* csv
* video
* defaults

## Code Laout

* Main.py will be main file that pulls everything together

# Video Editor

## Objects
SourceVideo
ExportVideo

### Source Video

- [ ] Init -> pass a path and update source path vars
- [ ] Import Videos -> Move files to specified directory in format (YY_MM_DD)
- [x] Rename files -> Renames go pro files from GHYYXXXX to GHXXXX_YY

### Export Video

- [x] Create dictionary from csv file
- [x] export clips
- [x] ALL files should move to save to and from user_settings
- [x] naming of files and sorting of source and export directories
- [x] Store those key data that gets passed in within user settings
- [ ] Update readme with new format of video/
- [ ] move all setting of vars to the UI section
- [ ] draft a command line ui
- [ ] check that all default settings actually still get checked
  - [ ] valid files etc
- [x] Rearrange the export to call subclip_dict and pass in csv there
- [ ] updating of documentation

## Added functionality



# Functionality concepts

Detailing the desired structure and functionality of the project as a whole.
Should be an a fully automated editing process navigated by an interactive online GUI.
Interacts with machine learning progams hosted on the cloud. Computation should probably be done on the cloud too but may require upload which would be slow.

## Layout of code

### Objects

* GUI
  * Algorithim
  * CSV editing
* Defaults
* Algorithim
* CSV file
* Source Video
* Export Video

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

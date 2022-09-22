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
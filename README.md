# Default Templates


## Layout of code

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

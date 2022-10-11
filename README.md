# Table of Contents

- [Table of Contents](#table-of-contents)
  - [This branch](#this-branch)
    - [GUI functionality](#gui-functionality)
  - [WebUI](#webui)
    - [Code Layout](#code-layout)
      - [Project](#project)
        - [WebUI subdir](#webui-subdir)
          - [Main dir](#main-dir)
          - [templates](#templates)

## This branch



### GUI functionality
* Import and sort videos from a folder
  * Needs a defaults JSON which points to external dirs first
    * Shows a list of external dirs and folders within that might be right. (select one checkbox and it performs an import and sort)
  * Contains the default location and the default folder name.
  * Defaults should be editiable in the gui
* Edit videos based on a csv file
  * CSV file generated by:
    * Manually created and imported
      * could give the option to open one with the right headings already in
    * Auto generated by algorithim
      * Need to be able to review it
  * CSV file needs to be auto editied
    * If only the file number, auto complete (eg 012145 --> GH012145 when imported)
    * If a cell is blank use the value in the cell directly above when manually created
* Export videos to a specific location


## WebUI

All work in user_interface/ folder

### Code Layout

#### Project

1. Web UI dir
2. run.py

##### WebUI subdir

1. Main dir
2. static
3. templates
4. init.py

###### Main dir

 1. Forms.py
    1. Addnewtime point form
 2. Routes.py
    1. home
    2. about
    3. new time point
 3. utils.py

###### templates

1. layout.html
2. about.html
3. time_point_new.html
4. home.html

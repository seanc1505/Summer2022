import json
from tkinter.filedialog import SaveFileDialog


class Defaults():
    def __init__(self) -> None:
        self.importDefaults()

    def importDefaults(self, user="user"):
        """Imports defaults from user_settings.json or default_settings.son
            Stores within default settings"""
        if user != "user":
            with open('default_settings.json') as json_file:
                self.default_settings = json.load(json_file)
        else:
            with open('user_settings.json') as json_file:
                self.user_settings = json.load(json_file)

    def resetDefaults(self):
        """Sets user settings to default settings"""
        self.ImportDefaults(user="defaults")
        with open('user_settings.json', 'w') as outfile:
            json.dump(self.default_settings, outfile)

    def editDefaults(self, edits):
        """Adjusts user_settings to the information included in edits dicitonary"""
        for value in edits:
            self.user_settings[value] = edits[value]
        self.SaveDefaults()
        # Implement editing/saving within a GUI using values passed

    def saveDefaults(self):
        """Saves changed settings to user_settings.json"""
        with open('user_settings.json', 'w') as outfile:
            json.dump(self.user_settings, outfile)

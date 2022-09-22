import json
from tkinter.filedialog import SaveFileDialog


class Settings():
    def __init__(self) -> None:
        self.importSettings()

    def importSettings(self, default_settings=False):
        """Imports Settings from user_settings.json or default_settings.son
            Stores within default settings"""
        with open('default_settings.json') as json_file:
            self.default_settings = json.load(json_file)
        with open('user_settings.json') as json_file:
            self.user_settings = json.load(json_file)
        if default_settings:
            self.settings = self.default_settings
        else:
            self.settings = self.user_settings
        

    def resetSettings(self):
        """Sets user settings to default settings"""
        self.importSettings(default_settings=True)
        with open('user_settings.json', 'w') as outfile:
            json.dump(self.default_settings, outfile)

    def editSettings(self, edits):
        """Adjusts user_settings to the information included in edits dicitonary"""
        for value in edits:
            self.user_settings[value] = edits[value]
        self.SaveSettings()
        # Implement editing/saving within a GUI using values passed

    def saveSettings(self):
        """Saves changed settings to user_settings.json"""
        with open('user_settings.json', 'w') as outfile:
            json.dump(self.user_settings, outfile)

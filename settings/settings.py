import json
from tkinter.filedialog import SaveFileDialog


class Settings():
    def __init__(self) -> None:
        self.importSettings()

    def importSettings(self, user="user"):
        """Imports Settings from user_settings.json or default_settings.son
            Stores within default settings"""
        if user != "user":
            with open('default_settings.json') as json_file:
                self.default_settings = json.load(json_file)
                self.settings = self.default_settings
        else:
            with open('user_settings.json') as json_file:
                self.user_settings = json.load(json_file)
                self.settings = self.user_settings
        

    def resetSettings(self):
        """Sets user settings to default settings"""
        self.ImportSettings(user="Settings")
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

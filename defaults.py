import json


class Defaults():
    def __init__(self) -> None:
        self.ImportDefaults(user=True)

    def ImportDefaults(self, user=True):
        if user != True:
            with open('default_settings.json') as json_file:
                self.default_settings = json.load(json_file)
        else:
            with open('user_settings.json') as json_file:
                self.user_settings = json.load(json_file)

    def resetDefaults(self):
        self.ImportDefaults(user=False)
        with open('user_settings.json', 'w') as outfile:
            json.dump(self.default_settings, outfile)

    def editDefaults(self, edits):
        for value in edits:
            self.user_settings[value] = edits[value]
        # Implement editing/saving within a GUI using values passed

    def saveDefaults(self):
        with open('user_settings.json', 'w') as outfile:
            json.dump(self.user_settings, outfile)

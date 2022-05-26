import json


class Defaults():
    def __init__(self) -> None:
        self.ImportDefaults()

    def ImportDefaults(self, user="user"):
        if user != "user":
            with open('default_settings.json') as json_file:
                self.default_data = json.load(json_file)
        else:
            with open('user_settings.json') as json_file:
                self.user_data = json.load(json_file)

    def ResetDefaults(self):
        self.ImportDefaults(user="defaults")
        with open('user_settings.json', 'w') as outfile:
            json.dump(self.default_data, outfile)

    def EditDefaults(self, edits):
        for value in edits:
            self.user_data[value] = edits[value]
        # Implement editing/saving within a GUI using values passed

    def SaveDefaults(self):
        with open('user_settings.json', 'w') as outfile:
            json.dump(self.user_data, outfile)

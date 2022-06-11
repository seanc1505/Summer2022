from video import Video

from utilities.checkvalidfile import checkValidFile
from utilities.finddatecreated import findDateCreated
from utilities.checkvaliddir import checkValidDirectory
from utilities.findfilename import findFileName
import os
import shutil


class SourceVideo(Video):
    def __init__(self, path, default_settings) -> None:
        super().__init__(default_settings)
        self.video_path = checkValidFile(path)
        self.video_directory = os.path.dirname(self.video_path)
        self.video_name = findFileName(self.video_path)
        self.video_date_created = findDateCreated(self.video_path)

    def importVideo(self, import_to=""):
        if import_to == "":
            import_to = self.user_settings["import_to_path"]
        elif import_to[-4] == ".":
            import_to = os.path.dirname(import_to)
        if self.video_date_created not in import_to:
            import_to += "/" + self.video_date_created
        if not os.path.exists(import_to):
            import_to = checkValidDirectory(import_to)
        import_to += "/" + self.video_name
        if self.video_path != import_to:
            shutil.move(self.video_path, import_to)
            self.video_path = import_to
            self.video_directory = os.path.dirname(import_to)

    def renameGoproVideo(self):
        if self.video_name[:2] != "GH":
            print("Not a gopro file: " + self.video_name)
        if self.video_name[-7] != "_":
            chapter = "_" + self.video_name[2:4]
            self.video_name = self.video_name[:2] + \
                self.video_name[4:-4] + chapter + ".mp4"
            temp_name = self.video_directory + "/" + self.video_name
            os.rename(self.video_path, temp_name)
            self.video_path = temp_name
            self.video_directory = os.path.dirname(self.video_path)
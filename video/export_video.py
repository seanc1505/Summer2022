from video.video import Video
from utilities.checkvaliddir import checkValidDirectory

import os


class ExportVideo(Video):
    def __init__(self, path, default_settings) -> None:
        super().__init__(default_settings)

    def exportVideo(self):
        print("export video")

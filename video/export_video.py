from video.video import Video
from utilities.checkvaliddir import checkValidDirectory
import moviepy
import os


class ExportVideo(Video):
    def __init__(self, path, default_settings) -> None:
        super().__init__(default_settings)
        self.video_path = path

    def exportVideo(self, subclip_dict, name):
        print("export video")
        for video in subclip_dict:
            video_clip = moviepy.VideoFileClip((self.video_path+"/"+clip))

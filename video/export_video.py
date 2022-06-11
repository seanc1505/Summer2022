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
            video_clip = moviepy.VideoFileClip((self.video_path+"/"+video))
    
    def prepDictionary(self,dataframe):
            
        clip_time_dict = {}
        video_name_dict={}
        video_number_dict = {}
        self.video_clips_dict = {}
        prev_row = ""
        for index,row in dataframe.iterrows():
            # if index > 4: 
            #     break
            clip_time_dict['Start Time'] = row['Start Time']
            clip_time_dict['Stop Time'] = row['Stop Time']
            video_number_dict[row['Subclip Num']]=clip_time_dict.copy()
            if index >0:
                if row['Subclip Num'] == 0:
                    video_name_dict[prev_row['Video Name']] = video_number_dict.copy()
                    video_number_dict = {}
                
                if prev_row['Paddler'] != row['Paddler']:
                    self.video_clips_dict[prev_row['Paddler']] = video_name_dict.copy()
                    video_name_dict = {}
            
            prev_row=row

        video_name_dict[prev_row['Video Name']] = video_number_dict.copy()
        self.video_clips_dict[prev_row['Paddler']] = video_name_dict.copy()

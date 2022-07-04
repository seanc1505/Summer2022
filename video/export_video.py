from dataclasses import replace
from utilities.checkvaliddir import checkValidDirectory
import moviepy
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os


class ExportVideo():
    def __init__(self, defaults,dataframe) -> None:
        self.prepDictionary(dataframe)
        self.exportVideo(defaults)

    def exportVideo(self,defaults):
        for paddler in self.video_clips_dict:
            subclip_list = []
            for video in self.video_clips_dict[paddler]:
                video_clip = moviepy.VideoFileClip(
                            ( defaults.user_settings["source_path"]+"/"+video))
                for subclip in self.video_clips_dict[paddler][video]:
                    temp_dict = self.video_clips_dict[paddler][video][subclip]
                    current_subclip = video_clip.subclip(
                                        temp_dict["Start Time"], temp_dict["Stop Time"])
                    subclip_list.append(current_subclip)
            
            final_clip = concatenate_videoclips(subclip_list)
            video_name = self.processExportName(defaults,paddler)
            final_clip.write_videofile(video_name)
    
    def prepDictionary(self,dataframe):       
        clip_time_dict = {}
        video_name_dict={}
        video_number_dict = {}
        self.video_clips_dict = {}
        prev_row = ""
        for index,row in dataframe.iterrows():
            if index > 0:
                if row['Subclip Num'] == 0:
                    video_name_dict[prev_row['Video Name']] = video_number_dict.copy()
                    video_number_dict = {}
            clip_time_dict['Start Time'] = row['Start Time']
            clip_time_dict['Stop Time'] = row['Stop Time']
            video_number_dict[row['Subclip Num']]=clip_time_dict.copy()
            if index >0:
                if prev_row['Paddler'] != row['Paddler']:
                    self.video_clips_dict[prev_row['Paddler']] = video_name_dict.copy()
                    video_name_dict = {}
            prev_row=row
        video_name_dict[prev_row['Video Name']] = video_number_dict.copy()
        self.video_clips_dict[prev_row['Paddler']] = video_name_dict.copy()

    def processExportName(self,defaults,paddler):
        path = defaults.user_settings["export_path"]
        file_name = defaults.user_settings["export_name"]
        strings = "hello"
        file_name = file_name.replace("person",paddler)
        # update this with correct date, maybe from settings file_name = file_name.replace("date",date)
        return path + "/" + file_name + "_" +paddler + ".mp4"
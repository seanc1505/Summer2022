from video.video import Video
from utilities.checkvaliddir import checkValidDirectory
import moviepy
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os


class ExportVideo(Video):
    def __init__(self, path, default_settings) -> None:
        super().__init__(default_settings)
        self.video_path = path

    def exportVideo(self, name):
        print("export video")
        for paddler in self.video_clips_dict:
            subclip_list = []
            for video in self.video_clips_dict[paddler]:
                video_clip = moviepy.VideoFileClip(
                            ( self.video_path+"/"+video))
                for subclip in self.video_clips_dict[paddler][video]:
                    temp_dict = self.video_clips_dict[paddler][video][subclip]
                    print(video)
                    print(temp_dict)
                    current_subclip = video_clip.subclip(
                                        temp_dict["Start Time"], temp_dict["Stop Time"])
                    subclip_list.append(current_subclip)
            
            final_clip = concatenate_videoclips(subclip_list)
            video_name = self.video_path  +"/"+name +"_"+ paddler + self.video_date_created + ".mp4"
            final_clip.write_videofile(video_name)
    
    def prepDictionary(self,dataframe):       
        clip_time_dict = {}
        video_name_dict={}
        video_number_dict = {}
        self.video_clips_dict = {}
        prev_row = ""
        for index,row in dataframe.iterrows():
            
            # if index > 4: 
            #     break
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

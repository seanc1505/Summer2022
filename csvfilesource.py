from tkinter import filedialog
import os
import pandas as pd
from moviepy.video.compositing.concatenate import concatenate_videoclips
import moviepy
from moviepy.editor import *
from utilities.checkvaliddir import checkValidDirectory


class CsvFileSource():
    def __init__(self):
        pass

    def processCsvData(self, data):
        data.fillna("", inplace=True)
        for index, row in data.iterrows():
            temp_row = row
            for column in range(len(row)):
                if row[column] == "":
                    if index > 0:
                        temp_row[column] = prev_row[column]
                elif column > 1 and isinstance(temp_row[column], str):
                    time_list = temp_row[column].split(":", 1)
                    time = (float(time_list[0])*60) + float(time_list[1])
                    temp_row[column] = time
                if column == 0:
                    temp = str(row[column])
                    if temp[-4:] != ".mp4":
                        temp_row[column] = temp[:] + ".mp4"

            data.iloc[index] = temp_row
            prev_row = row
        return data

    def importVideoCsv(self):
        # Add a way to set the csv file name
        csv_name = filedialog.askopenfilename(title='Select csv file')
        self.source_video_path = os.path.dirname(csv_name)
        self.export_video_name = input("Enter the base name of the video: ")
        self.export_video_path = checkValidDirectory(
            dir="", check_name="Export video Path")
        raw_data = pd.read_csv(csv_name)
        self.data = self.processCsvData(raw_data)

    def exportVideoFromCsv(self):
        paddler_name_list = self.data['Paddler'].unique()
        video_name_list = self.data['Video Name'].unique()

        for paddler in paddler_name_list:
            subclip_list = []
            video_length = 0
            for video in video_name_list:
                video_clip = moviepy.VideoFileClip(
                    (self.source_video_path+"/"+video))
                for index, row in self.data.iterrows():
                    if row['Paddler'] == paddler:
                        if row['Video Name'] == video:
                            # Calculate full video length
                            current_subclip = video_clip.subclip(
                                row["Start Time"], row["Stop Time"])
                            subclip_list.append(current_subclip)
            print(subclip_list)
            final_clip = concatenate_videoclips(subclip_list)
            video_name = self.export_video_path+"/" + \
                paddler+"_" + self.export_video_name + ".mp4"
            final_clip.write_videofile(video_name)

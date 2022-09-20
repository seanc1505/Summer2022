from tkinter import filedialog
import os
from utilities.checkvaliddir import checkValidDirectory
import pandas as pd
from subprocess import Popen
from utilities.checkvalidfile import checkValidFile


class CsvFile():
    def __init__(self, default_settings) -> None:
        self.default_settings = default_settings

    def importCsv(self, path=""):
        if path == "":
            self.csv_path = checkValidFile(
                file=(self.default_settings["csv_path"]))
        else:
            self.csv_path = checkValidFile(
                file=path)
        self.raw_csv_data = pd.read_csv(self.csv_path)
        self.csv_data = self.processCsv(self.raw_csv_data)

    def createCsvManual(self):
        self.csv_path = checkValidDirectory(make_if_fail=False)
        self.csv_path += ("/" + input("Name of csv file for edit:"))
        if self.csv_path[-4:] != ".csv":
            self.csv_path += ".csv"
        with open(self.csv_path, 'w') as csvfile:
            csvfile.write(self.default_settings["csv_headings"])
        Popen(self.csv_path, shell=True)

    def createCsvAlgorithim(self):
        print("createCsvAlgorithim")

    def processCsv(self, data):
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

        data = data.sort_values(['Paddler','Video Name'])
        data = data.reset_index(drop=True)

        data['Subclip Num'] = 0
        for index,row in data.iterrows():
            if index > 0:
                if prev_row['Paddler'] == row['Paddler']:
                    # print("same paddles")
                    if prev_row['Video Name'] == row['Video Name']:
                        # print("same video name")
                        data.iloc[index,4] =  prev_row['Subclip Num']+1
                        row['Subclip Num'] = prev_row['Subclip Num']+1
            prev_row = row

            
        return data

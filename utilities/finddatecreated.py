import os
import datetime


def findDateCreated(path, return_format="%Y_%m_%d"):
    recorded_time = os.path.getmtime(path)
    date_recorded = datetime.datetime.utcfromtimestamp(
        recorded_time).strftime(return_format)
    return(date_recorded)

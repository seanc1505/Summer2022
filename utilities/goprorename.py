def goproRename(file_name):
    """Returns the Gopro file name from GH<01>9999 to GH9999_<01>"""
    if file_name[:2] != "GH":
        print("Not a gopro file: " + file_name)
        return file_name

    if file_name[-7] != "_":
                chapter = "_" + file_name[2:4]
                file_name = file_name[:2] + file_name[4:-4] +  chapter +".mp4"
    return file_name
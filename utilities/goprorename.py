def goproRename(file_name):
    if file_name[:2] != "GH":
        return file_name

    if file_name[-7] != "_":
                chapter = "_" + file_name[2:4]
                file_name = file_name[:2] + file_name[4:-4] +  chapter +".mp4"
    return file_name
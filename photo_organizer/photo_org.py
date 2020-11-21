import os
from PIL import Image
from random import randint

sourceFolder = "E:\\Pictures\\Photos"
targetFolder = "E:\\Pictures\\organized"
photoExtensions = [".jpg", ".png"]
videoExtensions = [ ".mp4", ".mov"]

def files_to_move(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            for extension in photoExtensions:
                if file.lower().endswith(extension):
                    count += 1
                    filepath = os.path.join(root, file)
                    year = get_year(filepath)
                    sort_file(file, filepath, year)

    print(f"\nThe number of items that corresponds to these extensions are: {count}")


def get_year(filePath):
    try:
        creation_date = Image.open(filePath)._getexif()[36867]
        return creation_date[0:4]
    except:
        return "unknown"



def sort_file(filename, filepath, year):
    dest_folder = os.path.join(targetFolder, year)
    if not os.path.exists(dest_folder):
        print(f"{filename}: {year} will go here: {dest_folder}")
        os.makedirs(dest_folder)
    os.rename(filepath, dest_folder + '\\' + str(randint(1,20))+ filename)
    print(filename + ' moved.')

files_to_move(sourceFolder)

# Fetch all photos to be organized
# move all pics into yearly folder

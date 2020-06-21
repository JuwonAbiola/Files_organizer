import shutil
import os
from os.path import expanduser

home = expanduser("~")
os.chdir(home)
current_folder = 'Files_organizer'
source = 'Downloads'
files = os.listdir(source)

print(source)


# Mac OS users only

def transfer(src, doc):
    location = src.get(ext, 'Documents')
    return shutil.move(f"{source}/{doc}", location) if not os.path.exists(f"{location}/{doc}") \
        else print(f'{doc} already exist in {location}')


for file in files:
    switcher = {
        '.mp3': 'Music',
        '.mp4': 'Movies',
        '.png': 'Pictures',
        '.jpg': 'Pictures',
        '.jpeg': 'Pictures',
    }
    ext = os.path.splitext(file)[1]
    if file != current_folder:
        transfer(switcher, file)

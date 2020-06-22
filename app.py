import shutil
import os
from os.path import expanduser
from pyfiglet import Figlet

os.chdir(expanduser("~"))
current_folder = 'Files_organizer'

print(Figlet(font='slant').renderText(current_folder))

print(f'Welcome to {current_folder} v1.0')
# Mac OS users only

source = input('Source Folder : ')

files = os.listdir(source)


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

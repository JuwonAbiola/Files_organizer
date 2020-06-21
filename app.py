import shutil
import os

source = '../'
files = os.listdir(source)

### Mac OS users only

def transfer(src, doc):
    location = src.get(ext, '../../Documents')
    return shutil.move(f"{source}{doc}", location) if not os.path.exists(f"{location}/{doc}") \
        else print(f'{doc} already exist in {location}')


for file in files:
    switcher = {
        '.mp3': '../../Music',
        '.mp4': '../../Movies',
        '.png': '../../Pictures',
        '.jpg': '../../Pictures',
        '.jpeg': '../../Pictures',
    }
    ext = os.path.splitext(file)[1]
    if file != 'Files_organizer':
        transfer(switcher, file)

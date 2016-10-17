import shutil
import os


sourcepath = '/Users/Development/Desktop/Python Item 59/Folder A'
source = os.listdir(sourcepath)
destination = '/Users/Development/Desktop/Python Item 59/Folder B'


for files in source:
    if files.endswith('.txt'):
        source_files = os.path.join(sourcepath,files)
        dest_files = os.path.join(destination,files)
        shutil.move(source_files,destination)
        print source_files


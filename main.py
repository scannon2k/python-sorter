#!/usr/bin/env python3
from importlib.resources import path
import os
import shutil

# Specify the filepath
path = 'C:\\Users\\seanc\\Downloads'

# Create a list of the files in the directory
file_list = os.listdir(path)

for file in file_list:
    name, ext = os.path.splitext(file)

    ext = ext[1:]

    # Iterate if directory
    if ext == '':
        continue

    # Move to extention folder or create new extention folder
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

#try block for error handling
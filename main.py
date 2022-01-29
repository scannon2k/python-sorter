#!/usr/bin/env python3
import os
import shutil
import logging
from importlib.resources import path
from configparser import ConfigParser

# Specify filepath from config.ini
config = ConfigParser()
config.read('config.ini')
path = config['filepath']['path']

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
# write to log.txt when encounter an error
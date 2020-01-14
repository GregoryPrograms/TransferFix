import os
import tkinter
from tkinter import filedialog
from pathlib import Path, PurePath
from os import path
from os.path import splitext

#  foldFix - replaces any underscores in folder names with a dash. Also, 
#converts folder title to sentence case.
#
#   Parameters: foldList - an array containing a foldObj describing each subfolder
# of the initially queried folder. foldObjs are a union of two objects, with
# foldObj[0] being the folder name, and foldObj[1] being the root path to it.
def foldFix(foldList):
    for item in reversed(foldList):
        newString = item[0].replace("_","-").title()
        os.rename(PurePath(item[1]) / item[0], PurePath(item[1]) / newString)
def fileFix(fileList):
    for item in fileList:
        newString = item[0].replace("_","-").title()
        os.rename(PurePath(item[1]) / item[0], PurePath(item[1]) / newString)
        
def main():
    tkinter.Tk().withdraw()
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to trim file names...'))
    foldList = []
    fileList = []
    for root, folders, files in os.walk(dirPath):
        for name in folders:
            foldObj = [name, root]
            foldList.append(foldObj)
        for name in files:
            fileObj = [name, root]
            fileList.append(fileObj)
    fileFix(fileList)
    foldFix(foldList)
if(__name__ == "__main__"):
    main()
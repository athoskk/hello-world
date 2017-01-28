#!/usr/bin/python

import os
import sys
import shutil

"piccvt.py SourceDir ObjectDir"

def listDirectory(srcDirectory, dstDirectory, fileExtName):
    "get list of file info objects for files of particular extensions"
    
    # normcase
    fileList = [os.path.normcase(f) for f in os.listdir(srcDirectory)]
    srcFileList = [os.path.join(srcDirectory, f) for f in fileList
                            if os.path.splitext(f)[1] in fileExtName]
    dstFileList = [os.path.join(dstDirectory, "cvt_" + f) for f in fileList
                            if os.path.splitext(f)[1] in fileExtName]

    return srcFileList, dstFileList

if __name__ == "__main__":
    if len(sys.argv) < 2:
        (src, dst) = listDirectory("/home/kimi/Pictures", "/home/kimi/Pictures", [".jpg", ".JPG"])
        #print src
        #print dst
    else:
        (src, dst) = listDirectory(sys.argv[1], sys.argv[2], [".jpg", ".JPG"])
        #print src
        #print dst

    fileListLen = len(src)
    for i in range(fileListLen):
        commandStr = "convert -resize 1920 -quality 70% " + src[i] + " " + dst[i]
        print commandStr
        os.system(commandStr)


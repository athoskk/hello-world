import os
import sys
import shutil

"cp.py SourceDir ObjectDir"

def listDirectory(directory, objdirectory, fileExtList):                                        
    "get list of file info objects for files of particular extensions"
    fileList = [os.path.normcase(f)
                for f in os.listdir(directory)]           
    srcfileList = [os.path.join(directory, f) 
               for f in fileList
                if os.path.splitext(f)[1] in fileExtList]
    objfileList = [os.path.join(objdirectory, f) 
               for f in fileList
                if os.path.splitext(f)[1] in fileExtList]

    #print fileList
    #print srcfileList
    #print objfileList
    
    fileListLen = len(srcfileList)
    for i in range(fileListLen):
        shutil.copyfile(srcfileList[i], objfileList[i])

    
if __name__ == "__main__":
	if len(sys.argv) < 3:
		print u'Input a directory!'
		print u'cp.py SourceDir ObjectDir'
	else:
		obj = 1
		directory = sys.argv[1]
		fileList = [os.path.normcase(f)
                for f in os.listdir(directory)]
		srcfileList = [os.path.join(directory, f) 
               for f in fileList]
		for file in srcfileList:
			if os.path.isdir(file):
				obj = obj + 1
				objdir = 'img' + str(obj)
				dir = os.path.join(sys.argv[2], objdir) 
				print dir
				os.mkdir(dir)
				listDirectory(file, dir, [".jpg"])
				listDirectory(file, dir, [".jpeg"])
				

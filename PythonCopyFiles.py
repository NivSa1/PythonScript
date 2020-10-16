
#import libraries
import shutil
import os
import glob

#Source of the files you want to copy
srcname = input("Enter source path:")
#Destination of the copied files
desname = input("Enter destination path:")

#count files copied
num = 1

listsrc = list(srcname)
#Check if the source contains * at the last char
if (listsrc[len(listsrc)-1]=="*"):
    folders=glob.glob(srcname)
    #Runs on all existing folders
    for folder in folders:
        files=glob.glob(folder+"/"+"*.jpg")
        #Run on all the files in the specific folder
        for file in files:
            file="".join(file)
            fname,fext = os.path.splitext((os.path.basename(file)))
            #make the name format
            text=("{:06d}").format(int(num))
            newname = desname+"/F"+text+"T"+fname+fext
            #Copy file to the destination path
            shutil.copy(file,newname)
            num+=1
else:
    #A message that does not have an '*' at the end of the path
    raise ValueError("Please enter a source path with '*' at the end")    
    

        
        

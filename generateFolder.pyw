from sys import argv
import os
import ntpath
import shutil

cwd = os.getcwd()

#Get file name
def getFileNameFromPath(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#Create a folder and move the files into that folder
if len(argv) > 1:
    filename = getFileNameFromPath(argv[1])
    noFanSub = filename.split("] ", 1)
    noEpisode = noFanSub[1].split(" -", 1)
    if not os.path.isdir(noEpisode[0]):
        os.mkdir(noEpisode[0])

    for i in range(len(argv)):
        if i == 0:
            continue
        shutil.move(argv[i], f'{cwd}\\' + noEpisode[0])

#Renaming a file
# time.sleep(5.5)
# filename = getFileName(argv[1])
# newFileName = filename.replace("e", "a")
# os.rename(f'{cwd}\\' + filename, f'{cwd}\\' + newFileName)


# if(len(argv) > 1):
#     subprocess.call(['C:\Program Files\MPC-HC\mpc-hc64.exe', argv[1]])
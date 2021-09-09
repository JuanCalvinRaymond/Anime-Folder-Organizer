from sys import argv
import os
import ntpath
import shutil
import time

#Show a popup to test if the script is running
import tkinter as tk

# master = tk.Tk()

# def write_slogan():
#     info_message = "Your message"
#     tk.Label(master, text=info_message).grid(row=2, column=1) 

# btn = tk.Button(master, text='ORDER Number', command=write_slogan)
# btn.grid(row=3, column=1, sticky=tk.W, pady=4)

# master.mainloop()

cwd = os.getcwd()


# #Create a folder and move the files into that folder
if len(argv) > 1:
    folderName = argv[1]
    noDriveLetter = folderName.split("\\", 1)
    animeFolder = noDriveLetter[len(noDriveLetter) - 1]
    if animeFolder.startswith("["):
        noFanSub = folderName.split("] ", 1)
        noContext = noFanSub[1].split(" (", 1)
    else: 
        noFanSub = animeFolder
        noContext = noFanSub.split(" (", 1)
    animeName = noContext[0].split(" [", 1)
    os.rename(argv[1], f'{cwd}\\' + animeName[0])

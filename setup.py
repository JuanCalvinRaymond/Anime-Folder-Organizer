import os
import sys
import winreg as reg

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
python_exe = sys.executable

#Generate Anime Folder
#mp4, mkv, avi vlc
file_extension = [".mp4", ".mkv", ".avi", ".vlc"]

for extension in file_extension:
    key_path = r"SystemFileAssociations\\" +  extension + "\\shell\\Generate Folder"

    key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)
    reg.SetValue(key, '', reg.REG_SZ, "&Generate folder")

    key1 = reg.CreateKeyEx(key, r"command")
    reg.SetValue(key1, '', reg.REG_SZ, f"C:\\Windows\\pyw.exe" + f' "{dir_path}\\generateFolder.pyw"' + ' "%1"')

#Rename Anime Folder
key_path = r"Directory\\shell\\Rename Anime Folder"

key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, "&Rename folder")

key1 = reg.CreateKeyEx(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, f"C:\\Windows\\pyw.exe" + f' "{dir_path}\\renameFolder.pyw"' + ' "%1"')


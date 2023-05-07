import os
import glob
def find():
     directory_path = "/sdcard/DCIM/Camera" # Change this to the path of your directory

     jpg_files = len(glob.glob(directory_path + "/*.jpg"))
     os.system("termux-tts-speak directory sdcard dcim camera jpg file reading sir please whait sir")
     os.system("figlet writing sir ")

     print("JPG files in directory:", jpg_files)
     os.system(f'termux-tts-speak {jpg_files} jpg files')
   
find()

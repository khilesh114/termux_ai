import os
os.system("echo -e '\033[0;32m print'")
jpg_files = os.system('termux-media-scan -r -v file /sdcard/DCIM/Camera')
print("JPG files in directory:", jpg_files)
   
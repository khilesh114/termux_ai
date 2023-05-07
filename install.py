import os
os.chdir("/sdcard")
#os.system("ls")
print("creatint a folder tfish")
if not os.path.exists("tfish"):
    os.system("mkdir tfish")
    os.system("mkdir /sdcard/tfish/back")
    print("done")
else:
    print("allredy install ")
    print("run python tfish.py")
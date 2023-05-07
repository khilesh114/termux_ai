import subprocess
import random
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("\033[95m You said: ",str(inp))
os.system("figlet SWATI ")
def songs():
    set = ("a.mp3","b.mp3")
    random = random.choice(set)
    print(random)
    os.system(f"play {random}")
    
def wallpaper(): #wallpaper set
     os.system("bash wallpaper.sh")
     os.system(f"termux-wallpaper  -f 'image.jpg' ")
def system():
     if inp == "":
         subprocess.call(["termux-tts-speak","please tell something sir"])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
     elif "close" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good sir "])
         
     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)
         
     elif "torch on" in inp:
         os.system("termux-torch on")
     elif "torch off" in inp:
         os.system("termux-torch off")
     
         
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am your virtual assistanct Termux, sir"])
         
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
     
     elif "name" in inp:
         subprocess.call(["termux-tts-speak","you can call me swati "])
         
     elif "good job" in inp:
         subprocess.call(["termux-tts-speak","thank you sir"])
         
     elif "back camera" in inp:
         subprocess.call(["termux-tts-speak","oky sir i am click a photo 3 back camera"])
         os.system("python3 back.py")
         
     elif "simple camera" in inp:
         subprocess.call(["termux-tts-speak","oky sir i am click a photo selfiy camera"])
         os.system("python3 front.py") 
         
     elif "wallpaper" in inp:
         wallpaper()
         subprocess.call(["termux-tts-speak","wallpaper set sir"])
         
     elif "play song" in inp:
         subprocess.call(["termux-tts-speak","oky sir i am play song my choice random"])
         os.system("bash song.sh")
         os.system("python3 song.py")
         
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","I CREATING BY KHILESH"])
     elif "thank you" in inp:
         subprocess.call(["termux-tts-speak","welcome sir"])
         
     elif "directory" in inp:
         os.system("python3 count1.py")
         os.system("python3 count.py")   
     else:
       subprocess.call(["termux-tts-speak","I apane code nahi kiya hai plase code me"])

system()

os.system("python main.py")
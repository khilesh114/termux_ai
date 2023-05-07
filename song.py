import os
import random
set = ("a.mp3","b.mp3")
random = random.choice(set)
print(random)
os.system(f"play {random}")
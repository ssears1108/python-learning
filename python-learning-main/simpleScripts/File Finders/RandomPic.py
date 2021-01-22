#script to find a random photo
#works for a path with a fold specified
import random
import os

path= "C:\\Users\\ssear\\Pictures\\wall paper and screen savers"
#path="C:\\Users\\ssear\\Desktop\\python work\\simpleScripts\\RandomPicFind\\wall paper and screen savers"
files=os.listdir(path)
#files=os.listdir(path)
d=random.choice(files)
#os.startfile(d)
x = os.path.join(path, d)
os.startfile(x)
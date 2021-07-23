import os,glob

files = glob.glob("/home/subash/Projects/1000/micro_v2/sm/area/5612.csv")

for file in files:
    #print(file)
    b = os.path.getsize(file)
    break
    if b == 305:
        print(file)

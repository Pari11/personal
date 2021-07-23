
import os,glob
from natsort import natsorted
import csv 
from datetime import datetime
import datetime as dt
import time

dir_home = os.path.expanduser("~")
watch_folder = os.path.join(dir_home,'Pictures')
files = natsorted( glob.glob(os.path.join(watch_folder,"*")),reverse = True)

for file in files:
    d = datetime.strptime(time.ctime(os.path.getctime(file)),"%a %b %d %H:%M:%S %Y")
    c1 = d.date()
    a = datetime.now()
    t_date= a.date()
    dif = t_date - c1  
    d = int(dif.days)
    print(d)
    if d < 89 :
        os.remove(file)
    print(file)
    #break

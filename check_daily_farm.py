#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 07:38:21 2021

@author: satyukt
"""

import os,glob
from natsort import natsorted
import csv 
from datetime import datetime
import datetime as dt
import time

dir_home = os.path.expanduser("~")
watch_folder = os.path.join(dir_home,'Projects/1000/micro_v2/sm/area')
files = natsorted( glob.glob(os.path.join(watch_folder,"*")),reverse = True)

n = 1
count = 0 
for file in files:
    d = datetime.strptime(time.ctime(os.path.getctime(file)),"%a %b %d %H:%M:%S %Y")
    c1 = d.date()
    a = datetime.now()
    t_date= a.date()
    #print(a.date())
    #print(c1)
    #break
    dif = t_date - c1  
    d = int(dif.days)
    #print(d)
    if d == n :
        print(file)
        print(n)
        count = count + 1
        #os.remove(file)
    
print(count)

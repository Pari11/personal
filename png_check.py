#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:18:12 2021

@author: satyukt
"""
import os,glob
from natsort import natsorted
import csv 
from datetime import datetime

dir_home = os.path.expanduser("~")
watch_folder = os.path.join(dir_home,'Projects/1000/micro_v2/sm/aws/png/')
files = natsorted( glob.glob(os.path.join(watch_folder,"*")),reverse = True)
dir_log = os.path.join(dir_home,'pari/1005')

count = 0
for file in files:
    try:
    
        #print(file)
        file_name = str(file[48:]) 
        #print(file_name) 
        date = natsorted(glob.glob(os.path.join(file,"*png")),reverse = True)
        f_id =  date[0]
        f_id = str(f_id[56:-11])
        #file_name = str(file[48:]) 
        f_date = datetime. strptime(f_id, '%Y%m%d')
        
        date = []
        a = datetime.now()
    
        f_date = f_date.date()
        t_date = a.date()
        #t_date = datetime. strptime(a, '%Y%m%d')
        print(f_date)
        print(t_date)
        
        dif = t_date - f_date  
        print(dif.days)
        #break
        d = int(dif.days)
        if d > 12 :
            print(file_name)
            count = count + 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        #break
        
        
    except:
        print("some error")
print("Number of unupdated farms")    
print(count)   


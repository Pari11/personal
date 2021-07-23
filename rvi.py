#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 12:24:57 2021

@author: subash
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import rioxarray as rxr


def RVI(vv_file, vh_file):
    var1 = (4*vh)
    var2 = (vv+vh)
    RVI = var1/var2
    
    return(RVI)
    

#vv_path = "/media/subash/BKUP/micro/bindusen/farm/rvi/bc/5128/S1A_IW_GRDH_1SDV_20210407T004010_20210407T004035_037337_046643_E8B3_VV.tif"
#vh_path = "/media/subash/BKUP/micro/bindusen/farm/rvi/bc/5128/S1A_IW_GRDH_1SDV_20210407T004010_20210407T004035_037337_046643_E8B3_VH.tif"


vv = rxr.open_rasterio(vv_path, masked=True).squeeze()
vh = rxr.open_rasterio(vh_path, masked=True).squeeze()

var1 = (4*vh)
var2 = (vv+vh)

RVI = var1/var2

#RVI.plot()
#plt.show()

RVI.rio.to_raster("/media/subash/BKUP/micro/bindusen/farm/rvi/rvi/5128.tif")

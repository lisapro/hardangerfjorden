#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 11. mai 2017

Module creates relaxation input files for Hardangerfjord modelling 

@author: ELP
'''
import tkinter as tk
import os,sys
from netCDF4 import Dataset,num2date
from PyQt5 import QtGui, QtCore
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import interpolate
from tkinter.filedialog import askopenfilename

#To show only the dialog without any other GUI elements
root = tk.Tk()
root.withdraw()

#We get the whole path to file
ask_filename = askopenfilename(initialdir= os.getcwd(),
filetypes =(("NetCDF file", "*.nc"),
("All Files","*.*")),title = "Choose a file.")

fname = os.path.split(ask_filename)[1]
print (ask_filename)

fh = Dataset(ask_filename)
for names,vars in fh.variables.items():
    print (names, vars.units)

time = np.array(fh.variables['time'][0:365])
dates = num2date(time[:],units='days since 1985-01-01',
                 calendar='Gregorian' )
depth = np.array(fh.variables['depth'][0:8])

#no3 = np.array(fh.variables['N3n'][:,0:8,13,15])
po4 = np.array(fh.variables['N1p'][:,0:8,13,15])
lat = np.array(fh.variables['lat'])
lon = np.array(fh.variables['lon'])

o2_field = [ 219.468, 243.293, 212.332 ]
no3_field = [11.786,11.429, 12.857] #,      
po4_field = [0.97,0.94,1.19]
   
depth_field = [98,250,500]


depth_appended = np.append([depth],[depth_field])
var_appended = []

#combine model data and field data ( below 75 m) 

for n in range(0,365):
    #c = np.append([no3[n]],[no3_field])
    #c = np.append([o2[n]],[o2_field])
    c = np.append([po4[n]],[po4_field])
    var_appended.append(c)
    
# interpolate to model depths
depth_new = [0,3,10,15,25,50,75,100,150,200,250,299.75,312.14,312.3571]
var_int = []
depth_new_2d = []

days = []
for n in range(0,14):
    day = 1 
    for n in range(0,365):
        days.append(day)
        day += 1 
days = np.array(days)

for n in range(0,365):
    f = interpolate.interp1d(depth_appended,var_appended[n],
                              bounds_error=False,
                              fill_value='extrapolate',
                              kind = 'linear')#'nearest')
    xnew = f(depth_new)   # use interpolation function returned by `interp1d`
    var_int.append(xnew)
    depth_new_2d.append(depth_new)

var_hardanger = (np.array(var_int).T).flatten()
depth_hardanger = (np.array(depth_new_2d).T).flatten()

figure1 = plt.figure()
gs1 = gridspec.GridSpec(1,1)
ax111 = figure1.add_subplot(gs1[0])


for n in range(0,365):
    plt.plot(var_int[n],depth_new,'o--')
    #plt.plot(o2_hardanger[n],depth_new,'o--')
    #plt.plot(no3[n],depth)

#plt.plot(o2_field,depth_field,'ko-')   
#plt.plot(no3_field,depth_field,'ko-')   
#plt.plot(po4_field,depth_field,'ko-')
#    
plt.ylim(350,0)    
plt.show()





#print (days.shape, depth_hardanger.shape, o2_hardanger.shape)
#combined = np.vstack((days,depth_hardanger, var_hardanger)).T
#np.savetxt('hardanger_no3_out.dat', (combined), delimiter=' ')  
#np.savetxt('hardanger_o2_out.dat', (combined), delimiter=' ')  
#np.savetxt('hardanger_po4_out.dat', (combined), delimiter=' ') 


if __name__ == '__main__':
    pass
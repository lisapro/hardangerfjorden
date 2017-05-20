'''
Created on 19. mai 2017

@author: ELP
'''

import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

with open('wat_hardan1.txt', 'r') as f:
    # important to specify delimiter right 
    reader = csv.reader(f, delimiter='\t')
    r = []
    for row in reader:
        # if you don't know which delimiter is used 
        # print one row to view it 
        #print (row)
        #break
        r.append(row) 
r1 = np.transpose(np.array(r[1:]) ) # skip two header lines
st  = r1[0]   
lat = r1[1]     
lon = r1[2]   
nh4 = r1[3]   
#nh4_masked = np.ma.masked_where(nh4 == 'NaN' , nh4)
po4 = r1[4]  
fe = r1[5]  
doc = r1[6]  
mn = r1[7]  
no3no2 = r1[8]  
si = r1[9]  
tot = r1[10]  
ptot = r1[11]  
ptot2 = r1[12]  
pressure = r1[13] 

#for n,m in enumerate(st):
#    print (n,m)

start_list = [0,7,12,17,23,28] 
end_list = [7,12,17,23,28,33]
st_list = [1,2,3,4,5,6]

plt.style.use('ggplot')
figure1 = plt.figure(figsize=(10, 8 ), dpi=100)
gs = gridspec.GridSpec(2, 2) #xy

#print (nh4,pressure)
ax = figure1.add_subplot(gs[0])
ax1 = figure1.add_subplot(gs[1])
ax2 = figure1.add_subplot(gs[2])
ax3 = figure1.add_subplot(gs[3])

#ax3 = figure1.add_subplot(gs[2])
#ax4 = figure1.add_subplot(gs[3])
#axis.scatter(nh4,pressure)
def toplot(var,axis,title,y0,ymax):
    for m in range(0,6):
        axis.plot(var[start_list[m]:end_list[m]], 
                pressure[start_list[m]:end_list[m]],'o-',alpha = 0.7)        
        #axis.annotate(st_list[m],(var[start_list[m]],pressure[start_list[m]]),
        #              textcoords='offset points', xytext=(3, 3))
        
        axis.scatter(var[33],pressure[33],c = '#8b0000')
        axis.set_ylim(ymax,y0)
        axis.set_title(title)
        
#              linewidth = 0.4, linestyle =  '-', marker='o',
#               markersize= 4) 

        #toplot(si,ax2,'Si')    

    
        
        #pdf.savefig(figure1)
    

toplot(no3no2,ax,'NO3+NO2',-5,100)
toplot(no3no2,ax2,'NO3+NO2',100,700)
toplot(po4,ax1,'po4',-5,100)
toplot(po4,ax3,'po4',100,700)

plt.show()   
plt.savefig('po4.png')
plt.close() 
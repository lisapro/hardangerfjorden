'''
Created on 16. mai 2017

@author: ELP
'''
import matplotlib.gridspec as gridspec
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
#import Image


fig = plt.figure(figsize=(11.69,8.27), dpi=100)

gs = gridspec.GridSpec(1,1)
gs.update(left = 0.01,right = 0.95,bottom = 0.01, top = 0.95) 
ax = fig.add_subplot(gs[0])
#ax = plt.subplot2grid((2, 2), (0, 0), rowspan=2)
#ax01 = plt.subplot2grid((2, 2), (0, 1))
#ax02 = plt.subplot2grid((2, 2), (1, 1))

# setup Lambert Conformal basemap.
#m = Basemap(width=12000000,height=9000000,projection='lcc',
m = Basemap(projection='merc',llcrnrlat=59.9,
            urcrnrlat=60.2,
            llcrnrlon=5.6,urcrnrlon=6.1,
            resolution='f',ax = ax)
'''   
m1 = Basemap(projection='merc',llcrnrlat = 60.1,
             urcrnrlat=60.15,
            llcrnrlon=5.9,urcrnrlon=6,
            resolution='h',ax = ax01)         #,lat_ts=60 '''

        #resolution='f',lat_1=55,lat_2=80,lat_0=50, lon_0=5)
       
parallels = [59.9,60, 60.1,60.2]
meridians = [5.6,5.8, 6]
# labels = [left,right,top,bottom]
m.drawparallels(parallels, labels = [1,1,1,1]) # draw parallels
#m1.drawparallels([60.1,60.15], labels = [0,1,1,1]) # draw parallels
m.drawmeridians(meridians, labels = [1,1,1,1]) # draw parallels
#m1.drawmeridians([5.9,5.95,6], labels = [1,1,1,1]) # draw parallels
# f - full resolution 
# draw coastlines.
#m.drawcoastlines()
#m1.drawcoastlines()


# draw a boundary around the map, fill the background.
# this background will end up being the ocean color, since
# the continents will be drawn on top.
m.drawmapboundary(fill_color='#cae2f7')
#m1.drawmapboundary(fill_color='#cae2f7')
#m.shadedrelief()
# fill continents, set lake color same as ocean color.
m.fillcontinents(color='#bdad95',lake_color='aqua')
#m1.fillcontinents(color='#bdad95',lake_color='aqua')    

lon = [5.861 , 5.7815, 5.769, 5.959, 5.928, 5.925] 
lat = [59.97478, 59.97821, 59.9757, 60.0471, 60.1239, 60.1212]
lon_sed = 5.684
lat_sed = 59.9522

lon_sed2 = 5.667
lat_sed2 = 59.95

name_sed = ['199']
name_sed2 = ['200']

lon7 = 5.930716667
lat7 = 60.12692
name = ['st1 ','st2','st3','st4','st5','st6']
#X,Y = m(lon,lat)


x1,y1 = m(lon[0],lat[0])
x2,y2 = m(lon[1],lat[1])
x3,y3 = m(lon[2],lat[2])
x4,y4 = m(lon[3],lat[3])
x5,y5 = m(lon[4],lat[4])
x6,y6 = m(lon[5],lat[5])
x7,y7 = m(lon7,lat7)

x_sed1,y_sed1 = m(lon_sed,lat_sed)
x_sed2,y_sed2 = m(lon_sed2,lat_sed2)

x_farm1 = 5.772001
y_farm1 = 59.977903

x_farm2 = 5.939457
y_farm2 = 60.106703

x_farm3 = 5.931092
y_farm3 = 60.126556


x_farm4 = 5.908662
y_farm4 = 60.121650 

x_farm5 = 5.669370  
y_farm5 = 59.954219
 
'''
x6_1,y6_1 = m1(lon[5],lat[5])
x7_1,y7_1 = m1(lon7,lat7)
x5_1,y5_1 = m1(lon[4],lat[4])'''
m.scatter(lon, lat,latlon= True , color ='#ff7e37',
          edgecolor = '#995f3f', s= 55, zorder = 10, label = "water profiles")

m.scatter(lon_sed, lat_sed,latlon= True , color ='#b8894e',  label = "sediment profiles", 
          edgecolor = '#49361f', s= 55, zorder = 10)
m.scatter(lon_sed2, lat_sed2,latlon= True , color ='#b8894e',
          edgecolor = '#49361f', s= 55, zorder = 10)

m.scatter(lon7,lat7,latlon= True , color ='#ff7e37',
          edgecolor = '#995f3f', s= 55, zorder = 10)

m.scatter(x_farm1,y_farm1,latlon = True, marker = "*", 
          color ='#f6e32c', edgecolor = '#b8894e',
          label = 'Fish farm',s = 85, zorder = 10 ,alpha = 1)
m.scatter(x_farm2,y_farm2,latlon = True, marker = "*", color ='#f6e32c',
           s = 85, edgecolor = '#b8894e', zorder = 10 ,alpha = 1)
m.scatter(x_farm3,y_farm3,latlon = True, marker = "*", color ='#f6e32c',
           s = 85, edgecolor = '#b8894e', zorder = 10 ,alpha = 1)
m.scatter(x_farm4,y_farm4,latlon = True, marker = "*", color ='#f6e32c',
           s = 85, edgecolor = '#b8894e', zorder = 10 ,alpha = 1)
m.scatter(x_farm5,y_farm5,latlon = True, marker = "*", color ='#f6e32c',
           s = 85, edgecolor = '#b8894e', zorder = 10 ,alpha = 1)

'''
m1.scatter(x5_1,y5_1, color ='r',
          edgecolor = '#995f3f', s= 55, zorder = 10 )
m1.scatter(lon7,lat7,latlon= True , color ='r',
          edgecolor = '#995f3f', s= 55, zorder = 10 )
m1.scatter(lon[5],lat[5],latlon= True , color ='r',
          edgecolor = '#995f3f', s= 55, zorder = 10 )'''

txtsize = 15 
#for i, (x, y) in enumerate(zip(X, Y), start=1):
#    ax.annotate(name[i], (x,y), xytext=(9, -7),
# textcoords='offset points')
st = 0 
import matplotlib.patches as patches
from matplotlib.patches import Ellipse


for xy in ((x1,y1), (x2,y2)) :
    ax.annotate(name[st], xy,xytext=(7, -19), size= txtsize, 
                arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
                textcoords='offset points')
    st += 1
    
    
ax.annotate('st3 ', (x3,y3), xytext=(-3, -19),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
            textcoords='offset points')
ax.annotate('st4 ', (x4,y4), xytext=(1, -19),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')
ax.annotate('st5 ', (x5,y5), xytext=(12, 0),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')
ax.annotate('st199 ', (x_sed1,y_sed1), xytext=(12, -15),size= txtsize,
             textcoords='offset points')

ax.annotate('st200 ', (x_sed2,y_sed2), xytext=(12, -25),size= txtsize,
             textcoords='offset points')

ax.annotate('st6 ', (x6,y6), xytext=(12,-12),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')   

 
ax.annotate('st7', (x7,y7), xytext=(12,15),size= txtsize,
            arrowprops=dict(arrowstyle="-",connectionstyle="arc3"),
             textcoords='offset points')    
'''
ax01.annotate('st7 Fish Farm', (x7_1,y7_1), xytext=(12,15),size= txtsize,
            arrowprops=dict(arrowstyle="-",connectionstyle="arc3"),
             textcoords='offset points')   
ax01.annotate('st6 ', (x6_1,y6_1), xytext=(12,-12),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')  
ax01.annotate('st5 ', (x5_1,y5_1), xytext=(22, -5),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')'''
#for i, txt in enumerate(name):
#ax.text("1", lon[0],lat[0])

#x,y = m(5.861, 59.9)
#plt.text(x,y,'0')
#axins = zoomed_inset_axes(ax, 0.5, # zoom = 0.5
#                          loc=2)
#import imghdr
#image = np.array(Image.open('farm.png'))
#mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")
im = plt.imshow(plt.imread('farm.png'), extent=(1, 2, 1, 2))
#ellipse = patches.Ellipse( (x_farm,y_farm), width=2,
#                            height=1,angle = 45, 
#                            alpha = 1, zorder = 10)


plt.legend()
plt.show()

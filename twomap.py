from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes,inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import numpy as np
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(11.69,8.27), dpi=100)
gs = gridspec.GridSpec(1,1)
gs.update(left = 0.00,right = 0.71,bottom = 0.01, top = 0.95) 
ax = fig.add_subplot(gs[0])

gs2 = gridspec.GridSpec(1,1)
gs2.update(left = 0.65,right = 0.95,bottom = 0.3, top = 0.99) 
ax2 = fig.add_subplot(gs2[0])

map = Basemap(#width=150000,height=990000,
            resolution='l',projection='stere',\
            lat_0=70,lon_0=14,
            llcrnrlon = 5 ,llcrnrlat = 54 ,
            urcrnrlon = 27 ,urcrnrlat =70,ax = ax )

map2 = Basemap(projection='merc',llcrnrlat = 59.9,
             urcrnrlat=60.2,
            llcrnrlon=5.6,urcrnrlon=6.1,
            resolution='h',ax = ax2)         #,lat_ts=60 


x_patch,y_patch = map2(5.6,59.9)
x_patch2,y_patch2 = map2(5.6,60.2)

map.drawmapboundary(fill_color='#cae2f7')
map.fillcontinents(color='#bdad95')
map.drawcoastlines(linewidth=0.5)

map2.drawmapboundary(fill_color='#cae2f7')
map2.fillcontinents(color='#bdad95')
map2.drawcoastlines(linewidth=0.5)


parallels = [55,60,65,70]
meridians = [5,10,15,20]

parallels2 = [59.9,60,60.1,60.2]
meridians2 = [5.4,5.6,5.8,6]

map.drawparallels(parallels, labels = [1,1,0,0]) # draw parallels
map.drawmeridians(meridians, labels = [0,0,1,1]) # draw parallels

map2.drawparallels(parallels2, labels = [1,1,1,1]) # draw parallels
map2.drawmeridians(meridians2, labels = [1,1,1,1]) # draw parallels


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


x1,y1 = map2(lon[0],lat[0])
x2,y2 = map2(lon[1],lat[1])
x3,y3 = map2(lon[2],lat[2])
x4,y4 = map2(lon[3],lat[3])
x5,y5 = map2(lon[4],lat[4])
x6,y6 = map2(lon[5],lat[5])
x7,y7 = map2(lon7,lat7)

x7_1,y7_1 = map(lon7,lat7)

x_sed1,y_sed1 = map2(lon_sed,lat_sed)
x_sed2,y_sed2 = map2(lon_sed2,lat_sed2)


def plot_m(xf,yf,mapf,size,color,edgecolor,label = None, marker = None):

    mapf.scatter(xf,yf,latlon = True, marker = marker,
                color = color, s = size , edgecolor = edgecolor,
                label = label, zorder = 10 ,alpha = 1)

starsize = 105  
s_ecolor = '#235063' 
star_ecolor = '#f29f10' #'k' ##824c02
dot_size = 55
farmcolor = '#f6e32c'  
sed_color ='#880303'
wat_color = '#007cb2'

plot_m(lon_sed, lat_sed,map2,dot_size,sed_color,s_ecolor,"sediment station")
plot_m(lon_sed2, lat_sed2,map2,dot_size,sed_color,s_ecolor)

plot_m(lon7, lat7,map2,dot_size,wat_color,s_ecolor)
plot_m(lon, lat,map2,dot_size,wat_color,s_ecolor,"water column station")

plot_m(lon7,lat7,map,550,farmcolor,s_ecolor,None,"*")   

plot_m(x_farm1,y_farm1,map2,starsize,farmcolor,star_ecolor,'Fish farm',"*")       
plot_m(x_farm2,y_farm2,map2,starsize,farmcolor,star_ecolor,None,"*") 
plot_m(x_farm3,y_farm3,map2,starsize,farmcolor,star_ecolor,None,"*")
plot_m(x_farm4,y_farm4,map2,starsize,farmcolor,star_ecolor,None,"*")
plot_m(x_farm5,y_farm5,map2,starsize,farmcolor,star_ecolor,None,"*")  

txtsize = 10

def to_annotate(title,coords,txt_coords,axis):  
    axis.annotate(title, coords, xytext = txt_coords,size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
            textcoords='offset points')

to_annotate('st1', (x1,y1),(7, -19),ax2) 
to_annotate('st2', (x2,y2),(7, -19),ax2) 
to_annotate('st3', (x3,y3),(-3, -19),ax2) 
to_annotate('st4', (x4,y4),(1, -19),ax2) 
to_annotate('st5', (x5,y5),(12, 0),ax2) 
to_annotate('st6', (x6,y6),(12, -12),ax2) 
to_annotate('st7', (x7,y7),(12, 15),ax2) 

to_annotate('st199', (x_sed1,y_sed1),(12, -15),ax2) 
to_annotate('st200', (x_sed2,y_sed2),(12, -25),ax2) 
      
'''    
from matplotlib.patches import ConnectionPatch
con = ConnectionPatch(xyA=(x_patch,y_patch), xyB=(x7_1,y7_1),
                       coordsA="data", coordsB="data",
                      axesA=ax2, axesB=ax, color="k")
con2 = ConnectionPatch(xyA=(x_patch2,y_patch2), xyB=(x7_1,y7_1),
                        coordsA="data", coordsB="data",
                      axesA=ax2, axesB=ax, color="k")
ax2.add_artist(con)
ax2.add_artist(con2)
'''
plt.legend()
plt.show()
#plt.savefig('hardanger_map.eps', format='eps')
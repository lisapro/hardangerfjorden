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

#map = Basemap(projection='stere', 
#              lat_0= 5, lon_0 =5)


map = Basemap(#width=150000,height=990000,
            resolution='l',projection='stere',\
            lat_0=70,lon_0=14,
            llcrnrlon = 5 ,llcrnrlat = 54 ,
            urcrnrlon = 27 ,urcrnrlat =70,ax = ax )


#axins = inset_axes(ax2,
#                        #width="30%", # width = 30% of parent_bbox
#                        height="30%", # height : 1 inch
#                        loc=9)

'''map2 = Basemap(projection='merc',
               llcrnrlat=59,urcrnrlat=63,
            llcrnrlon=5,urcrnrlon=10,
            resolution='i',ax = ax2)'''

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

#m1.drawparallels([60.1,60.15], labels = [0,1,1,1]) # draw parallels


#axins = zoomed_inset_axes(ax, 7, loc=1)
'''
axins = inset_axes(ax,
                        width="30%", # width = 30% of parent_bbox
                        height="30%", # height : 1 inch
                        loc=9)
x,y = map(5.5,60.0) # we define the corner 1
x2,y2 = map(6.5,61.5) # then corner 2

axins.set_xlim(x,x2) # and we apply the limits of the zoom plot to the inset axes
axins.set_ylim(y,y2) # idem

#assert loc in range(1, 11)  # called only internally

#axins.set_xlim(50, 6)
axins.set_ylim(60,65)

plt.xticks(visible=False)
plt.yticks(visible=False)

map2 = Basemap(llcrnrlon=5,llcrnrlat=60,
               urcrnrlon=6,urcrnrlat=61, 
               ax=axins,resolution='h')

map2.drawmapboundary(fill_color='#7777ff')
map2.fillcontinents(color='#ddaa66', lake_color='#7777ff', zorder=0)
map2.drawcoastlines()
map2.drawcountries()

#map2.scatter(x, y, s=cases/5., c='r', alpha=0.5)
mark_inset(ax, axins, loc1=1, loc2=3, fc="none", ec="0.5")

#mark_inset(ax, axins, loc1=10, loc2=15, fc="none", ec="0.5")
'''



#mark_inset(ax, ax2, loc1=2, loc2=3, fc="none", ec="0.5")

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

map2.scatter(lon_sed, lat_sed,latlon= True , color ='#880303',  label = "sediment station", 
          edgecolor = '#49361f', s= 55, zorder = 10)
map2.scatter(lon_sed2, lat_sed2,latlon= True , color ='#880303',
          edgecolor = '#49361f', s= 55, zorder = 10)


map2.scatter(lon7, lat7,latlon= True , color ='#ff7e37',
          edgecolor = '#995f3f', s= 55, zorder = 10)




map2.scatter(lon, lat,latlon= True , color ='#ff7e37',
          edgecolor = '#995f3f', s= 55, zorder = 10, label = "water column station")

map2.scatter(x_farm1,y_farm1,latlon = True, marker = "*", 
          color ='#f6e32c', edgecolor = '#b8894e',
          label = 'Fish farm',s = 85, zorder = 10 ,alpha = 1)

map2.scatter(x_farm2,y_farm2,latlon = True, marker = "*", color ='#f6e32c',
           s = 85, edgecolor = '#b8894e', zorder = 10 ,alpha = 1)
map2.scatter(x_farm3,y_farm3,latlon = True, marker = "*", color ='#f6e32c',
           s = 85, edgecolor = '#b8894e', zorder = 10 ,alpha = 1)
map2.scatter(x_farm4,y_farm4,latlon = True, marker = "*", color ='#f6e32c',
           s = 85, edgecolor = '#b8894e', zorder = 10 ,alpha = 1)
map2.scatter(x_farm5,y_farm5,latlon = True, marker = "*", color ='#f6e32c',
           s = 85, edgecolor = '#b8894e', zorder = 10 ,alpha = 1)



map.scatter(lon7, lat7,latlon= True , 
            color ='#ff7e37',
          edgecolor = '#995f3f', s= 55,
          zorder = 10, label = "water profiles")

txtsize = 10
st = 0
for xy in ((x1,y1), (x2,y2)) :
    ax2.annotate(name[st], xy,xytext=(7, -19), size= txtsize, 
                arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
                textcoords='offset points')
    st += 1
    
ax2.annotate('st3 ', (x3,y3), xytext=(-3, -19),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
            textcoords='offset points')
ax2.annotate('st4 ', (x4,y4), xytext=(1, -19),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')
ax2.annotate('st5 ', (x5,y5), xytext=(12, 0),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')
ax2.annotate('st199 ', (x_sed1,y_sed1), xytext=(12, -15),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')

ax2.annotate('st200 ', (x_sed2,y_sed2), xytext=(12, -25),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')

ax2.annotate('st6 ', (x6,y6), xytext=(12,-12),size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
             textcoords='offset points')   

 
ax2.annotate('st7', (x7,y7), xytext=(12,15),size= txtsize,
            arrowprops=dict(arrowstyle="-",connectionstyle="arc3"),
             textcoords='offset points')      
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
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes,inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import numpy as np
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(7,7.0), dpi=100)
gs = gridspec.GridSpec(1,1)
gs.update(left = 0.05,right = 0.93,bottom = 0.05, top = 0.95,hspace=0.07)
ax2 = fig.add_subplot(gs[0])
txtsize = 12

map2 = Basemap(projection='merc',llcrnrlat = 59.9,
             urcrnrlat=60.15,
            llcrnrlon=5.6,urcrnrlon=6.,
            resolution='i',ax = ax2)

x_patch,y_patch = map2(5.6,59.9)
x_patch2,y_patch2 = map2(5.6,60.2)

map2.drawmapboundary(fill_color='#cae2f7')
map2.fillcontinents(color='#bdad95')
map2.drawcoastlines(linewidth=0.5)

parallels2 = [59.9,60,60.1,60.2]
meridians2 = [5.4,5.6,5.8,6]

map2.drawparallels(parallels2, labels = [1,1,1,1], size = txtsize)
map2.drawmeridians(meridians2, labels = [1,1,1,1], size = txtsize)

lon = [5.861 , 5.7815, 5.769, 5.959, 5.928, 5.925] 
lat = [59.97478, 59.97821, 59.9757, 60.0471, 60.1239, 60.1212]
lon7 = 5.930716667
lat7 = 60.12692

def get_dist(lat1,lon1,lat2,lon2):
    import geopy.distance
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    return(geopy.distance.vincenty(coords_1, coords_2).m)

x_farm23 = 5.772001
y_farm23 = 59.977903

x_farm2 = 5.939457
y_farm2 = 60.106703

x_farm567 = 5.931092
y_farm567 = 60.126556

x_farm4 = 5.908662
y_farm4 = 60.121650 

x_farm1 = 5.669370  
y_farm1 = 59.954219

lon_sed199 = 5.684
lat_sed199 = 59.9522
lon_sed200 = 5.667
lat_sed200 = 59.95

dist199 = get_dist(y_farm1,x_farm1,lat_sed199,lon_sed199)
dist200 = get_dist(y_farm1,x_farm1,lat_sed200,lon_sed200)
print ('199',dist199)
print ('200',dist200)
#distances = [get_dist(lat[k],lon[k],) for k in [4,5,6]]

x_sed1,y_sed1 = map2(lon_sed199,lat_sed199)
x_sed2,y_sed2 = map2(lon_sed200,lat_sed200)

name_sed = ['199']
name_sed2 = ['200']



x1,y1 = map2(lon[0],lat[0])
x2,y2 = map2(lon[1],lat[1])
x3,y3 = map2(lon[2],lat[2])
x4,y4 = map2(lon[3],lat[3])
x5,y5 = map2(lon[4],lat[4])
x6,y6 = map2(lon[5],lat[5])
x7,y7 = map2(lon7,lat7)

starsize = 30
dot_size = 55
s_ecolor = '#235063' 
star_ecolor = '#f29f10' #'k' ##824c02

farmcolor = '#f6e32c'  
sed_color ='#880303'
wat_color = '#007cb2'

def plot_m(xf,yf,mapf,size,color,edgecolor,label = None, marker = None):

    mapf.scatter(xf,yf,latlon = True, marker = marker,
                color = color, s = size , edgecolor = edgecolor,
                label = label, zorder = 10 ,alpha = 0.7)

# 847.8884464264984 488.3460760562393
plot_m(lon_sed199, lat_sed199,map2,dot_size,'g',sed_color,str(dist199)+'m')
plot_m(lon_sed200, lat_sed200,map2,dot_size,'g',sed_color,str(dist200)+'m')
plot_m(x_farm1,y_farm1,map2,starsize,farmcolor,star_ecolor,'fish farm',"*") 


dist7 = get_dist(y_farm567,x_farm567,lat7,lon7)
print ('6',dist7)
plot_m(lon7, lat7,map2,dot_size,'y','y',str(dist7))

plot_m(x_farm567,y_farm567,map2,starsize,farmcolor,star_ecolor,None,"*")


for k in [4,5]:
    dist = get_dist(y_farm567,x_farm567,lat[k],lon[k]) 
    plot_m(lon[k], lat[k],map2,dot_size,'g',s_ecolor,None)
    print (k,dist)

plot_m(x_farm23,y_farm23,map2,starsize,farmcolor,star_ecolor,None,"*")  
for k in [0,1,2,3]:
    dist = get_dist(y_farm23,x_farm23,lat[k],lon[k]) 
    plot_m(lon[k], lat[k],map2,dot_size,'g',s_ecolor,None)
    print (k,dist)

plot_m(x_farm2,y_farm2,map2,starsize,farmcolor,star_ecolor,None,"*") 
plot_m(x_farm4,y_farm4,map2,starsize,farmcolor,star_ecolor,None,"*")


def to_annotate(title,coords,txt_coords,axis):  
    axis.annotate(title, coords, xytext = txt_coords,size= txtsize,
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),
            textcoords='offset points')

to_annotate('st1', (x1,y1),(7, -19),ax2) 
to_annotate('st2', (x2,y2),(9, -19),ax2) 
to_annotate('st3', (x3,y3),(-6, -19),ax2) 
to_annotate('st4', (x4,y4),(1, -19),ax2) 
to_annotate('st5', (x5,y5),(12, 0),ax2) 
to_annotate('st6', (x6,y6),(12, -12),ax2) 
to_annotate('st7: '+str(np.int(dist7))+'m', (x7,y7),(12, 15),ax2) 

to_annotate('sed 199', (x_sed1,y_sed1),(10, -15),ax2) 
to_annotate('sed 200', (x_sed2,y_sed2),(12, -25),ax2) 
      

plt.legend(prop={'size': txtsize})
plt.show()
#plt.savefig('Results/hardanger_map.png', format='png')
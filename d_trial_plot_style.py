# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:45:30 2021

@author: jcv
"""
#%%
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable

'''
# check where matplotlib is looking for fonts
font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
# if not recognizing, go to .matplotlib and clear font cache and restart
mpl.get_configdir()
'''
# in linux
#sudo fc-cache -fv
#rm -fr ~/.cache/matplotlib

'''
# check font name of ttf file and use in custom mplstyle
path = 'path_to_font_from_font_manager/Comic_Sans_MS.ttf'
prop = font_manager.FontProperties(fname=path)
mpl.rcParams['font.family'] = prop.get_name()
'''

# load in colormap
cm_data = np.flipud(np.loadtxt("Z:/Python/mpl_styles/oslo.txt"))
custom_map = LinearSegmentedColormap.from_list('custom', cm_data)

x1 = np.random.rand(10)
x2 = np.random.rand(20)
x3 = np.random.rand(30)

y1 = np.random.rand(10)
y2 = np.random.rand(20)
y3 = np.random.rand(30)

npts = 200
ngridx = 100
ngridy = 200
xi = np.linspace(-2, 2, ngridx)
yi = np.linspace(-2, 2, ngridy)
Xi, Yi = np.meshgrid(xi, yi)
Z = Xi*np.exp(-Xi**2 - Yi**2)


plt.style.use('Z:/Python/mpl_styles/stg_plot_style_1.mplstyle')

f = plt.figure()
ax = f.add_subplot(1,1,1)
ax.scatter(x1,y1, label = '1')
ax.scatter(x2,y2, label = '2')
ax.scatter(x3,y3, label = '3')
ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')
ax.grid()
ax.legend()




'''
f = plt.figure()
ax = f.add_subplot(1,1,1)
ax.tick_params(which = 'both', color = 'r')
sp = ax.contourf(Xi,Yi,Z, levels = 20, cmap = custom_map, alpha = 0.8)
ax.contour(Xi,Yi,Z, levels = 20, cmap=custom_map, linewidths = 0.5)
ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')
ax.grid()

divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='3%', pad=0.05)
f.colorbar(sp,cax=cax)
'''

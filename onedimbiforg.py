#!/usr/bin/env python 
'''
	plot one-dimensional bifurcation diagram
'''

import numpy as np
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_pdf import PdfPages

def func(a, x0):
	return a * x0 * (1.0 - x0)

params = {'text.usetex': True,
          'text.latex.preamble': r'\usepackage{newtxtext,newtxmath}',
          'legend.fontsize': 12, 'axes.labelsize': 12,
          'axes.titlesize': 12, 'xtick.labelsize' :12,
          'ytick.labelsize': 12, 'font.family': 'serif',
          'grid.color': 'k', 'grid.linestyle': ':',
          'grid.linewidth': 0.5,
         }
plt.rcParams.update(params)

idle = 100
mapmax = 300
amin = 2.5
amax = 4.0

base = 10.0
fig = plt.figure(figsize = (base, base/16*9))		# create a figure

ax = fig.add_subplot(111)					# create axes 

fig.subplots_adjust(bottom=0.1)

# PLOT options 
#plt.xticks(fontsize=10) 
#plt.yticks(fontsize=10) 

# AXES helpers
ax.set_xlabel(r'$a \longrightarrow$', fontsize=14)
ax.set_ylabel(r'$\varphi(k) \longrightarrow $', fontsize=14)
ax.set_xlim([amin, amax])
ax.set_ylim([0., 1.0])

resolution = 0.001

a_list = np.arange(amin, amax, resolution)
x_list = []
y_list = []

x0 = 0.2

for a in a_list:
	for i in range(idle):
		x = func(a, x0)
		xx = func(a, func(a, x0))
		x0 = x
	for i in range(mapmax):
		x = func(a, x0)
		if i < 10 or np.abs(x - x0) > 1e-4:
			x_list.append(a)
			y_list.append(x)
		x0 = x

print("computation complete")
print("computed {0} points".format(len(y_list)))

ax.plot(x_list, y_list, '.', markersize = 0.1, 
	markerfacecolor = 'black',
	markerfacecoloralt = 'black',
	markeredgecolor = 'black', fillstyle='full',
	color = "black", alpha = 0.2)

ax.grid(c='gainsboro', zorder=1)

plt.pause(0.001)	# flush current graphics

# Publish a PDF in the same time.
# Taking much time to flush data into a PDF if mapmax is large
#

pdf = PdfPages('snapshot.pdf')
pdf.savefig()
pdf.close()

plt.show() 	# keep appearance 


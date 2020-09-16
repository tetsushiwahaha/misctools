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

idle = 300
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

# resolution 0.0001 is fine
#

a_list = np.arange(amin, amax, 0.001)
x_list = []
y_list = []

# mapmax ranges up to 300
#

maxmap = 100
x0 = 0.2

for a in a_list:
	for i in range(idle):
		x = func(a, x0)
		x0 = x
	for i in range(maxmap):
		x = func(a, x0)
		x_list.append(a)
		y_list.append(x)
		x0 = x

print("computation complete")
print("computed  {0} points".format(len(y_list)))

ax.plot(x_list, y_list, 'o', markersize = 0.2, 
	color = "black", alpha = 0.2)

ax.grid(c='gainsboro', zorder=1)

# Publish a PDF in the same time.
#
pdf = PdfPages('snapshot.pdf')
pdf.savefig()
pdf.close()

plt.show()

#!/usr/bin/env python 
'''
	Plotting a function 
'''

import numpy as np
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_pdf import PdfPages

params = {'text.usetex': True,
          #'text.latex.preamble': r'\usepackage{newtxtext,newtxmath}',
          'legend.fontsize': 12, 'axes.labelsize': 12,
          'axes.titlesize': 12, 'xtick.labelsize' :12,
          'ytick.labelsize': 12, 'font.family': 'serif',
          'grid.color': 'k', 'grid.linestyle': ':',
          'grid.linewidth': 0.5,
         }
plt.rcParams.update(params)

x_list=[] 
y_list=[] 

fig = plt.figure(figsize = (5, 5/16*5))		# create a figure
ax = fig.add_subplot(111)					# create axes 
fig.subplots_adjust(bottom=0.3)

# PLOT options 
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10) 

# AXES helpers
ax.set_xlabel(r'$t \longrightarrow$', fontsize=12)
ax.set_ylabel(r'$\varphi(t) \longrightarrow $', fontsize=12)
ax.set_xlim([0, 3])
ax.set_ylim([-0.5, 3.0])

# CHANGE BELOW APPROPRIATELY
x_list = np.arange(0, 3, 0.01)	# x domain 
y_list = np.exp(-x_list + 1.0)	# y range defined by a fuction

### DATA PLOTTING 
ax.plot(x_list, y_list, 
	label = r'$\varphi(t)$', color = 'BLUE', linewidth = 0.8)
#ax.plot(x_list, y_list) 
#ax.plot(x_list, y_list, color='RED',linewidth=4.0) 
#ax.plot(x_list, y_list, marker='o') 
#ax.plot(x_list, y_list,'o') 
#ax.hlines([y1,y2], xmin, xmax, linestyles="dashed")  

ax.legend(loc='best') # legend
#ax.legend(loc=0)
ax.grid(c='gainsboro', zorder=2)
#ax.grid(True)

# Publish a PDF in the same time.
#
pdf = PdfPages('snapshot.pdf')
pdf.savefig()
pdf.close()

plt.show()

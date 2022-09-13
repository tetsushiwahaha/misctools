#!/usr/bin/env python 
'''
	Plotting data from a text file containing t, x(t), y(t)...
'''

import numpy as np
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_pdf import PdfPages

params = {'text.usetex': True,
          'text.latex.preamble': r'\usepackage{newtxtext,newtxmath}',
          'legend.fontsize': 12, 'axes.labelsize': 12,
          'axes.titlesize': 12, 'xtick.labelsize' :12,
          'ytick.labelsize': 12, 'font.family': 'serif',
          'grid.color': 'k', 'grid.linestyle': ':',
          'grid.linewidth': 0.5,
         }
# for finalization, uncomment below:
# plt.rcParams.update(params)

x_list=[] 
y_list=[] 
fd = open('data.txt','rt') 	# specify appropriate data file here
for line in fd:
    data = line[:-1].split(' ')	# split a line into columns
    x_list.append(float(data[0])) # choose an appropriate column 
    y_list.append(float(data[1]))

fig = plt.figure(figsize = (5, 5/16*5))		# create a figure
ax = fig.add_subplot(111)					# create axes 
fig.subplots_adjust(bottom=0.3, left=0.15)	# modify options if any

# PLOT options 
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10) 

# AXES helpers
ax.set_xlabel(r'$t \longrightarrow$', fontsize=12)
ax.set_ylabel(r'$\varphi(t) \longrightarrow $', fontsize=12)
ax.set_xlim([0, x_list[-1]])
ax.set_ylim([-0.5, 0.5])

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

#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
import matplotlib.colors
from matplotlib import cm
import sys

input_file = sys.argv[1]
results = np.loadtxt(input_file)
mask = results[:, 2] < 300 # Filter out really bad design outliers
not_outlier_data = results[mask, :]
norm = matplotlib.colors.Normalize(vmin=np.min(not_outlier_data[:,2]), vmax=np.max(not_outlier_data[:,2]))
cmap = cm.get_cmap('viridis', 256)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(not_outlier_data[:,0], not_outlier_data[:,1], not_outlier_data[:,2], c=cmap(norm(not_outlier_data[:,2])))
ax.set_xlabel('x position')
ax.set_ylabel('z position')
ax.set_zlabel('objective fcn.')
fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap))
fig.savefig(sys.argv[1]+'.png')

#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as lin
from matplotlib.collections import LineCollection
import matplotlib.colors
from matplotlib import cm

results = np.loadtxt('nonapod_inputs_grid_many/results')

base_points = np.loadtxt('nonapod_base_points')

fig = plt.figure()
ax = fig.add_subplot(111)

n = 100
result_array = np.empty((n, n))
result_array[:] = np.NaN

min_x = -20
max_x = 20
min_z = 0.0
max_z = 20.0
x_values = np.linspace(min_x, max_x, n)
z_values = np.linspace(min_z, max_z, n)

for i in range(results.shape[0]):
    xi = int(results[i, 0])
    zi = int(results[i, 1])
    objective = results[i, 2]
    x = x_values[xi]
    z = z_values[zi]

    # Check that this point is in the feasible space
    skip_this_one = False
    for j in range(base_points.shape[0]):
        member_length = lin.norm(base_points[j,:] - np.array([x, 0, z]))
        if member_length < 10 or member_length > 30:
            skip_this_one = True
            break
    if skip_this_one:
        continue

    result_array[zi, xi] = objective

norm = matplotlib.colors.Normalize(vmin=np.nanmin(result_array), vmax=min(300, np.nanmax(result_array)))
cmap = cm.get_cmap('viridis', 256)

ax.pcolormesh(x_values, z_values, result_array, norm=norm, cmap=cmap)
# ax.imshow(result_array, norm=norm, cmap=cmap)
ax.set_xlabel('x position')
ax.set_ylabel('z position')
ax.set_title('Constrained nonapod objective function')
fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap))
fig.savefig('constrained_result.png')

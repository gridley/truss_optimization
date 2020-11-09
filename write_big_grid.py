#!/usr/bin/env python3
from jinja2 import Template
import numpy as np

min_x = -20
max_x = 20
min_z = 0.0
max_z = 20.0

with open('nonapod_input.jinja') as template_file:
    templ = Template(template_file.read())

# Do the cases for grid sampling. Since 50 and 500 are not perfect squares,
# must use an approximate number.
x_values = np.linspace(min_x, max_x, 100)
z_values = np.linspace(min_z, max_z, 100)

fh = open('nonapod_inputs_grid_many/input_list', 'w')
for i, x in enumerate(x_values):
    for j, z in enumerate(z_values):
        with open('nonapod_inputs_grid_many/x_%i_z_%i'%(i,j), 'w') as result:
            result.write(templ.render(x=x, z=z))
        fh.write('%i %i %s\n' %(i, j, 'x_%i_z_%i'%(i,j)))
fh.close()

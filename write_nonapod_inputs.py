#!/usr/bin/env python3
from jinja2 import Template
from pyDOE2 import lhs # latin hypercube sample generation method
import random
import numpy as np

min_x = -20
max_x = 20
min_z = 0.1
max_z = 20.0

with open('nonapod_input.jinja') as template_file:
    templ = Template(template_file.read())

# Do the cases for grid sampling. Since 50 and 500 are not perfect squares,
# must use an approximate number.
x_values_50 = np.linspace(min_x, max_x, 7)
z_values_50 = np.linspace(min_z, max_z, 7)
x_values_500 = np.linspace(min_x, max_x, 22)
z_values_500 = np.linspace(min_z, max_z, 22)

fh = open('nonapod_inputs_grid_50/input_list', 'w')
for x in x_values_50:
    for z in z_values_50:
        with open('nonapod_inputs_grid_50/x_%.3f_z_%.3f'%(x,z), 'w') as result:
            result.write(templ.render(x=x, z=z))
        fh.write('%f %f %s\n' %(x, z, 'x_%.3f_z_%.3f'%(x,z)))
fh.close()

fh = open('nonapod_inputs_grid_500/input_list', 'w')
for x in x_values_500:
    for z in z_values_500:
        with open('nonapod_inputs_grid_500/x_%.3f_z_%.3f'%(x,z), 'w') as result:
            result.write(templ.render(x=x, z=z))
        fh.write('%f %f %s\n' %(x, z, 'x_%.3f_z_%.3f'%(x,z)))
fh.close()

# Do the cases for random sampling. Exactly 50 and 500 different points are used here.
fh = open('nonapod_inputs_random_50/input_list', 'w')
for i in range(50):
    x = random.uniform(min_x, max_x)
    z = random.uniform(min_z, max_z)
    with open('nonapod_inputs_random_50/x_%.3f_z_%.3f'%(x,z), 'w') as result:
        result.write(templ.render(x=x, z=z))
    fh.write('%f %f %s\n' %(x, z, 'x_%.3f_z_%.3f'%(x,z)))
fh.close()

fh = open('nonapod_inputs_random_500/input_list', 'w')
for i in range(500):
    x = random.uniform(min_x, max_x)
    z = random.uniform(min_z, max_z)
    with open('nonapod_inputs_random_500/x_%.3f_z_%.3f'%(x,z), 'w') as result:
        result.write(templ.render(x=x, z=z))
    fh.write('%f %f %s\n' %(x, z, 'x_%.3f_z_%.3f'%(x,z)))
fh.close()

# Lastly, the latin hypercube sampling approach:
sample_space_50 = lhs(2, samples=50)
sample_space_500 = lhs(2, samples=500)

# Transform those numbers in [0,1] to values in our space of interest
for arr in [sample_space_50, sample_space_500]:
    arr[:, 0] = arr[:,0] * (max_x - min_x) + min_x
    arr[:, 1] = arr[:,1] * (max_z - min_z) + min_z

fh = open('nonapod_inputs_latin_50/input_list', 'w')
for x, z in sample_space_50:
    with open('nonapod_inputs_latin_50/x_%.3f_z_%.3f'%(x,z), 'w') as result:
        result.write(templ.render(x=x, z=z))
    fh.write('%f %f %s\n' %(x, z, 'x_%.3f_z_%.3f'%(x,z)))
fh.close()

fh = open('nonapod_inputs_latin_500/input_list', 'w')
for x, z in sample_space_500:
    with open('nonapod_inputs_latin_500/x_%.3f_z_%.3f'%(x,z), 'w') as result:
        result.write(templ.render(x=x, z=z))
    fh.write('%f %f %s\n' %(x, z, 'x_%.3f_z_%.3f'%(x,z)))
fh.close()

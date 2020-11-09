#!/usr/bin/env python3
# Optimizes the location of the n-pod joint
import scipy.optimize
import os
import numpy as np
from jinja2 import Template

with open('nonapod_input.jinja') as fh:
    templ = Template(fh.read())

def calculate_objective(vec):

    # Write the input file
    with open('a', 'w') as fh:
        fh.write(templ.render(x=vec[0], z=vec[1]))

    # run solver
    os.system('./a.out a')

    # Extract objective function
    obj_value = 0.0
    with open('a_result') as fh:
        for line in fh:
            split_line = line.split()
            if len(split_line) == 7:
                x1, y1, z1, x2, y2, z2, tension = [float(value) for value in split_line]
                member_length = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
                obj_value += abs(tension) * member_length

    return obj_value

# start from x,z guess of whatever the np.array is below
result = scipy.optimize.minimize(calculate_objective, np.array([-8, 6]), method='Nelder-Mead')
print(result)

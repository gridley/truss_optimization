#!/usr/bin/env python3
# Optimizes the location of the n-pod joint
import scipy.optimize
import os
import numpy as np
import numpy.linalg as lin
from jinja2 import Template
import sys

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

# Create all of the constraints on member lengths.
constraints = list()
base_points = np.loadtxt('nonapod_base_points')

min_len = float(sys.argv[1])
constraints.append({'type': 'ineq', 'fun':  (lambda xz: lin.norm(base_points[0,:]-np.array([xz[0],0,xz[1]]))-min_len)})
constraints.append({'type': 'ineq', 'fun': (lambda xz: -lin.norm(base_points[0,:]-np.array([xz[0],0,xz[1]]))+30)})
constraints.append({'type': 'ineq', 'fun':  (lambda xz: lin.norm(base_points[1,:]-np.array([xz[0],0,xz[1]]))-min_len)})
constraints.append({'type': 'ineq', 'fun': (lambda xz: -lin.norm(base_points[1,:]-np.array([xz[0],0,xz[1]]))+30)})
constraints.append({'type': 'ineq', 'fun':  (lambda xz: lin.norm(base_points[2,:]-np.array([xz[0],0,xz[1]]))-min_len)})
constraints.append({'type': 'ineq', 'fun': (lambda xz: -lin.norm(base_points[2,:]-np.array([xz[0],0,xz[1]]))+30)})
constraints.append({'type': 'ineq', 'fun':  (lambda xz: lin.norm(base_points[3,:]-np.array([xz[0],0,xz[1]]))-min_len)})
constraints.append({'type': 'ineq', 'fun': (lambda xz: -lin.norm(base_points[3,:]-np.array([xz[0],0,xz[1]]))+30)})
constraints.append({'type': 'ineq', 'fun':  (lambda xz: lin.norm(base_points[4,:]-np.array([xz[0],0,xz[1]]))-min_len)})
constraints.append({'type': 'ineq', 'fun': (lambda xz: -lin.norm(base_points[4,:]-np.array([xz[0],0,xz[1]]))+30)})
constraints.append({'type': 'ineq', 'fun':  (lambda xz: lin.norm(base_points[5,:]-np.array([xz[0],0,xz[1]]))-min_len)})
constraints.append({'type': 'ineq', 'fun': (lambda xz: -lin.norm(base_points[5,:]-np.array([xz[0],0,xz[1]]))+30)})
constraints.append({'type': 'ineq', 'fun':  (lambda xz: lin.norm(base_points[6,:]-np.array([xz[0],0,xz[1]]))-min_len)})
constraints.append({'type': 'ineq', 'fun': (lambda xz: -lin.norm(base_points[6,:]-np.array([xz[0],0,xz[1]]))+30)})
constraints.append({'type': 'ineq', 'fun':  (lambda xz: lin.norm(base_points[7,:]-np.array([xz[0],0,xz[1]]))-min_len)})
constraints.append({'type': 'ineq', 'fun': (lambda xz: -lin.norm(base_points[7,:]-np.array([xz[0],0,xz[1]]))+30)})
constraints.append({'type': 'ineq', 'fun':  (lambda xz: lin.norm(base_points[8,:]-np.array([xz[0],0,xz[1]]))-min_len)})
constraints.append({'type': 'ineq', 'fun': (lambda xz: -lin.norm(base_points[8,:]-np.array([xz[0],0,xz[1]]))+30)})

# start from x,z guess of whatever the np.array is below
result = scipy.optimize.minimize(calculate_objective, np.array([12, 12]), constraints=constraints, method='COBYLA', tol=1e-8)
print(result.fun)
# Check constraints
# x = result.x
# for j in range(base_points.shape[0]):
#     print(lin.norm(base_points[j,:]-np.array([x[0],0,x[1]])  ))

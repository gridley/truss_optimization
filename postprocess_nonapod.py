#!/usr/bin/env python3
# Given a directory, computes the objective function for a family of trusses
import sys
import os

result_dir = sys.argv[1]

input_list = open(os.path.join(result_dir, 'input_list'))
result_list = open(os.path.join(result_dir, 'results'), 'w')
for line in input_list:
    x, z, input_name = line.split()
    result_file = open(os.path.join(result_dir, input_name + '_result'))

    # The result file contains pin reactions as well as member tensions.
    # The number of numbers on each line of the file tells you whether a tension
    # or pin reaction is listed.
    objective_fcn_value = 0.0
    for line in result_file:
        split_line = line.split()
        if len(split_line) == 7:
            x1, y1, z1, x2, y2, z2, tension = [float(value) for value in split_line]
            member_length = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
            objective_fcn_value += abs(tension) * member_length

    result_list.write("%s %s %f\n"%(x, z, objective_fcn_value))

    result_file.close()
input_list.close()
result_list.close()

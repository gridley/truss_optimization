#!/usr/bin/env python3
import random
from calculate_objective import calculate_objective

result_file = open('result_20', 'w')
for i in range(1, 21):
    these_params = [random.uniform(-3, 3),
            random.uniform(-3, 3),
            random.uniform(-3, 3),
            random.uniform(-5, 1),
            random.uniform(-5, 1),
            random.uniform(-5, 1)]
    obj_value = calculate_objective(these_params, i=i)
    these_params.append(obj_value)
    result_file.write(' '.join([str(s) for s in these_params]))
    result_file.write('\n')
result_file.close()

import scipy.optimize
import numpy as np
from calculate_objective import calculate_objective 

# initial_guess = np.array([1,-1,1,-2,-2,-2])
# result = scipy.optimize.minimize(calculate_objective, x0=initial_guess, method='Powell')

bounds = [(-3, 3), (-3, 3), (-3, 3), (-8, 1), (-8, 1), (-8, 1)]
result = scipy.optimize.differential_evolution(calculate_objective, bounds)
print(result)

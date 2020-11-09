# parallel coordinates plot
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('result_many')

plt.gca().get_xaxis().set_visible(False)

coords = np.array([0, 1, 2, 3, 4, 5])
d_min = np.min(data[:, 6])
d_max = np.max(data[:, 6])

def opacity(val):
    return np.exp(-(val/d_min)**2-1)

for i in range(data.shape[0]):
    plt.plot(coords, data[i,:6], alpha=opacity(data[i,6]), c='b')
plt.savefig('pcp.png')

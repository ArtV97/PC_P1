import numpy as np
from scipy import linalg

a = np.matrix([[4, 3, 0], [3, 4, -1], [0, -1, 4]])

b = np.array([24, 30, -24])

result = linalg.solve(a,b)
print("x = ", result)
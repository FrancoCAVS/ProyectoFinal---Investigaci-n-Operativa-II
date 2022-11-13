import nashpy as nash
import numpy as np




variable = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
rps = nash.Game(variable)
print(rps)
eqs = rps.support_enumeration()
print(list(eqs))
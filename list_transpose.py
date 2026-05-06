mat = [["1","2","3"],["4","5","6"],["7","8","9"]]
import numpy as np

mat_t = list(zip( *mat ))
print(mat_t)

np_mat = np.array(mat)
print(np_mat.T)
import time
import numpy as np
start_time = time.time()
N=10
b = np.matrix(np.random.rand(N,1))
A = np.matrix(np.random.rand(N,N))
x = np.linalg.solve(A, b)
time_elapsed = time.time() - start_time
print(time_elapsed)

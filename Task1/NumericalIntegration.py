import numpy as np

def numerical_integration(lower, upper, N):
    x = np.linspace(lower, upper, N+1)
    dx = (upper - lower) / N
    y = np.abs(np.sin(x))
    area = np.sum(y[:-1] * dx)  
    return area


Ns = [10, 100, 1000, 10000, 100000, 1000000]
results = [numerical_integration(0, np.pi, N) for N in Ns]
print(results)

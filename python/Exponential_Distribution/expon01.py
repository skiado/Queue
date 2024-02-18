import numpy as np
import matplotlib.pyplot as plt  #Για τη δημιουργία γραφικών παραστάσεων
import scipy as sp

rng = np.random.default_rng()

def exponential():
    U = rng.random()
    return -np.log(U)
 
MAX = 100000
a = []
l = float(input('l = '))
for i in range(MAX):
    a.append(l*exponential())
b = rng.exponential(l,MAX)
print('From numpy library ')
print('mean E[X] = ',np.mean(b))
print('From my function')
print('mean E[X] = ',np.mean(a))

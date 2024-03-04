import numpy as np
import matplotlib.pyplot as plt  # Για την περίπτωση που θέλουμε να δημιουργήσουμε γραφική παράσταση

rng = np.random.default_rng()

def exponential():
    U = rng.random()
    return -np.log(U)
 
MAX = 100000
a = []
l = float(input('λ = '))
for i in range(MAX):
    a.append((1/l)*exponential())
b = rng.exponential((1/l),MAX)
print('From Theory')
print('mean E[X] = ',1/l)
print('From numpy library ')
print('mean E[X] = ',np.mean(b))
print('From my function')
print('mean E[X] = ',np.mean(a))

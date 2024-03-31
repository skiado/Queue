import matplotlib.pyplot as plt

f = open('test01.txt','r')
lines = f.readlines()
f.close()
N_th = []
N_sim = []
ro = []
for i in range(1,len(lines)):
    l = lines[i].split()
    ro.append(float(l[0]))
    N_sim.append(float(l[1]))
    N_th.append(float(l[2]))
plt.plot(ro,N_th,color='blue',label='Theory')
plt.plot(ro,N_sim,color='red',label='simulation')
plt.legend()
plt.title('N theory - simulations')
plt.xlabel('ρ')
plt.ylabel('N')
plt.savefig('test01_python.png')
plt.show()

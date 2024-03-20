
sim = input('Experiment number = ')
with open('sim_data/'+sim+'queue_data.dat','r') as f:
    lines = f.readlines()
    
Nq = []
Nq_max = 0
Nqt_max = 0
for l in lines:
    a = l.split(',')
    Nq.append(int(a[1]))
    if int(a[1]) > Nq_max:
        Nq_max = int(a[1])
        Nqt_max = float(a[0])
print('Nq = ',Nq_max,'Nqt = ',Nqt_max)
print('mean Nq = ',sum(Nq)/len(lines))

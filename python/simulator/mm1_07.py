import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

rng = np.random.default_rng()

def exponential():
    U = rng.random()
    return -np.log(U)
    
def next_arrival(l,cur_t,t_arr):
    return cur_t + l * exponential()
    
def service_till(m,cur_t,t_ser):
    return cur_t + m * exponential()
    
def time_jump(t_arr,t_ser,cur_t):
    if t_arr <= t_ser:
        cur_time = t_arr
    elif cur_t <= t_ser :
        cur_t = t_ser
    return cur_t
    
def arrival(cur_t,queue,client,queue_data):
    queue.append(client)
    queue_data.append([cur_t,len(queue)])
    client_data.append([cur_t,0,0])
    
def service(cur_t,t_ser,queue,client_data,queue_data):
    client = queue.pop(0)
    queue_data.append([cur_t,len(queue)])
    client_data[client][1] = cur_t
    client_data[client][2] = t_ser
    
queue = []
queue_data = []
client = 0         #next client to come
client_data = []   #client_data 0 = arrival time, 1 = departure time
l = float(input('mean arriving time interval = '))
m = float(input('mean time interval to service a client = '))
t_max = float(input('Simulation untill = '))
t_ser = 0          #time when service will be IDLE
t_arr = 0         #time of next arrival
cur_t = 0   

t_arr = next_arrival(l,cur_t,t_arr)
cur_t = t_arr
arrival(cur_t,queue,client,queue_data)
client += 1
t_arr = next_arrival(l,cur_t,t_arr)
t_ser = service_till(m,cur_t,t_ser)
service(cur_t,t_ser,queue,client_data,queue_data)
while cur_t < t_max:
    cur_t = time_jump (t_arr,t_ser,cur_t)
    if cur_t == t_arr:
        arrival(cur_t,queue,client,queue_data)
        client += 1
        t_arr = next_arrival(l,cur_t,t_arr)
    elif cur_t >= t_ser and len(queue) > 0:
        t_ser = service_till(m,cur_t,t_ser)
        service(cur_t,t_ser,queue,client_data,queue_data)
    else:
        cur_t = t_arr
        
sim = input('Simulation number = ')
f = open('sim_data/'+sim+'client_data.dat','w')
for i in client_data:
    f.write(str(i[0])+','+str(i[1])+','+str(i[2])+'\n')
f.close()
f = open('sim_data/'+sim+'queue_data.dat','w')
for i in queue_data:
    f.write(str(i[0])+','+str(i[1])+'\n')
f.close()

T = 0
Tq = 0
Ts = 0
s_clients = 0          #number of serviced clients
f = open('sim_data/'+sim+'client_data.dat','r')
lines = f.readlines()
f.close()
for line in lines:
    line = line.split(',')
    if float(line[2]) > 0:
       T += float(line[2]) - float(line[0]) 
       Tq += float(line[1]) - float(line[0]) 
       Ts += float(line[2]) - float(line[1])
       s_clients += 1
T = T / s_clients
Tq = Tq / s_clients
Ts = Ts / s_clients

f = open('sim_data/'+sim+'sim_data.dat','w')
f.write('l = '+str(l)+', m = '+str(m)+', t_max = '+str(t_max)+'\n')
f.write('λ = '+str(1/l)+', μ = '+str(1/m)+'\n')
f.write('Queue Theory \n')
ro_t = m/l
f.write('T = '+str((m*l)/(l-m))+', Tq = '+str((m/l)/((l-m)/(m*l)))+', Ts = '+str(m)+'\n'+'N = '+ str(ro_t/(1-ro_t)))
f.write('\nSimulation \n')
f.write('T = '+str(T)+', Tq = '+str(Tq)+', Ts = '+str(Ts)+'\n')
f.write('Number of serviced clients = '+str(s_clients))

f.close()



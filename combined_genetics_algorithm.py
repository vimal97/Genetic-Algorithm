import random
import time
import math

#Cuckoo Algorithm

print("\n\n#Cuckoo Algorithm******************\n\n")

start = time.time()

p_start_main = 0.6
p_end_main = 1.2
f_start_main = 0.20
f_end_main = 0.40
p_rand = []
f_rand = []
p_optimum = '0.81'
f_optimum = 0.38
p_junk_values = []
f_junk_values = []
p_start = 0
p_end = 0
f_start = 0
f_end = 0
opt_p = 0
opt_f = 0

def find_optimum_value(mode,optimum,start,end):
    k = 0
    i = 0
    if mode == 0:
        while i < 6:
            k = "{0:.2f}".format(random.uniform(start,end))
            if not k in p_junk_values:
                p_rand.append(k)
                p_junk_values.append(k)
                print('Rand : ',p_rand)
                print('Junk : ',p_junk_values)
                i = i + 1
                print('i : ',i)
            if(len(p_rand) == 10):
                break
        if(optimum in p_rand):
            print("Optimum criteria reached for pressure with value : ",optimum)

        else:
            find_optimum_value(0,optimum,start,end)
    if mode == 1:
        while i < 6:
            k = "{0:.2f}".format(random.uniform(start,end))
            if not k in f_junk_values:
                f_rand.append(k)
                f_junk_values.append(k)
                print('Rand : ',f_rand)
                print('Junk : ',f_junk_values)
                i = i + 1
                print('i : ',i)
            if(len(f_rand) == 10):
                break

        if(str(optimum) in f_rand):
            print("Optimum criteria reached for flowrate with value : ",optimum)

        else:
            find_optimum_value(1,optimum,start,end)

if((p_optimum >= '0.60') and (p_optimum <= '0.69')):
    p_start = 0.60
    p_end = 0.69
elif((p_optimum >= '0.70') and (p_optimum <= '0.79')):
    p_start = 0.70
    p_end = 0.79
elif((p_optimum >= '0.80') and (p_optimum <= '0.89')):
    p_start = 0.80
    p_end = 0.89
elif((p_optimum >= '0.90') and (p_optimum <= '0.99')):
    p_start = 0.90
    p_end = 0.99
elif((p_optimum >= '1.00') and (p_optimum <= '1.09')):
    p_start = 1.00
    p_end = 1.09
elif((p_optimum >= '1.10') and (p_optimum <= '1.20')):
    p_start = 1.10
    p_end = 1.20
else:
    print("Optimum value out of limit for 1")
find_optimum_value(0,p_optimum,p_start,p_end)

if((f_optimum >= 0.20) and (f_optimum <= 0.29)):
    f_start = 0.20
    f_end = 0.29
elif((f_optimum >= 0.30) and (f_optimum <= 0.40)):
    f_start = 0.30
    f_end = 0.40
else:
    print("Optimum value out of limit for 2 ")
find_optimum_value(1,f_optimum,f_start,f_end)
print("Voltage : ",float(p_optimum)*10.375 + float(f_optimum)*45.448)
print("Current : ",float(float(p_optimum)*10.375 + float(f_optimum)*45.448)*0.20 + 15)
print("Iteration for pressure : ",p_junk_values.index(str(p_optimum)),"Iteration for flowrate : ",f_junk_values.index(str(f_optimum)))
t = (time.time())-start
print("Execution Time for cuckoo algorithm: ",t)

times = []
times.append(t)

print("\n\n#End of Cuckoo Algorithm******************\n\n")

#end of Cuckoo Algorithm

#Particle swarm algorithm

print("\n\n#Particle Swarm Algorithm******************\n\n")

start = time.time()

n = 10 #int(input("Enter the number of Particles : "))
f = 0.38 #float(input("Enter the optimized flowrate value : "))
p = 0.81 #float(input("Enter the optimized pressure value : "))
f_max = 0.4
f_min = 0.2
p_max = 1.2
p_min = 0.6
p_f = []
p_p = []
i = 0

while(i <= n):
    f_value = float("{0:.2f}".format(random.uniform(f_min,f_max)))
    p_value = float("{0:.2f}".format(random.uniform(p_min,p_max)))
    p_f.append(f_value)
    p_p.append(p_value)
    i = i + 1

opt_p = min(p_p, key=lambda x:abs(x-p))
opt_f = min(p_f, key=lambda x:abs(x-f))

print("Optimized pressure value found to be : ",opt_p)
print("Optimized flowrate value found to be : ",opt_f)

print("Voltage : ",float(opt_p)*10.375 + float(opt_f)*45.448)
print("Current : ",float(float(opt_p)*10.375 + float(opt_f)*45.448)*0.20 + 15)

print("Pressure Iteration : ",p_p.index(opt_p))
print("Flowrate Iteration : ",p_f.index(opt_f))

t = (time.time())-start
print("Execution Time : ",t)
times.append(t)

print("\n\n#End of Particle Swarm Algorithm******************\n\n")

#End of Particle swarm

#firefly Algorithm

print("\n\n#Firefly Algorithm******************\n\n")

start = time.time()

pressure = []
flowrate = []
p_min = 0.6
p_max = 1.2
f_min = 0.2
f_max = 0.4
v = 0
optimized = 25

def optimize():
    i = 0
    flag = False
    while i < 10:
        value = "{0:.2f}".format(random.uniform(p_min,p_max))
        if not value in pressure:
            pressure.append(value)
            i = i + 1
    i = 0
    while i < 10:
        value = "{0:.2f}".format(random.uniform(f_min,f_max))
        if not value in flowrate:
            flowrate.append(value)
            i = i + 1
    opt1 = 0
    opt2 = 1
    opt_arr = []
    for i in pressure:
        for j in flowrate:
            v = float(i)*10.375 + float(j)*45.448
            if((math.floor(v) == optimized) or (math.ceil(v) == optimized)):
                opt_arr.append(v)
                opt2 = min(opt_arr, key=lambda x:abs(x-25))
                if opt1 != opt2:
                    opt1 = opt2
                    p = i
                    f = j
                flag = True
                break
    if flag == True:
        i = opt1 * 0.20 + 15
        print("Optimum found with closest voltage value ",opt1,"V and current ",i,"A using pressure ",p," and flowrate ",f," Pressure iteration : ",pressure.index(p)," Flowrate Iteration : ",flowrate.index(f))
        # print(opt_arr)
    else:
        print(pressure)
        print(flowrate)
        optimize()
optimize()

t = (time.time())-start
times.append(t)
print("Execution Time : ",t)

print("\n\n#Firefly Algorithm******************\n\n")

#end of firefly Algorithm

algos = ["Cuckoo Algorithm","Particle swarm Algorithm","Firefly Algorithm"]

print("******************************")

print("Efficient Algorithm on this run : ",algos[times.index(min(times))])

print("******************************")

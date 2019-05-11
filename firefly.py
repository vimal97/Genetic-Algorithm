import random
import math

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
        print("Optimum found with closest voltage value ",opt1,"V and current ",i,"A using pressure ",p," and flowrate ",f)
        # print(opt_arr)
    else:
        print(pressure)
        print(flowrate)
        optimize()
optimize()
import random

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
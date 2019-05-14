import random

n = int(input("Enter the number of Particles : "))
f = float(input("Enter the optimized flowrate value : "))
p = float(input("Enter the optimized pressure value : "))
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
import math
a = input()
a = int(a)
Uoc = []
Value = 0
for i in range(1,a,1):
    if (a % i == 0):
        Uoc.append(i)
for item in Uoc:
    Value += item
if (Value == a):
    print ("PerfectNumber")
else:
    print ("UnPerfectNumber")
import math
F0 = 0
F1 = 1
Fn = 0
n = input()
n = int(n)
if (n == 0): print(F0)
elif (n == 1): print(F1)
else:
    for i in range(1, n, 1):
        Fn = F1 + F0
        F0 = F1
        F1 = Fn
        # if (Fn == n)
    print(Fn)
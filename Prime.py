import math
n = input()
n = int(n)
if(n <= 1): 
    print("Khong phai so nguyen to")
else:
    IsPrime = True
    for i in range(2, math.sqrt(n) + 1, 1):
        if(n % i == 0): IsPrime = False
    print(f"{n} SNT" if IsPrime else f"{n} Khong phai SNT")
    # if (IsPrime): print(f"{n} la so nguyen to")
    # else: print(f"{n} khong la so nguyen to")
import math
a = float(input())
b = float(input())
c = float(input())
if (a == 0):
    if (b == 0):
        if (c == 0):
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        print(f"Có một nghiệm {-b/a}")
else:
    Delta = math.pow(b, 2) - 4*a*c
    if (Delta < 0): print("Vô nghiệm")
    elif (Delta == 0): print(f"Nghiệm kép là {-b/ (2*a)}")
    else:
        print(f"Phương trình có 2 nghiệm là {(-b - math.sqrt(Delta) / (2*a))} và {(-b + math.sqrt(Delta) / (2*a))}")


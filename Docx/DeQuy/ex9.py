def HaNoiTower(n, start, end, temp):
    if(n == 1): return f"Chuyển từ {start} sang {end}"
    else: 
        HaNoiTower(n-1, start, temp, end)
        HaNoiTower(1, start, end, temp)
        HaNoiTower(n-1, temp, end, start)
n = int(input("Nhập n: "))
a = "Cột a"
b = "Cột b"
c = "Cột c"
HaNoiTower(n,a,c,b)
def main():
    a = [0, 0]
    b = [0, 0]
    c = [0, 0]

    for i in range(2):
        print(f"Nhập hệ số cho phương trình {i + 1} (ax + by = c):")
        a[i] = float(input(f"Nhập a{i + 1}: "))
        b[i] = float(input(f"Nhập b{i + 1}: "))
        c[i] = float(input(f"Nhập c{i + 1}: "))

    D = a[0] * b[1] - a[1] * b[0]
    Dx = c[0] * b[1] - c[1] * b[0]
    Dy = a[0] * c[1] - a[1] * c[0]

    if D == 0:
        if Dx == 0 and Dy == 0:
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        x = Dx / D
        y = Dy / D
        print(f"Nghiệm của hệ phương trình là: x = {x}, y = {y}")

if __name__ == "__main__":
    main()

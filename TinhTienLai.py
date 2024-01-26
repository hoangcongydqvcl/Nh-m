A = float(input("Nhập số tiền gốc (A): "))
r = float(input("Nhập lãi suất hàng năm (r%): "))
n = int(input("Nhập số tháng (n): "))
thang_can_tinh = int(input("Nhập tháng cần tính lãi: "))
def tinh_lai_kep(A, r, n, thang_can_tinh):
    a = r / 100.0
    for thang in range(1, n + 1):
        if thang == thang_can_tinh:
            lai_tai_thang = A * (1 + a / n)**(thang / n) - A
            return lai_tai_thang
SoTien=tinh_lai_kep(A, r,n, thang_can_tinh)
print(f"Số tiền lãi tại tháng {thang_can_tinh} là: {SoTien}")
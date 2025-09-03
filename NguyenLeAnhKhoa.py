# Bài 1
def BangCuuChuong():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")

BangCuuChuong()

# Bài 2
def Palindrome(s):
    if s == s[::-1]:
        print("Day la chuoi Palindrome")
    else:
        print("Day la chuoi khong phai Palindrome")

Chuoi = str(input("Nhap chuoi: "))
Palindrome(Chuoi)

#Bài 3
def SoNguyenTo(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True


num = int(input("Nhap so nguyen: "))
if SoNguyenTo(num):
    print("Day la so nguyen to")
else:
    print("Day la so khong phai nguyen to")

#Bài 4
def KyTuXuatHienNhieuNhat(s):
    max_count = 0

    for i in range(len(s)):
        count = s.count(s[i])
        if count > max_count:
            max_count = count

    print(f"Ky tu xuat hien nhieu nhat: {max_count} lan la :")
    for i in range(len(s)):
        is_duplicate = False
        for j in range(i):
            if s[i] == s[j]:
                is_duplicate = True
                break
        if s.count(s[i]) == max_count and not is_duplicate:
            print(s[i])

chuoi = str(input("Nhap chuoi: "))
KyTuXuatHienNhieuNhat(chuoi)

#Bài 5
def SoHoanHao(n):
    if n < 1:
        return False
    
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

num = int(input("Nhap so nguyen: "))
if SoHoanHao(num):
    print("Day la so hoan hao")
else:
    print("Day la so khong phai hoan hao")

#Bài 6
def DemSNT(a,b):
    count = 0
    for num in range(a, b + 1):
        if SoNguyenTo(num):
            count += 1
    return count

a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
KQ = DemSNT(a,b)
print(f"So luong so nguyen to trong khoang [{a}, {b}] la: {KQ}")

#Bài 7
def DaoNguocSoNguyen(n):
    DaoNguoc = 0
    while n > 0 :
        TachSo = n % 10
        DaoNguoc = DaoNguoc *10 + TachSo
        n = int(n / 10)
    return DaoNguoc

SoNguyen = int(input("Nhap so nguyen : "))
Result = DaoNguocSoNguyen(SoNguyen)
print(f"So {SoNguyen} sau khi duoc dao : {Result}")

#Bài 8
def TinhThue (ThuNhap,SoNguoi) :
    ThuNhapChiuThue = ThuNhap - (11000000 + 4400000*SoNguoiPhuThuoc)
    Thue = 0
    if ThuNhapChiuThue <= 0:
        Thue = 0
    elif ThuNhapChiuThue <= 5000000:
        Thue = ThuNhapChiuThue * 0.05
    elif ThuNhapChiuThue <= 10000000:
        Thue = 5000000 * 0.05 + (ThuNhapChiuThue - 5000000) * 0.1
    elif ThuNhapChiuThue <= 18000000:
        Thue = 5000000 * 0.05 + 5000000 * 0.1 + (ThuNhapChiuThue - 10000000) * 0.15
    elif ThuNhapChiuThue <= 32000000:
        Thue = 5000000 * 0.05 + 5000000 * 0.1 + 8000000 * 0.15 + (ThuNhapChiuThue - 18000000) * 0.2
    elif ThuNhapChiuThue <= 52000000:
        Thue = 5000000 * 0.05 + 5000000 * 0.1 + 8000000 * 0.15 + 14000000 * 0.2 + (ThuNhapChiuThue - 32000000) * 0.25
    elif ThuNhapChiuThue <= 80000000:
        Thue = 5000000 * 0.05 + 5000000 * 0.1 + 8000000 * 0.15 + 14000000 * 0.2 + 20000000 * 0.25 + (ThuNhapChiuThue - 52000000) * 0.3
    else:
        Thue = 5000000 * 0.05 + 5000000 * 0.1 + 8000000 * 0.15 + 14000000 * 0.2 + 20000000 * 0.25 + 28000000 * 0.3 + (ThuNhapChiuThue - 80000000) * 0.35

    return Thue

ThuNhap = int(input("Nhap tong thu nhap cua ban : "))
SoNguoiPhuThuoc = int(input("Nhap so nguoi phu thuoc : "))
print(f"Thue thu nhap ca nhan cua ban la : {TinhThue(ThuNhap,SoNguoiPhuThuoc)}")
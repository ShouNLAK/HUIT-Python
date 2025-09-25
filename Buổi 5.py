# Đây là bài Phân số
import math
class PhanSo:
    def __init__(self,tu,mau) :
        if mau == 0:
            # Tương đương throw new Exception trong C#
            raise Exception("ERROR : Đã có phân số cho mẫu bằng 0")
        else :
            self.tu = tu
            self.mau = mau
            self.rutgon()
            
    def rutgon(self):
        ucln = math.gcd(self.tu,self.mau)
        self.tu //= ucln
        self.mau //= ucln
        if (self.mau < 0):
            self.tu *= -1
            self.mau *= -1
        return self
    
    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
    def GiaTriThuc(self):
        return self.tu / self.mau
    
    def __add__(self,other) :
        Tu = self.tu * other.mau + self.mau * other.tu
        Mau = self.mau * other.mau
        return PhanSo(Tu,Mau)
    
    def __sub__(self,other) :
        Tu = self.tu * other.mau - self.mau * other.tu
        Mau = self.mau * other.mau
        return PhanSo(Tu,Mau)
    
    def __mul__(self,other) :
        Tu = self.tu * other.tu
        Mau = self.mau * other.mau
        return PhanSo(Tu,Mau)
    
    def __truediv__(self,other) :
        if (other.tu == 0):
            return "CAN NOT DIVIDED BY ZERO"
        else:
            Tu = self.tu * other.mau
            Mau = self.mau * other.tu
            return PhanSo(Tu,Mau)
        
    def nhap():
        User_input_Tu = int(input("Hãy nhập tử cho phân số : "))
        User_input_Mau = int(input("Hãy nhập mẫu cho phân số : "))
        return PhanSo(User_input_Tu,User_input_Mau)
    
    def xuat(self):
        return f"Phân số : {self.tu}/{self.mau}"
    
    def nghich_dao(self):
        if (self.tu == 0):
            return "unable"
        else:
            temp = self.tu
            self.tu = self.mau
            self.mau = temp
            return self
            
    def la_phan_so_toi_gian(self) :
        if (self.tu == (self.rutgon()).tu) :
            return True
        return False
    
    def la_phan_so_duong(self) :
        if (self.tu * self.mau > 0):
            return True
        return False
    
    def __eq__(self,other):
        return True if (self.GiaTriThuc() == other.GiaTriThuc()) else False
    
    def __lt__(self,other) :
        return True if (self.GiaTriThuc() < other.GiaTriThuc()) else False
    
    def __gt__(self,other) :
        return True if (self.GiaTriThuc() > other.GiaTriThuc()) else False
    
    def doi_dau(self):
        self.tu *= -1
        self.mau *= -1
        return self
        
    def Gia_Tri_Thap_Phan(self):
        return self.GiaTriThuc() - int(self.GiaTriThuc())
    
    def La_So_Nguyen(self):
        return True if (self.GiaTriThuc() == int(self.GiaTriThuc())) else False
    
    def Doi_Sang_So_Thap_Phan(self,Fix):
        return (int)(self.Gia_Tri_Thap_Phan() * 10**Fix) 
    

if __name__ == "__main__" :
    a = PhanSo.nhap()
    b = PhanSo.nhap()
    
    a.xuat()
    b.xuat()
    
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    
    print(f"Nghịch đảo của Phân số {a} = ",a.nghich_dao())
    print(f"Phân số {a} đã tối giản hay chưa : ",a.la_phan_so_toi_gian())
    print(f"Phân số {a} là số dương ? : ",a.la_phan_so_duong())
    
    print(f"{a} = {b} : {a == b}")
    print(f"{a} < {b} : {a < b}")
    print(f"{a} > {b} : {a > b}")
    
    print(f"Phân số A ban đầu {a} - Sau khi đổi dấu {a.doi_dau()}")
    print(f"Giá trị thập phân của phân số {b} = {b.Gia_Tri_Thap_Phan()}")
    print(f"{b} có phải là số nguyên ? : {b.La_So_Nguyen()}")
    print(f"Lấy 3 số cuối của số thập phân của {b} = {b.Doi_Sang_So_Thap_Phan(3)}")


# Đây là bài Tọa độ - Điểm
import math

class Diem:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def hien_thi(self):
        return f"Tọa độ : ({self.x},{self.y})"

    def Khoang_cach(self,other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    
    def Doi_Xung_Truc_Tung(self):
        self.x *= -1
        return self
    
    def Doi_Xung_Truc_Hoanh(self):
        self.y *= -1
        return self
    
    def Doi_Xung_Ca_Hai_Truc(self):
        self.x *= -1
        self.y *= -1
        return self
    
    def Thuoc_Truc_Nao(self):
        if (self.x == 0 and self.y == 0):
            return "Cả hai trục (trục hoành và trục tung)"
        elif (self.x == 0):
            return "Trục hoành"
        elif (self.y == 0):
            return "Trục tung"
        return "Không thuộc trục nào cả"
    
    def nhap():
        X = float(input("Nhập tọa độ x của điểm : "))
        Y = float(input("Nhập tọa độ y của điểm : "))
        return Diem(X,Y)
    
    def xuat(self) :
        self.hien_thi()
        
    def Goc_Voi_Ox(self):
        return round(math.fabs(math.degrees(math.atan(self.y /self.x))),2)
    
    def Goc_Voi_Oy(self):
        return round(math.fabs(math.degrees(math.atan(self.x /self.y))),2)
    
A = Diem(2,3)
B = Diem(5,7)

print(f"Khoảng cách giữa 2 điểm A và B la {A.Khoang_cach(B)}")
print(f"Đối xứng trục tung đối với điểm {A.xuat()} là {A.Doi_Xung_Truc_Tung()}")
print(f"Đối xứng trục hoành đối với điểm {B.xuat()} là {B.Doi_Xung_Truc_Hoanh()}")
print(f"Đối xứng cả hai trục đối với điểm {B.xuat()} là {B.Doi_Xung_Ca_Hai_Truc()}")
print(f"Điểm A thuộc trục : {A.Thuoc_Truc_Nao()}")

print(f"A : {A.hien_thi()}")
print(f"B : {B.hien_thi()}")

print(f"Góc của OAx (OA và Ox) là : {A.Goc_Voi_Ox()}")
print(f"Góc của OAy (OA và Oy) là : {A.Goc_Voi_Oy()}")

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
    
    def cong(self,other) :
        Tu = self.tu * other.mau + self.mau * other.tu
        Mau = self.mau * other.mau
        return PhanSo(Tu,Mau)
    
    def tru(self,other) :
        Tu = self.tu * other.mau - self.mau * other.tu
        Mau = self.mau * other.mau
        return PhanSo(Tu,Mau)
    
    def nhan(self,other) :
        Tu = self.tu * other.tu
        Mau = self.mau * other.mau
        return PhanSo(Tu,Mau)
    
    def chia(self,other) :
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
    
    
a = PhanSo.nhap()
b = PhanSo.nhap()

a.xuat()
b.xuat()

print(f"{a} + {b} = {a.cong(b)}")
print(f"{a} - {b} = {a.tru(b)}")
print(f"{a} * {b} = {a.nhan(b)}")
print(f"{a} / {b} = {a.chia(b)}")

print(f"Nghịch đảo của Phân số {a} = ",a.nghich_dao())
print(f"Phân số {a} đã tối giản hay chưa : ",a.la_phan_so_toi_gian())
print(f"Phân số {a} là số dương ? : ",a.la_phan_so_duong())

print(f"{a} = {b} : {a == b}")
print(f"{a} < {b} : {a < b}")
print(f"{a} > {b} : {a > b}")

print(f"Phân số A ban đầu {a} - Sau khi đổi dấu {a.doi_dau()}")
print(f"Giá trị thập phân của phân số {b} = {b.Gia_Tri_Thap_Phan()}")
print(f"{b} có phải là số nguyên ? : {b.La_So_Nguyen()}")
print(f"Lấy 3 số cuối của số thập phân của {b} = {b.Doi_Sang_So_Thap_Phan(4)}")

# Sử dụng file .txt
class SinhVien():
    def __init__ (self, ma, ten,diem):
        self.Ma = ma
        self.Ten = ten
        self.Diem = float(diem)
        
    def Xuat(self):
        print(f"{self.Ma} | {self.Ten} | {self.Diem}")
        
    def HSG(self):
        if self.Diem >= 8.5:
            return True
        return False
    
    def HSK(self) :
        if self.Diem >= 7 and self.Diem < 8.5:
            return True
        return False
    
    def HSTB(self) :
        if self.Diem >= 5 and self.Diem < 7:
            return True
        return False
    
    def HocLuc (self):
        if self.HSG():
            return "Gioi"
        elif self.HSK():
            return "Kha"
        elif self.HSTB():
            return "Trung binh"
        return "Yeu"
    
class DSSV():
    def __init__(self):
        self.DS = []
        
    def Nhap(self,tenFile):
        with open(tenFile,'r') as doc:
            soLuong = int(doc.readline())
            for i in range(soLuong):
                dataSV = doc.readline().strip().split(",")
                SV = SinhVien(dataSV[0],dataSV[1],dataSV[2])
                self.DS.append(SV)
    
    def Xuat(self):
        print("Ma SV | Ten SV | Diem")
        for SV in self.DS:
            SV.Xuat()
            
    def Ghi_File(self,tenFile = "DSSV.txt"):
        with open(tenFile,'w') as doc:
            doc.write(f"{len(self.DS)}\n")
            for SV in self.DS:
                doc.write(f"{SV.Ma},{SV.Ten},{SV.Diem}\n")

    def KT_HSG(self):
        KQ = DSSV()
        for SV in self.DS:
            if SV.HSG():
                KQ.DS.append(SV)
        return KQ

    def Search_By_Ma(self,Ma):
        for SV in self.DS:
            if SV.Ma.lower() == Ma.lower():
                return SV;
        return None
    
    def Search_By_CName(self,Ten):
        KQ = DSSV()
        for SV in self.DS:
            Tach = SV.Ten.split()
            if Ten in Tach:
                KQ.DS.append(SV)
        return KQ if len(KQ.DS) > 0 else None
    
    def ThongKe_HocLuc(self):
        TK = {}
        for SV in self.DS:
            if SV.HocLuc() in TK :
                TK[SV.HocLuc()] += 1
            else :
                TK[SV.HocLuc()] = 1
        return TK
    
    def Sort_GDDiem(self):
        self.DS.sort(key = lambda SV : SV.Diem * -1)
        return self
    
    
def Menu():
    DanhSach = DSSV()
    while (True) :
        print("\n1. Nhap File Danh sach sinh vien")
        print("2. Xuat Danh sach sinh vien")
        print("3. Xuat File Danh sach sinh vien gioi")
        print("4. Tim sinh vien theo ma")
        print("5. Tim theo ten sinh vien gan dung")
        print("6. Thong ke loai hoc luc")
        print("7. Sap xep danh sach theo diem giam dan")
        print("---------------------------------")
        print("0. Thoat chuong trinh")
    
        chon = int(input("\n >> Nhap chuong trinh thuc thi : "))
        if chon == 1:
            Input = "SinhVien.txt"
            DanhSach.Nhap(Input)
        elif chon == 2:
            DanhSach.Xuat()
        elif chon == 3:
            DanhSach.KT_HSG().Ghi_File()
        elif chon == 4:
            Ma = input("Nhap ma sinh vien can tim : ")
            if (DanhSach.Search_By_Ma(Ma) == None):
                print("Khong tim thay")
            else:
                DanhSach.Search_By_Ma(Ma).Xuat()
        elif chon == 5:
            Ten = input("Nhap 1 chu trong ten sinh vien can tim : ")
            if (DanhSach.Search_By_CName(Ten) == None):
                print("Khong tim thay")
            else:
                DanhSach.Search_By_CName(Ten).Xuat()
        elif chon == 6:
            ThongKe = DanhSach.ThongKe_HocLuc()
            for HL,SL in ThongKe.items():
                print(f"{HL} : {SL}")
        elif chon == 7:
            DanhSach.Sort_GDDiem().Xuat()
        elif chon == 0:
            break
        else:
            print("Nhap sai chuong trinh - Vui long nhap lai")


Menu()

#Sử dụng file .json - Thuộc file BTVN Tuần 8

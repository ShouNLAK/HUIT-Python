import datetime
import math

BangQuyDoi={
    'Mèo Anh lông ngắn' : {'Cắt lông' : 'Tỉa nhẹ : 3 - 4 tháng / lần', 'Thức ăn' : 'Hạt khô + Pate' , 'Tiếng kêu' : 'Meo meo'},
    'Mèo Anh lông dài' : {'Cắt lông' : 'Cắt lông : 2 tháng / lần','Thức ăn' : 'Hạt khô + Pate', 'Tiếng kêu' : 'Meo meo'},
    'Mèo ta' : {'Cắt lông' : 'Không cần cắt, chỉ cần chải lông định ','Thức ăn' : 'Cá / Thịt nấu','Tiếng kêu' : 'Mèo méo'},
    'Mèo Xiêm' : {'Cắt lông' : 'Không cần cắt, chỉ cần chải lông định ','Thức ăn' : 'Pate / Thịt mềm','Tiếng kêu' : 'Mèo mèo'},
    'Mèo Ba Tư' : {'Cắt lông' : 'Cắt lông : 2 tháng / lần','Thức ăn' : 'Hạt mềm / Cá hồi / Thịt gà','Tiếng kêu' : 'Meo mèo'},
}




class ThuCung:
    def __init__(self,Ma,Ten,Sinh,Can,Giong,Mau):
        self.Ma = Ma
        self.Ten = Ten
        Tach = Sinh.split("/")
        if (len(Tach) == 1):
            self.NamSinh = Sinh
        elif (len(Tach) == 2):
            self.ThangSinh = Tach[0]
            self.NamSinh = Tach[1]
        self.CanNang = Can
        if Giong == "1":
            self.GiongMeo = "Mèo Anh lông ngắn"
        elif Giong == "2":
            self.GiongMeo = "Mèo Anh lông dài"
        elif Giong == "3":
            self.GiongMeo = "Mèo ta"
        elif Giong == "4":
            self.GiongMeo = "Mèo Xiêm"
        elif Giong == "5":
            self.GiongMeo = "Mèo Ba Tư"
        else:
            self.GiongMeo = Giong
        self.MauLong = Mau
        
    def __str__(self):
        return f"{self.Ma} | {self.Ten} | {self.NamSinh} | {self.CanNang} | {self.GiongMeo} | {self.MauLong}"
    
    def tinh_Tuoi(self):
        return datetime.datetime.now().year - (int)(self.NamSinh)
    def tinh_TuanTuoi(self):
        return (datetime.datetime.now().month - int(self.ThangSinh))*4 if (datetime.datetime.now().month - int(self.ThangSinh)) > 0 else (52 - datetime.datetime.now().month - int(self.ThangSinh))*4
    
    def hien_thi_thong_tin(self):
        print("Mã mèo : ",self.MaMeo)
        print("Tên mèo : ",self.Ten)
        print(f"Ngày sinh : Tháng {self.ThangSinh} Năm {self.NamSinh}  ({self.tinh_Tuoi()} tuổi)")
        print("Giống mèo : ",self.GiongMeo)
        print("Màu lông : ",self.MauLong)
        print("Tiếng kêu : ",self.Keu())

    def hien_thi_chi_tiet(self) :
        print(f"{self.Ma} | {self.Ten} | {self.ThangSinh}/{self.NamSinh} | {self.CanNang} | {self.GiongMeo} | {self.MauLong} | {self.Keu()} |{self.Lich_Cat_Long()} | {self.Lich_Tiem_Chung()}")
        
    def Keu(self):
        for Giong,value in BangQuyDoi.items():
            if self.GiongMeo == Giong :
                for Search, Detail in value.items():
                    if Search == 'Tiếng kêu':
                        return Detail
    
    def An(self):
        for Giong,value in BangQuyDoi.items():
            if self.GiongMeo == Giong :
                for Search, Detail in value.items():
                    if Search == 'Thức Ăn':
                        return Detail
                    
    def Lich_Cat_Long(self):
        for Giong,value in BangQuyDoi.items():
            if self.GiongMeo == Giong :
                for Search, Detail in value.items():
                    if Search == 'Cắt lông':
                        return Detail
        
    def Lich_Tiem_Chung(self):
        if (self.tinh_Tuoi() >= 1):
            return "Hằng năm : Nhắc lại vaccine tổng hợp + Phòng dại"
        else :
            if self.tinh_TuanTuoi() >= 12 and self.tinh_TuanTuoi() <= 14:
                return "Tiêm mũi phòng dại"
            elif self.tinh_TuanTuoi() >= 8 and self.tinh_TuanTuoi() <= 11:
                return "Tiêm mũi tổng hợp lần 2"
            elif self.tinh_TuanTuoi() >= 6 and self.tinh_TuanTuoi() <= 7:
                return "Tiêm mũi tổng hợp lần 1"
            else : 
                return "Chưa đến lịch tiêm phòng"
            
def Nhap_DSTC():
    DSThuCung = []
    n = int(input("Nhập số lượng thú cưng cần quản lý: "))
    for i in range(n):
        print(f"Nhập thông tin thú cưng thứ {i+1} : ")
        Ma = input("Nhập mã thú cưng : ")
        Ten = input("Nhập tên thú cưng : ")
        TS = input("Nhập tháng sinh và năm sinh của thú cưng (mm/yyyy) : ")
        Can = input("Nhập cân nặng của thú cưng : ")
        Giong = input("Nhập loại giống của thú cưng (1 - Mèo Anh lông ngắn | 2 - Mèo Anh lông dài | 3 - Mèo ta | 4 - Mèo Xiêm | 5 - Mèo Ba Tư | (Nhập khác là tên của giống mèo đã nhập) : )")
        Mau = input("Nhập màu lông của thú cưng :")
        Meo = ThuCung(Ma,Ten,TS,Can,Giong,Mau)
        DSThuCung.append(Meo)
    return DSThuCung

def Search_DSTC_by_Ma(DSTC,Ma) :
    for ThuCung in DSTC :
        if ThuCung.Ma == Ma :
            return ThuCung
    return "Not Found"

def Xuat_Detail_DSTC(DSTC) : 
    for ThuCung in DSTC :
        print(ThuCung)

def Oldest_Pet(DSTC) :
    max = 0;
    for ThuCung in DSTC :
        if ThuCung.tinh_TuanTuoi() > max :
            max = ThuCung.tinh_TuanTuoi()
            best = ThuCung
    return best


def menu(DSTC):
    print("-----Quản Lý Thú Cưng-----")
    print("1. Nhập danh sách thông tin thú cưng")
    print("2. Hiển thị danh sách thú cưng")
    print("3. Tìm kiếm thông tin thú cưng theo mã")
    print("4. Hiển thị chi tiết thông tin thú cưng (Tất cả)")
    print("5. Xuất ra con mèo già nhất trong danh sách")
    print("6. Thoát")
    print("--------------------------")
    choice = int(input("Chọn chức năng (1-6): "))
    if(choice == 1):
        DSTC = Nhap_DSTC()
    if (choice == 2) :
        Xuat_Detail_DSTC(DSTC)
    if (choice == 3):
        Searching = input("Nhập mã thú cưng mà bạn cần tìm : ")
        print(f"Kết quả : {Search_DSTC_by_Ma(DSTC,Searching)}")
    if (choice == 4) :
        for ThuCung in DSTC :
            ThuCung.hien_thi_chi_tiet()
    if (choice == 5) :
        KQ = Oldest_Pet(DSTC)
        KQ.hien_thi_chi_tiet()
    #if (choice == 6) : 
    menu(DSTC)

DSTC = []
menu(DSTC)    for ThuCung in DSTC :
        print(ThuCung)

def Oldest_Pet(DSTC) :
    max = 0;
    for ThuCung in DSTC :
        if ThuCung.tinh_TuanTuoi() > max :
            max = ThuCung.tinh_TuanTuoi()
            best = ThuCung
    return best


def menu(DSTC):
    print("-----Quản Lý Thú Cưng-----")
    print("1. Nhập danh sách thông tin thú cưng")
    print("2. Hiển thị danh sách thú cưng")
    print("3. Tìm kiếm thông tin thú cưng theo mã")
    print("4. Hiển thị chi tiết thông tin thú cưng (Tất cả)")
    print("5. Xuất ra con mèo già nhất trong danh sách")
    print("6. Thoát")
    print("--------------------------")
    choice = int(input("Chọn chức năng (1-6): "))
    if(choice == 1):
        DSTC = Nhap_DSTC()
    if (choice == 2) :
        Xuat_Detail_DSTC(DSTC)
    if (choice == 3):
        Searching = input("Nhập mã thú cưng mà bạn cần tìm : ")
        print(f"Kết quả : {Search_DSTC_by_Ma(DSTC,Searching)}")
    if (choice == 4) :
        for ThuCung in DSTC :
            ThuCung.hien_thi_chi_tiet()
    if (choice == 5) :
        KQ = Oldest_Pet(DSTC)
        KQ.hien_thi_chi_tiet()
    #if (choice == 6) : 
    menu(DSTC)

DSTC = []
menu(DSTC)

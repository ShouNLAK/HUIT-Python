import datetime
import math

BangQuyDoi={
    'Mèo Anh lông ngắn' : {'Cắt lông' : 'Tỉa nhẹ : 3 - 4 tháng / lần', 'Thức ăn' : 'Hạt khô + Pate' , 'tiếng kêu' : 'Meo Meo'},
    'Mèo Anh lông dài' : {'Cắt lông' : 'Cắt lông : 2 tháng / lần','Thức ăn' : 'Hạt khô + Pate', 'tiếng kêu' : 'Meo Meo'},
    'Mèo ta' : {'Cắt lông' : 'Không cần cắt, chỉ cần chải lông định ','Thức ăn' : 'Cá / Thịt nấu','tiếng kêu' : 'Meo Meo'},
    'Mèo Xiêm' : {'Cắt lông' : 'Không cần cắt, chỉ cần chải lông định ','Thức ăn' : 'Pate / Thịt mềm','tiếng kêu' : 'Meo Meo'},
    'Mèo Ba Tư' : {'Cắt lông' : 'Cắt lông : 2 tháng / lần','Thức ăn' : 'Hạt mềm / Cá hồi / Thịt gà','tiếng kêu' : 'Meo Meo'},
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
        if Giong == 1:
            self.GiongMeo = "Mèo Anh lông ngắn"
        elif Giong == 2:
            self.GiongMeo = "Mèo Anh lông dài"
        elif Giong == 3:
            self.GiongMeo = "Mèo ta"
        elif Giong == 4:
            self.GiongMeo = "Mèo Xiêm"
        elif Giong == 5:
            self.GiongMeo = "Mèo Ba Tư"
        else:
            self.GiongMeo = Giong
        self.MauLong = Mau
        
    def __str__(self):
        return f"{self.Ma} | {self.Ten} | {self.NgaySinh} | {self.CanNang} | {self.GiongMeo} | {self.MauLong}"
    
    def tinh_Tuoi(self):
        return datetime.datetime.now().Year() - self.NamSinh
    
    def hien_thi_thong_tin(self):
        print("Mã mèo : ",self.MaMeo)
        print("Tên mèo : ",self.Ten)
        print(f"Ngày sinh : Tháng {self.ThangSinh} Năm {self.NamSinh}  ({self.tinh_Tuoi()} tuổi)")
        print("Giống mèo : ",self.GiongMeo)
        print("Màu lông : ",self.MauLong)
        
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
        if self.tinh_Tuoi() >= 12 and self.tinh_Tuoi() <= 14:
            return "Tiêm mũi phòng dại"
        elif self.tinh_Tuoi() >= 8 and self.tinh_Tuoi() <= 11:
            return "Tiêm mũi tổng hợp lần 2"
        elif self.tinh_Tuoi() >= 6 and self.tinh_Tuoi() <= 7:
            return "Tiêm mũi tổng hợp lần 1"
        

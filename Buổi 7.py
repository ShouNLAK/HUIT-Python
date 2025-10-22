# Đây là bài 1. Động vật
class DongVat:
    def __init__(self, ten):
        self.Ten = ten
        
    def TiengKeu(self):
        return f"Động vật đang kêu"
    
class Cho(DongVat):
    def TiengKeu(self):
        return f"Đông vật : {self.Ten} đang sủa gâu gâu"
    
class Meo(DongVat):
    def TiengKeu(self):
        return f"Đông vật : {self.Ten} đang meo meo"
    
class Kien(DongVat):
    pass

cho = Cho("Mực")
meo = Meo("Na")
kien = Kien("Kiến lửa")

print(cho.TiengKeu())
print(meo.TiengKeu())
print(kien.TiengKeu())

# Đây là bài 2. Hình học
import math

class Hinh():
    def __init__(self,ten):
        self.Ten = ten
        
    def chu_vi(self):
        return 0
    def dien_tich(self):
        return 0
    def thong_tin(self):
        return f"Hình {self.Ten}"
    
class Hinh_Tron(Hinh):
    def __init__(self,ten,bk):
        super().__init__(ten)
        self.banKinh = bk
        
    def chu_vi(self):
        return 2*math.pi*self.banKinh
    def dien_tich(self):
        return math.pi*math.pow(self.banKinh,2)
    def thong_tin(self):
        return f"Hình tròn : {self.Ten} | Bán kính : {self.banKinh} | Chu vi : {self.chu_vi()} | Diện tích : {self.dien_tich()}"
    
class Hinh_Chu_Nhat(Hinh):
    def __init__ (self, ten, cd, cr) :
        super().__init__(ten)
        self.chieuDai = cd
        self.chieuRong = cr
        
    def chu_vi(self):
        return 2*(self.chieuDai + self.chieuRong)
    def dien_tich(self):
        return self.chieuDai * self.chieuRong
    
    def thong_tin(self):
        return f"Hình chữ nhật : {self.Ten} | Chiều dài : {self.chieuDai} | Chiều rộng : {self.chieuRong} | Chu vi : {self.chu_vi()} | Diện tích : {self.dien_tich()}"

    
class Hinh_Vuong(Hinh):
    def __init__(self,ten,canh):
        super().__init__(ten)
        self.Canh = canh
        
    def chu_vi(self):
        return 4* self.Canh
    def dien_tich(self):
        return math.pow(self.Canh,2)
    
    def thong_tin(self):
        return f"Hình vuông : {self.Ten} | Cạnh : {self.Canh} | Chu vi : {self.chu_vi()} | Diện tích : {self.dien_tich()}"

class Hinh_Tam_Giac(Hinh):
    def __init__(self,ten,a,b,c):
        super().__init__(ten)
        self.Canh1 = a
        self.Canh2 = b
        self.Canh3 = c
        
    def chu_vi(self):
        return self.Canh1 + self.Canh2 + self.Canh3
    def dien_tich(self):
        p = self.chu_vi / 2
        return math.sqrt(p*(p-self.Canh1)*(p-self.Canh2)*(p-self.Canh3))
    
    def thong_tin(self):
        return f"Hình tam giác : {self.Ten} | Độ dài 3 cạnh : {self.Canh1} - {self.Canh2} - {self.Canh3} | Chu vi : {self.chu_vi()} | Diện tích : {self.dien_tich()}"

DS = []
n = int(input("Nhập số lượng hình mà bạn muốn : "))
for i in range(n):
    print(f"--- Nhập thông tin hình số {i+1} ---")
    ten = input("Nhập tên hình mà bạn muốn gọi : ")
    loaiHinh = int(input("Nhập loại hình (1-Hình tròn | 2-Hình chữ nhật | 3-Hình vuong | 4-Hình tam giác | Khác-Hình) : "))
    if loaiHinh == 1:
        while (True) :    
            banKinh = float(input("Nhập độ dài bán kính :"))
            if banKinh <= 0 :
                print("bán kính phải lớn hơn 0")
                continue
            else :
                break
        DS.append(Hinh_Tron(ten,banKinh))
    elif loaiHinh == 2:
        while (True) :
            cd = float(input("Nhập chiều dài :"))
            cr = float(input("Nhập chiều rộng :"))
            if (cd * cr == 0 or cd < cr) :
                print("Chiều dài > Chiều rộng > 0")
                continue
            else:
                break
        DS.append(Hinh_Chu_Nhat(ten, cd, cr))
    elif loaiHinh == 3:
        while (True) :    
            canh = float(input("Nhập độ dài cạnh :"))
            if canh <= 0 :
                print("Cạnh phải lớn hơn 0")
                continue
            else :
                break;
        DS.append(Hinh_Vuong(ten, canh))
    elif loaiHinh == 4:
        while (True) :
            c1 = float(input("Nhập cạnh thứ nhất :"))
            c2 = float(input("Nhập cạnh thứ hai :"))
            c3 = float(input("Nhập cạnh thứ ba :"))
            if (c1 + c2 < c3 or c1 + c3 < c2 or c2 + c3 < c1):
                print("Không hợp lệ , để tạo hình tam giác phải 2 cạnh có tổng lớn hơn cạnh còn lại")
                continue
            else:
                break
        DS.append(Hinh_Tam_Giac(ten, c1, c2, c3))
    else:
        DS.append(Hinh(ten))
        
for H in DS:
    print(H.thong_tin())

## Đây là bài 3. Phương tiện
class PhuongTien():
    def __init__(self,speed):
        self.TocDo = speed
    def di_chuyen(self):
        return "Phương tiện đang di chuyển với tốc độ {self.TocDo} (km/h)"
    def dung_lai(self):
        return "Phương tiện đã dừng lại"
    def thong_tin(self) :
        return f"Tốc độ phương tiện : {self.TocDo} (km/h)"
    
class Oto(PhuongTien) :
    def __init__(self,speed,ac=False):
        super().__init__(speed)
        self.DieuHoa = ac
    def di_chuyen(self):
        return f"Ô tô đang di chuyển với tốc độ {self.TocDo} (km/h)"
    def bat_dieu_hoa(self):
        self.DieuHoa = True
    def tat_dieu_hoa(self) :
        self.DieuHoa = False
    def thong_tin(self) :
        return f"Tốc độ Ô tô : {self.TocDo} (km/h) | Điều hòa : {self.DieuHoa}"
        
class XeMay(PhuongTien) :
    def __init__(self,speed,light=False):
        super().__init__(speed)
        self.DenXe = light
    def di_chuyen(self):
        return f"Xe máy đang di chuyển với tốc độ {self.TocDo} (km/h)"
    def bat_den(self):
        self.DenXe = True
    def tat_den(self) :
        self.DenXe= False
    def thong_tin(self) :
        return f"Tốc độ Xe máy : {self.TocDo} (km/h) | Đèn xe : {self.DenXe}"
        
class XeTai(PhuongTien) :
    def __init__(self,speed,ac=False):
        super().__init__(speed)
        self.DieuHoa = ac
    def di_chuyen(self):
        return f"Xe tải đang di chuyển với tốc độ {self.TocDo} (km/h)"
    def bat_dieu_hoa(self):
        self.DieuHoa = True
    def tat_dieu_hoa(self) :
        self.DieuHoa = False
    def thong_tin(self) :
        return f"Tốc độ Xe tải : {self.TocDo} (km/h) | Điều hòa : {self.DieuHoa}"
        
def Nhap_DS():
    DS = []
    n = int(input("Nhập số lượng phương tiện mà bạn muốn : "))
    for i in range(n):
        print(f"--- Nhập thông tin phương tiện số {i+1} ---")
        speed = input("Nhập tốc độ phương tiện : ")
        loaiHinh = int(input("Nhập loại hình (1 - Xe oto | 2 - Xe máy | 3 - Xe tải | Khác - Phương tiện) : "))
        if loaiHinh == 1:
            dieuHoa= input("Nhập trạng thái điều hòa ( 0 - Tắt | 1 - Mở ) : ")
            if dieuHoa == "0":
                dieuHoa = False
            elif dieuHoa == "1":
                dieuHoa = True
            else :
                raise Exception("Điều hòa phải là 0 hoặc 1") 
            DS.append(Oto(speed,dieuHoa))
        elif loaiHinh == 2:
            denXe = input("Nhập trạng thái đèn xe ( 0 - Tắt | 1 - Mở ) : ")
            if denXe == "0":
                denXe = False
            elif denXe == "1":
                denXe = True
            else :
                raise Exception("Đèn xe phải là 0 hoặc 1")  
            DS.append(XeMay(speed,denXe))
        elif loaiHinh == 3:
            dieuHoa= input("Nhập trạng thái điều hòa ( 0 - Tắt | 1 - Mở ) : ")
            if dieuHoa == "0":
                dieuHoa = False
            elif dieuHoa == "1":
                dieuHoa = True
            else :
                raise Exception("Điều hòa phải là 0 hoặc 1")  
            DS.append(XeTai(speed,dieuHoa))
        else:
            DS.append(PhuongTien(speed))
    return DS

def Xuat_DS(DS):
    for xe in DS :
        print(xe.thong_tin())
        
def Bat_AC(DS) :
    for xe in DS :
        if hasattr(xe, 'DieuHoa') :
            xe.bat_dieu_hoa()
    return DS
            
def Dem_Xe_Khong_AC(DS) :
    sum = 0
    for xe in DS :
        if not hasattr(xe, 'DieuHoa') :
            sum += 1
    return sum

def Dem_Xe_HienTai_AC_True(DS) :
    sum = 0
    for xe in DS :
        if hasattr(xe, 'DieuHoa') :
            if xe.DieuHoa == True:
                sum += 1
    return sum

def Tat_AC_XeTai(DS) :
    for xe in DS:
        if isinstance(xe, XeTai) :
            xe.tat_dieu_hoa()
    return DS

def Thay_Doi_TrangThai_Den_XeMay(DS) :
    for xe in DS:
        if isinstance(xe, XeMay) :
            if xe.DenXe == True :
                xe.tat_den()
            else:
                xe.bat_den()
    return DS
            
def Menu(DS):
    while (True) :
        print("\n--- QUẢN LÝ PHƯƠNG TIỆN GIAO THÔNG ---")
        print("1. Nhập danh sách phương tiện")
        print("2. Hiển thị trạng thái phương tiện")
        print("3. Bật điều hòa cho xe có điều hòa")
        print("4. Đếm số lượng xe không có điều hòa")
        print("5. Đếm số lượng xe đang bật điều hòa")
        print("6. Tắt điều hòa cho tất cả xe tải")
        print("7. Bật/Tắt đèn xe máy")
        print("8. Thoát chương trình")
        print("-----------------------------------------")
        n = int(input("Nhập chương trình bạn muốn thực thi : "))
        if n == 1:
            DS = Nhap_DS()
        elif n == 2:
            Xuat_DS(DS)
        elif n == 3:
            Xuat_DS(Bat_AC(DS))
        elif n == 4:
            print(f"Có tổng cộng {Dem_Xe_Khong_AC(DS)} xe không có điều hòa")
        elif n == 5:
            print(f"Có tổng cộng {Dem_Xe_HienTai_AC_True(DS)} xe đang mở điều hòa")
        elif n == 6:
            Xuat_DS(Tat_AC_XeTai(DS))
        elif n == 7:
            Xuat_DS(Thay_Doi_TrangThai_Den_XeMay(DS))
        elif n == 8 :
            break

DS = []
Menu(DS)

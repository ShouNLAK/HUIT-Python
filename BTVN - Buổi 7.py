class Sach:
    def __init__(self,ten,nxb,namxb,sotrang,giavon,giabia,giam):
        self.Ten = ten
        self.NXB = nxb
        self.NamXB = namxb
        self.SoTrang = sotrang
        self.GiaVon = giavon
        self.GiaBia = giabia
        if giam >= 0 and giam <= 1:
            self.Giam = giam
        else:
            self.Giam = 0

    def gia_ban_cuoi(self):
        return self.GiaBia * (1-self.Giam)
    
    def thong_tin_chung(self):
        return f'Ten: {self.Ten}, NXB: {self.NXB}, NamXB: {self.NamXB}, SoTrang: {self.SoTrang}, GiaVon: {self.GiaVon}, GiaBia: {self.GiaBia}, Giam: {self.Giam}, GiaBanCuoi: {self.gia_ban_cuoi()}'
    
    def thong_tin(self):
        return self.thong_tin_chung()
    
class SGK(Sach):
    def __init__(self,ten,nxb,namxb,sotrang,giavon,giabia,lop,giam = 0.05):
        super().__init__(ten,nxb,namxb,sotrang,giavon,giabia,giam)
        if lop >= 1 and lop <= 12:
            self.KhoiLop = lop
        else:
            self.KhoiLop = 1

    def thong_tin(self):
        return f'{self.thong_tin_chung()}, KhoiLop: {self.KhoiLop}'
    
class TieuThuyet(Sach):
    def __init__(self,ten,nxb,namxb,sotrang,giavon,giabia,theloai,giam = 0.1):
        super().__init__(ten,nxb,namxb,sotrang,giavon,giabia,giam)
        self.TheLoai = theloai

    def thong_tin(self):
        return f'{self.thong_tin_chung()}, TheLoai: {self.TheLoai}'
    
class TapChi(Sach):
    def __init__(self,ten,nxb,namxb,sotrang,giavon,giabia,dinhky,giam = 0):
        super().__init__(ten,nxb,namxb,sotrang,giavon,giabia,giam)
        self.DinhKy = dinhky

    def thong_tin(self):
        return f'{self.thong_tin_chung()}, DinhKy: {self.DinhKy}'
    
def Nhap_DS_Sach():
    ds_sach = []
    n = int(input("Nhap so luong sach: "))
    for i in range(n):
        print(f"Nhap thong tin sach thu {i+1}:")
        loai = input("Loai sach (1 - SGK, 2 - TieuThuyet, 3 - TapChi): ")
        ten = input("Nhap Ten sach: ")
        nxb = input("Nhap Nha xuat ban: ")
        namxb = int(input("Nhap Nam xuat ban: "))
        sotrang = int(input("Nhap So trang: "))
        giavon = float(input("Nhap Gia von: "))
        giabia = float(input("Nhap Gia bia: "))
        if loai == "1":
            lop = int(input("Nhap Khoi lop: "))
            sach = SGK(ten,nxb,namxb,sotrang,giavon,giabia,lop)
        elif loai == "2":
            theloai = input("Nhap The loai: ")
            sach = TieuThuyet(ten,nxb,namxb,sotrang,giavon,giabia,theloai)
        elif loai == "3":
            dinhky = input("Nhap Dinh ky: ")
            sach = TapChi(ten,nxb,namxb,sotrang,giavon,giabia,dinhky)
        else:
            print("Loai sach khong hop le. Bo qua.")
            continue
        ds_sach.append(sach)
    return ds_sach

def Hien_DS_Sach(ds_sach):
    for sach in ds_sach:
        print(sach.thong_tin())

def Tong_Gia_Von(ds_sach):
    return sum(sach.GiaVon for sach in ds_sach)

def Tong_Gia_Ban(ds_sach):
    return sum(sach.gia_ban_cuoi() for sach in ds_sach)

def Tong_Loi_Nhuan(ds_sach):
    return Tong_Gia_Ban(ds_sach) - Tong_Gia_Von(ds_sach)

def ThongKe_TheoLoaiSach(ds_sach):
    loai_count ={}
    for sach in ds_sach:
        if isinstance(sach, SGK):
            loai = "SGK"
        elif isinstance(sach, TieuThuyet):
            loai = "TieuThuyet"
        elif isinstance(sach, TapChi):
            loai = "TapChi"
        if loai in loai_count:
            loai_count[loai] += 1
        else:
            loai_count[loai] = 1
    return loai_count

def ThongKe_TheoTongVon(ds_sach):
    tongvon_count = {}
    for sach in ds_sach:
        if sach.GiaVon in tongvon_count:
            tongvon_count[sach.GiaVon] += 1
        else:
            tongvon_count[sach.GiaVon] = 1
    return tongvon_count

def Loc_SGK_TheoKhoi(ds_sach, khoi):
    return [(sach.Ten,sach.gia_ban_cuoi()) for sach in ds_sach if (isinstance(sach, SGK) and sach.KhoiLop == khoi)]

def Search_By_NXB(ds_sach, nxb):
    found = []
    for sach in ds_sach:
        if sach.NXB.lower() == nxb.lower():
            found.append(sach.thong_tin())
    return found

def Search_By_TimeRange(ds_sach):
    found = []
    start_year = int(input("Nhap nam bat dau: "))
    end_year = int(input("Nhap nam ket thuc: "))
    if start_year > end_year:
        temp = start_year
        start_year = end_year
        end_year = temp
    for sach in ds_sach:
        if start_year <= sach.NamXB <= end_year:
            found.append(sach.thong_tin())
    return found

def Sort_By_GiaBanTD(ds_sach):
    return sorted(ds_sach, key=lambda sach: sach.gia_ban_cuoi())

def Sort_By_GiaBanGD(ds_sach):
    return sorted(ds_sach, key=lambda sach: sach.gia_ban_cuoi()*-1)

def Max_GiaBan(ds_sach):
    found = []
    max_gia = max(sach.gia_ban_cuoi() for sach in ds_sach)
    for sach in ds_sach:
        if sach.gia_ban_cuoi() == max_gia:
            found.append(sach.thong_tin())
    return found

def Min_GiaBan(ds_sach):
    min_gia = min(sach.gia_ban_cuoi() for sach in ds_sach)
    found = []
    for sach in ds_sach:
        if sach.gia_ban_cuoi() == min_gia:
            found.append(sach.thong_tin())
    return found

def Menu(ds_sach):
    while(True):
        print("1. Nhap danh sach sach")
        print("2. Hien thi danh sach sach")
        print("3. Tong gia von")
        print("4. Tong gia ban")
        print("5. Tong loi nhuan")
        print("6. Thong ke theo the loai")
        print("7. Thong ke theo tong von")
        print("8. Loc SGK theo khoi")
        print("9. Tim kiem theo NXB")
        print("10. Tim kiem theo khoang thoi gian")
        print("11. Sap xep theo gia ban tang dan")
        print("12. Sap xep theo gia ban giam dan")
        print("13. Sach co gia ban cao nhat")
        print("14. Sach co gia ban thap nhat")
        print("0. Thoat")
        choice = input("Chon chuc nang: ")
        if choice == "1":
            ds_sach = Nhap_DS_Sach()
        elif choice == "2":
            Hien_DS_Sach(ds_sach)
        elif choice == "3":
            print("Tong gia von:", Tong_Gia_Von(ds_sach))
        elif choice == "4":
            print("Tong gia ban:", Tong_Gia_Ban(ds_sach))
        elif choice == "5":
            print("Tong loi nhuan:", Tong_Loi_Nhuan(ds_sach))
        elif choice == "6":
            print("Thong ke theo the loai:")
            for loai, count in ThongKe_TheoLoaiSach(ds_sach).items():
                print(f"{loai}: {count}")
        elif choice == "7":
            print("Thong ke theo tong von:")
            for von, count in ThongKe_TheoTongVon(ds_sach).items():
                print(f"{von}: {count}")
        elif choice == "8":
            khoi = int(input("Nhap khoi lop: "))
            ds = Loc_SGK_TheoKhoi(ds_sach, khoi)
            for ten, gia in ds:
                print(f"Ten: {ten}, GiaBanCuoi: {gia}")
        elif choice == "9":
            nxb = input("Nhap NXB can tim: ")
            ds = Search_By_NXB(ds_sach, nxb)
            for thongtin in ds:
                print(thongtin)
        elif choice == "10":
            ds = Search_By_TimeRange(ds_sach)
            for thongtin in ds:
                print(thongtin)
        elif choice == "11":
            print("Sach sap xep theo gia ban tang dan:")
            ds = Sort_By_GiaBanTD(ds_sach)
            Hien_DS_Sach(ds)
        elif choice == "12":
            print("Sach sap xep theo gia ban giam dan:")
            ds = Sort_By_GiaBanGD(ds_sach)
            Hien_DS_Sach(ds)
        elif choice == "13":
            print("Sach co gia ban cao nhat:")
            ds = Max_GiaBan(ds_sach)
            for sach in ds:
                print(sach)
        elif choice == "14":
            print("Sach co gia ban thap nhat:")
            ds = Min_GiaBan(ds_sach)
            for sach in ds:
                print(sach)
        elif choice == "0":
            break
        else:
            print("Chuc nang khong hop le. Vui long chon lai.")


if __name__ == "__main__":
    DS=[]
    Menu(DS)
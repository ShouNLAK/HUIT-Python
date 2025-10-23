import json

class Cay():
    def __init__(self,ma,ten,tuyenduong,cao,duongkinh,tinhtrang):
        self.Ma = ma
        self.Ten = ten
        self.TuyenDuong = tuyenduong
        self.TinhTrang = tinhtrang
        if (cao <= 0 or duongkinh <= 0):
            raise ValueError("Chieu cao hoac Duong kinh phai lon hon 0")
        else:
            self.ChieuCao = float(cao)
            self.DuongKinh = float(duongkinh)
        
    def to_dict(self):
        return {"ma_cay":self.Ma, "ten_cay":self.Ten, "tuyen_duong":self.TuyenDuong, "chieu_cao":self.ChieuCao, "duong_kinh_than":self.DuongKinh, "tinh_trang":self.TinhTrang}
    
    def __str__(self):
        return f"{self.Ma:<10} | {self.Ten:<20} | {self.TuyenDuong:<20} | {self.ChieuCao:<10} | {self.DuongKinh:<10} | {self.TinhTrang}"
    
    def Xuat_Cay(self):
        print(f"{'Ma':<10} | {'Ten':<20} | {'Tuyen duong':<20} | {'Chieu cao':<10} | {'Duong kinh':<10} | {'Tinh trang'}")
        print(self)
    
    def Update_Data(self,loai,giaTriMoi):
        if loai == 1:
            self.Ten = giaTriMoi
        elif loai == 2:
            self.TuyenDuong = giaTriMoi
        elif loai == 3:
            self.ChieuCao = (float(giaTriMoi))
        elif loai == 4:
            self.DuongKinh = (float(giaTriMoi))
        elif loai == 5:
            self.TinhTrang = giaTriMoi
    
class DanhSachCayXanh():
    def __init__(self):
        self.DS = []
        
    def Tim_Cay_TheoMa(self,ma):
        for DataCay in self.DS:
            if DataCay.Ma.lower() == ma.lower():
                return DataCay
        return None
    
    def Tim_Cay_TheoTen_GanDung(self,ten):
        KQ = DanhSachCayXanh()
        for DataCay in self.DS:
            Tach = DataCay.Ten.split()
            for Tu in Tach:
                if (ten.lower() == Tu.lower()):
                    KQ.DS.append(DataCay)
        return KQ if len(KQ.DS) > 0 else None
    
    def Tim_Cay_TheoTen_ChinhXac(self,ten):
        KQ = DanhSachCayXanh()
        for DataCay in self.DS:
            if (DataCay.Ten.lower() == ten.lower()):
                KQ.DS.append(DataCay)
        return KQ if KQ.DS else None
        
    def Nhap_XML(self,tenFile):
        with open(tenFile,'r',encoding='utf-8') as fi:
            Data_Cay = json.load(fi)
            for Data in Data_Cay :
                self.DS.append(Cay(Data['ma_cay'],Data['ten_cay'],Data['tuyen_duong'],Data['chieu_cao'],Data['duong_kinh_than'],Data['tinh_trang']))
            
    def Ghi_XML(self,tenFile):
        data = [DataCay.to_dict() for DataCay in self.DS]
        with open(tenFile, 'w', encoding='utf-8') as fo:
            json.dump(data, fo, ensure_ascii=False, indent=5)
        return True
    
    def Xuat_DS(self):
        print(f"{'Ma':<10} | {'Ten':<20} | {'Tuyen duong':<20} | {'Chieu cao':<10} | {'Duong kinh':<10} | {'Tinh trang'}")
        for Data_Cay in self.DS:
            print(Data_Cay)
            
    def Them_Cay(self):
        ma = input("Nhap ma cay xanh :")
        if (self.Tim_Cay_TheoMa(ma) != None) :
            print("Ma cay xanh nay da ton tai")
            return False
        ten = input("Nhap ten cay xanh: ")
        tuyen = input("Nhap tuyen duong trong cay xanh : ")
        cao = float(input("Nhap chieu cao cay xanh : "))
        dk = float(input("Nhap duong kinh cay xanh : "))
        tinhtrang = input("Nhap tinh trang cay xanh : ")
        self.DS.append(Cay(ma,ten,tuyen,cao,dk,tinhtrang))
        return True
    
    def CapNhat_DataCay(self,ma):
        DataCay = self.Tim_Cay_TheoMa(ma)
        if (DataCay == None) :
            print("Ma cay xanh nay khong ton tai")
            return False
        DataCay.Xuat_Cay()
        loai = int(input("Nhap loai du lieu ma ban muon chinh sua (1-Ten | 2-Tuyen duong | 3-Chieu cao | 4-Duong kinh | 5-Tinh trang) : "))
        giaTri = input("Nhap gia tri moi : ")
        DataCay.Update_Data(loai,giaTri)
        self.DS = [DataCay if DataCay.Ma == DataGoc.Ma else DataGoc for DataGoc in self.DS]
        return True
        
    def Xoa_Cay(self,ma):
        DataCay = self.Tim_Cay_TheoMa(ma)
        if (DataCay == None) :
            print("Ma cay xanh nay khong ton tai")
            return False
        self.DS.remove(DataCay)
        print("Da xoa cay khoi danh sach")
        return True
        
    def Search_Cay(self,giaTri):
        if (self.Tim_Cay_TheoMa(giaTri) != None) :
            self.Tim_Cay_TheoMa(giaTri).Xuat_Cay()
            return True
        if (self.Tim_Cay_TheoTen_ChinhXac(giaTri) != None) :
            self.Tim_Cay_TheoTen_ChinhXac(giaTri).Xuat_DS()
            return True
        print("Khong tim thay cay theo ma hoac ten")
        return None
    
    def Tong_ChieuCao(self):
        sum = 0.0
        for DataCay in self.DS:
            sum += DataCay.ChieuCao
        return sum
    
    def Max_ChieuCao(self):
        List = DanhSachCayXanh()
        max = 0.0
        for DataCay in self.DS:
            if DataCay.ChieuCao > max:
                max = DataCay.ChieuCao
        List.DS = [DataCay for DataCay in self.DS if DataCay.ChieuCao == max]
        return List
    
    def Min_ChieuCao(self):
        List = DanhSachCayXanh()
        min = 0.0
        for DataCay in self.DS:
            if (DataCay.ChieuCao < min or min == 0):
                min = DataCay.ChieuCao
        List.DS = [DataCay for DataCay in self.DS if DataCay.ChieuCao == min]
        return List
    
    def SapXep_GDChieuCao(self):
        temp = DanhSachCayXanh()
        temp.DS = self.DS.copy()
        temp.DS.sort(key=lambda DataCay: DataCay.ChieuCao, reverse=True)
        return temp
        
    def SapXep_TDChieuCao(self):
        temp = DanhSachCayXanh()
        temp.DS = self.DS.copy()
        temp.DS.sort(key=lambda DataCay: DataCay.ChieuCao)
        return temp
        
    def Xuat_TOP_3_ChieuCao(self):
        temp = self.SapXep_TDChieuCao()
        top_3_list =DanhSachCayXanh()
        top_3_list.DS = temp.DS[:3]
        return top_3_list
    
    def Count_Cay(self):
        count=0
        for DataCay in self.DS:
            count += 1
        return count
    
    def TrungBinh_ChieuCao(self):
        return self.Tong_ChieuCao() / self.Count_Cay()
    
    def Loc_Cay_TinhTrangXau(self):
        List = DanhSachCayXanh()
        DS_TinhTrangXau = ["sâu bệnh", "gãy", "nghiêng", "lụi", "hư gốc"]
        for DataCay in self.DS:
            TinhTrang = DataCay.TinhTrang.lower()
            for tu_khoa in DS_TinhTrangXau:
                if tu_khoa in TinhTrang:
                    List.DS.append(DataCay)
                    break
        return List if List.DS else None
    
    def Count_Cay_BatThuong(self):
        loc_list = self.Loc_Cay_TinhTrangXau()
        return len(loc_list.DS) if loc_list else 0
    
    def ThongKe_Cay_TuyenDuong(self):
        TK = {}
        for DataCay in self.DS:
            if DataCay.TuyenDuong not in TK:
                TK[DataCay.TuyenDuong] = 1
            else:
                TK[DataCay.TuyenDuong] += 1
        return TK
    
    def ThongKe_Cay_ChieuCao(self,ChieuCaoToiThieu):
        count = 0
        for DataCay in self.DS:
            if DataCay.ChieuCao > ChieuCaoToiThieu:
                count += 1
        return count
    
    def TyLe_Cay_TinhTrangXau(self):
        return self.Count_Cay_BatThuong() / self.Count_Cay() * 100
    
    def Max_DuongKinh(self):
        List = DanhSachCayXanh()
        max = 0
        for DataCay in self.DS:
            if DataCay.DuongKinh > max:
                max = DataCay.DuongKinh
        List.DS = [DataCay for DataCay in self.DS if DataCay.DuongKinh == max]
        return List
    
    def SapXep_TDTuyenDuong(self):
        temp = DanhSachCayXanh()
        temp.DS = self.DS.copy()
        temp.DS.sort(key=lambda DataCay: DataCay.TuyenDuong)
        return temp
        
    def Count_Cay_BinhThuong(self):
        return self.Count_Cay() - self.Count_Cay_BatThuong()
    
    def Xuat_ChieuCao_CoDieuKien(self,a,b):
        List = DanhSachCayXanh()
        if (a > b):
            temp = a
            a = b
            b = temp
        for DataCay in self.DS:
            if (DataCay.ChieuCao >= a and DataCay.ChieuCao <= b):
                List.DS.append(DataCay)
        return List if List.DS else None
    
def Menu():
    print(" 1. Đọc dữ liệu từ file JSON")
    print(" 2. Hiển thị danh sách cây xanh")
    print(" 3. Thêm cây mới")
    print(" 4. Cập nhật thông tin cây xanh")
    print(" 5. Xóa cây xanh")
    print(" 6. Tìm kiếm cây theo mã hoặc tên")
    print(" 7. Tính tổng chiều cao toàn bộ cây xanh")
    print(" 8. Tìm cây cao nhất / thấp nhất")
    print(" 9. Sắp xếp danh sách theo chiều cao giảm dần")
    print("10. Ghi dữ liệu ra file JSON")
    print("11. Xuất file top 3 cây cao nhất")
    print("12. Tính chiều cao trung bình của cây xanh")
    print("13. Liệt kê cây cần chăm sóc đặc biệt")
    print("14. Ghi danh sách cây cần chăm sóc ra file JSON")
    print("15. Thống kê cây theo tuyến đường (nhập từ bàn phím)")
    print("16. Thống kê số lượng cây theo tuyến đường")
    print("17. Thống kê số lượng cây cao hơn 20 m")
    print("18. Tính tỷ lệ cây cần chăm sóc đặc biệt (%)")
    print("19. Tìm cây có đường kính thân lớn nhất")
    print("20. Liệt kê cây theo tên tuyến đường (A → Z)")
    print("21. Đếm số cây Bình thường và Bất thường")
    print("22. Xuất danh sách cây có chiều cao nằm trong khoảng nhập vào")
    print("23. Xuất danh sách cây có cùng loại (tên cây)")
    print("24. Tìm cây có tên chứa chuỗi ký tự bất kỳ")
    print("-"*25)
    print("0. Thoat chuong trinh")
    print("-"*25)
    chon = int(input("Hay nhap chuong trinh thuc thi :"))
    return chon
   
def Process():
    DanhSach = DanhSachCayXanh()
    f_input = "Cayxanh.json"
    while (True):
        chon = Menu()
        if (chon == 1):
            DanhSach.Nhap_XML(f_input)
            print(">> Da nhap file XML")
        elif (chon == 2):
            DanhSach.Xuat_DS()
        elif (chon == 3):
            if (DanhSach.Them_Cay() == True):
                DanhSach.Xuat_DS()
        elif (chon ==4):
            ma = input("Hay nhap ma cua cay : ")
            if (DanhSach.CapNhat_DataCay(ma) == True):
                DanhSach.Xuat_DS()
        elif (chon == 5):
            ma = input("Hay nhap ma cua cay : ")
            if (DanhSach.Xoa_Cay(ma) == True):
                DanhSach.Xuat_DS()
        elif (chon == 6):
            giaTri = input("Nhap gia tri (Ma hoac Ten) cua cay can tim : ")
            DanhSach.Search_Cay(giaTri)
        elif (chon == 7):
            print(f">> Tong chieu cao cua danh sach cay xanh : {DanhSach.Tong_ChieuCao()}")
        elif (chon == 8):
            print(f" >> Cay cao nhat : ")
            DanhSach.Max_ChieuCao().Xuat_DS()
            print(f" >> Cay thap nhat : ")
            DanhSach.Min_ChieuCao().Xuat_DS()
        elif (chon == 9):
            DanhSach.SapXep_GDChieuCao().Xuat_DS()
        elif (chon == 10) :
            DanhSach.Ghi_XML("Cayxanh-Output.json")
            print(">> Da ghi file thanh cong")
        elif (chon == 11):
            DanhSach.Xuat_TOP_3_ChieuCao().Xuat_DS()
            DanhSach.Xuat_TOP_3_ChieuCao().Ghi_XML("Top3-Output.json")
            print(">> Da xuat top 3 cay cao nhat")
        elif (chon == 12):
            print(f">> Chiều cao trung bình của cây xanh : {DanhSach.TrungBinh_ChieuCao()}")
        elif (chon == 13):
            loc_list = DanhSach.Loc_Cay_TinhTrangXau()
            if loc_list:
                loc_list.Xuat_DS()
            else:
                print(">> Khong co cay can cham soc dac biet")
        elif (chon == 14):
            loc_list = DanhSach.Loc_Cay_TinhTrangXau()
            if loc_list:
                loc_list.Ghi_XML("CayXau-Output.json")
                print(">> Da ghi danh sach cay can cham soc")
            else:
                print(">> Khong co cay can cham soc dac biet")
        elif (chon == 15):
            tuyen = input("Nhap ten tuyen duong : ")
            tk = DanhSach.ThongKe_Cay_TuyenDuong()
            if tuyen in tk:
                print(f">> {tuyen} : {tk[tuyen]} cay")
            else:
                print(">> Tuyen duong khong ton tai")
        elif (chon == 16):
            tk = DanhSach.ThongKe_Cay_TuyenDuong()
            for tuyen, count in tk.items():
                print(f"{tuyen} : {count}")
        elif (chon == 17):
            print(f">> So luong cay cao hon 20m : {DanhSach.ThongKe_Cay_ChieuCao(20)}")
        elif (chon == 18):
            print(f">> Ty le cay can cham soc dac biet : {DanhSach.TyLe_Cay_TinhTrangXau()}%")
        elif (chon == 19):
            DanhSach.Max_DuongKinh().Xuat_DS()
        elif (chon == 20):
            DanhSach.SapXep_TDTuyenDuong().Xuat_DS()
        elif (chon == 21):
            print(f">> So cay Binh thuong : {DanhSach.Count_Cay_BinhThuong()}")
            print(f">> So cay Bat thuong : {DanhSach.Count_Cay_BatThuong()}")
        elif (chon == 22):
            a = float(input("Nhap chieu cao tu : "))
            b = float(input("Nhap chieu cao den : "))
            result = DanhSach.Xuat_ChieuCao_CoDieuKien(a, b)
            if result:
                result.Xuat_DS()
            else:
                print(">> Khong co cay trong khoang chieu cao nay")
        elif (chon == 23):
            ten = input("Nhap ten cay : ")
            result = DanhSach.Tim_Cay_TheoTen_ChinhXac(ten)
            if result:
                result.Xuat_DS()
            else:
                print(">> Khong tim thay cay voi ten nay")
        elif (chon == 24):
            tu = input("Nhap chuoi ky tu : ")
            result = DanhSach.Tim_Cay_TheoTen_GanDung(tu)
            if result:
                result.Xuat_DS()
            else:
                print(">> Khong tim thay cay chứa chuoi ky tu nay")
        elif (chon == 0):
            break
        else:
            print("Nhap sai chuong trinh")

Process()
 

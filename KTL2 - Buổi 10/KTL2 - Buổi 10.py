import json

class NhanVien:
    def __init__(self,ma,ten,user,passuser,luong,phai,tuoi,phong):
        self.Ma = ma
        self.HoTen = ten
        self.Username = user
        self.Password = passuser
        self.Luong = int(luong)
        self.GioiTinh = phai
        self.Tuoi = int(tuoi)
        self.PhongBan = phong
        
    def to_dict(self):
        return {"ma_nv": self.Ma, "ho_ten": self.HoTen, "user": self.Username, "pass": self.Password, "luong": self.Luong, "gioi_tinh": self.GioiTinh, "tuoi": self.Tuoi, "phong": self.PhongBan}
    
    def __str__(self):
        return f"{self.Ma} | {self.HoTen} | {self.Username} | {self.Password} | {self.Luong} | {self.GioiTinh} | {self.Tuoi} | {self.PhongBan}"
    
class DSNV:
    def __init__(self):
        self.DS = []
    
    # Câu 1
    def Xuat_DS(self):
        for NV in self.DS :
            print(NV)
            
    def Nhap_JSON(self,tenFile):
        with open(tenFile,'r',encoding='utf-8') as fi:
            Data_NV = json.load(fi)
            for Data in Data_NV :
                self.DS.append(NhanVien(Data['ma_nv'],Data['ho_ten'],Data['user'],Data['pass'],Data['luong'],Data['gioi_tinh'],Data['tuoi'],Data['phong']))
    # Câu 2            
    def count_NV_Luong_Tren(self,mucLuong):
        count = 0
        for NV in self.DS :
            if NV.Luong > 30000000:
                count += 1
        return count
    # Câu 5
    def ThongKe_PhongBan(self):
        TK = {}
        for NV in self.DS :
            if NV.PhongBan not in TK:
                TK[NV.PhongBan] = 1
            else :
                TK[NV.PhongBan] += 1
        return TK
    # Câu 3
    def ThongKe_Phong(self,loaiPhong):
        TK = self.ThongKe_PhongBan()
        for Phong,SoLuong in TK.items():
            if Phong == loaiPhong:
                return SoLuong
    # Câu 4
    def Login(self,user,pword):
        for NV in self.DS:
            if NV.Username == user :
                if NV.Password == pword:
                    return f"Đăng nhập thành công! Xin chào bạn {NV.HoTen}"
        return f"Tên đăng nhập hoặc mật khẩu không đúng."
    # Câu 6
    def DSNV_SapVeHuu(self):
        KQ = DSNV()
        for NV in self.DS :
            if (NV.GioiTinh == "Nam" and NV.Tuoi + 2 >= 60) or (NV.GioiTinh == "Nữ" and NV.Tuoi + 2 >= 55):
                KQ.DS.append(NV)
        return KQ
    
    def sum_Tuoi_Phong(self,loaiPhong):
        sum_tuoi = 0
        for NV in self.DS :
            if NV.PhongBan == loaiPhong:
                sum_tuoi += NV.Tuoi
        return sum_tuoi
    # Câu 7
    def avg_Tuoi_Phong(self,loaiPhong):
        return self.sum_Tuoi_Phong(loaiPhong)*1.0 / self.ThongKe_Phong(loaiPhong)*1.0
    
    def Them_NV_ThongTin(self):
        ma = input("Nhập mã nhân viên : ")
        ten = input("Nhập họ va tên nhân viên : ")
        user = input("Nhập Username nhân viên : ")
        passuser = input("Nhập mật khẩu user nhân viên : ")
        luong = int(input("Nhập mức lương nhân viên : "))
        phai = input("Nhập giới tính nhân viên (1 - Nữ | 2 - Nam): ")
        if phai == "1" :
            phai = "Nữ"
        elif phai == "2" :
            phai = "Nam"
        else:
            raise ValueError ("Nhập sai định dạng")
        tuoi = int(input("Nhập tuổi nhân viên : "))
        phong = input("Nhập phòng ban của nhân viên : ")
        return ma,ten,user,passuser,luong,phai,tuoi,phong
    # Câu 8
    def Them_NV_DS(self):
        ma,ten,user,passuser,luong,phai,tuoi,phong = self.Them_NV_ThongTin()
        if (phai == "Nam" and tuoi > 55) or (phai == "Nữ" and tuoi > 50) :
            return f"Sai độ tuổi quy định (Nam - Dưới 55 | Nữ - Dưới 50)"
        for NV in self.DS :
            if NV.Ma.lower() == ma.lower() :
                return f"Mã nhân viên này đã tồn tại"
        self.DS.append(NhanVien(ma,ten,user,passuser,luong,phai,tuoi,phong))
        return f"Đã thêm nhân viên thành công"
    # Câu 9
    def NV_Max_Luong(self):
        Max = 0
        for NV in self.DS :
            if Max < NV.Luong :
                Max = NV.Luong
        List_NV = DSNV()
        for NV in self.DS :
            if Max == NV.Luong :
                List_NV.DS.append(NV)
        return List_NV
    # Câu 10
    def Ghi_JSON_Phong(self,Phong,tenFile = 'NhanVien_ThuocPhongChiDinh.json'):
        data = [NV.to_dict() for NV in self.DS if NV.PhongBan == "Thực phẩm"]
        with open(tenFile, 'w', encoding='utf-8') as fo:
            json.dump(data, fo, ensure_ascii=False, indent=5)
        return True
    
def Menu():
    print("1.  Xuất danh sách nhân viên")
    print("2.  Tổng số nhân viên có lương > 30 triệu")
    print("3.  Thống kê số lượng nhân viên thuộc phòng Thực Phẩm ")
    print("4.  Đăng nhập")
    print("5.  Xuất sĩ số nhân viên theo từng phòng ban")
    print("6.  Xuất danh sách nhân viên còn 2 năm là về hưu, nếu nữ tính tuổi về hưu là 55, nam là 60.")
    print("7.  Tính tuổi trung bình theo giới tính của phòng Thời Trang ")
    print("8.  Thêm nhân viên mới vào danh sách, Mã nhân viên phải theo định dạng:  Mã nhân viên đó chưa tồn tại mới cho thêm, Tuổi phải dưới 50 cho nữ, và dưới 55 cho nam")
    print("9.  Xuất mã nhân viên, tên nhân viên có lương cao nhất")
    print("10. Ghi file chứa danh sách nhân viên thuộc phòng ban:”Thực phẩm”")
    print("======================================================================")
    print("0.  Thoát chương trình")
    
    chon = int(input(">>> Chọn chương trình cần thực thi : "))
    return chon
    
def Process():
    List = DSNV()
    List.Nhap_JSON("Nhanvien.json")
    while (True) :
        chon = Menu()
        if chon == 1 :
            List.Xuat_DS()
        elif chon == 2:
            print(f"Số lượng nhân vien có mức lương trên 30 000 000 là : {List.count_NV_Luong_Tren(30000000)}")
        elif chon == 3:
            print(f'Số lượng nhân viên của phòng Thực Phẩm là : {List.ThongKe_Phong("Thực phẩm")}')
        elif chon == 4:
            user = input("Nhập Username của bạn : ")
            pword = input("Nhập password : ")
            print(List.Login(user, pword))
        elif chon == 5 :
            TK = List.ThongKe_PhongBan()
            for LoaiPhong,SoLuong in TK.items() :
                print(f"{LoaiPhong} : {SoLuong}")
        elif chon == 6 :
            KQ = List.DSNV_SapVeHuu()
            KQ.Xuat_DS()
        elif chon == 7:
            print(f'Độ tuổi trung bình của phòng Thời Trang là : {List.avg_Tuoi_Phong("Thời trang")}')
        elif chon == 8:
            print(f"{List.Them_NV_DS()}")
        elif chon == 9:
            KQ = List.NV_Max_Luong()
            KQ.Xuat_DS()
        elif chon == 10:
            List.Ghi_JSON_Phong("Thực phẩm")
            
        elif chon == 0:
            break
            
Process()
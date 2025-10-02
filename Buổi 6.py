class Sach:
    def __init__(self,ma,ten,tg,namxb,trangthai = "Có sẵn"):
        self.Ma = ma
        self.Ten = ten
        self.TacGia = tg
        self.NamXB = namxb
        self.TrangThai = trangthai

    def __str__(self):
        return f"{self.Ma} | {self.Ten} | {self.TacGia} | {self.NamXB} | {self.TrangThai}"
    
    def xuat_thong_tin(self):
        print(f"Mã: {self.Ma} | Tên: {self.Ten} | Tác giả: {self.TacGia} | Năm xuất bản: {self.NamXB} | Trạng thái: {self.TrangThai}")

    def thay_doi_trang_thai(self):
        if self.TrangThai == "Có sẵn":
            self.TrangThai = "Đã mượn"
        else:
            self.TrangThai = "Có sẵn"
    
    def kiem_tra_Trang_Thai_cho_muon(self):
        if self.TrangThai == "Có sẵn":
            return True
        return False
        
    def muon_sach(self):
        if self.kiem_tra_Trang_Thai_cho_muon() == True:
            self.thay_doi_trang_thai()
            return "Đã mượn sách thành công"
        else:
            return "Sách hiện tại đang được cho mượn trước đó"

    def tra_sach(self):
        if self.kiem_tra_Trang_Thai_cho_muon() == True:
            return "Không thể trả sách do sách hiện tại chưa được mượn"
        else:
            self.thay_doi_trang_thai()
            return "Đã trả sách thành công"
    
def Nhap_DSQL():
    list = []
    n = int(input("Nhập số lượng sách mà bạn cần quản lý : "))
    for i in range (n):
        print(f"--- Nhập thông tin cuốn sách thứ {i+1} ---")
        MaSach = input("Nhập mã sách : ")
        TenSach = input("Nhập tên sách : ")
        TacGia = input("Nhập tên tác giả : ")
        NamXB = input("Nhập năm xuất bản : ")
        TrangThai = input("1 - Có sẵn / 2 - Đã mượn")
        if TrangThai == "1" : 
            TrangThai = "Có sẵn"
        else :
            TrangThai = "Đã mượn"
        SachTemp = Sach(MaSach , TenSach , TacGia, NamXB,TrangThai)
        list.append(SachTemp)
    return list

def Muon_Sach(list):
    Search = input("Nhập mã sách cần mượn : ")
    for CuonSach in list :
        if CuonSach.Ma == Search :
            print("Trạng thái lúc trước :")
            CuonSach.xuat_thong_tin()
            CuonSach.muon_sach()
            print("Trạng thái lúc sau :")
            CuonSach.xuat_thong_tin()

def Tra_Sach(list):
    Search = input("Nhập mã sách cần trả : ")
    for CuonSach in list :
        if CuonSach.Ma == Search :
            print("Trạng thái lúc trước : ")
            CuonSach.xuat_thong_tin()
            CuonSach.tra_sach()
            print("Trạng thái lúc sau : ")
            CuonSach.xuat_thong_tin()

def Xuat_DSQL(list) :
    print("Mã sách | Tên sách | Tác giả | Năm xuất bản | Trạng thái")
    for CuonSach in list :
        CuonSach.xuat_thong_tin()

def Search_By_Ma(list) :
    Search = input("Nhập mã sách : ")
    for CuonSach in list :
        if CuonSach.Ma == Search :
            return CuonSach
    return "Not Found"

def Search_By_Name(list) :
    Search = input("Nhập tên sách : ")
    for CuonSach in list :
        if CuonSach.Ten == Search:
            return CuonSach
    return "Not Found"    
    
def Search_By_TacGia(list):
    Temp = []
    Search = input("Nhập tên tác giả : ")
    for CuonSach in list :
        if CuonSach.TacGia == Search :
            Temp.append(CuonSach)
    if (Temp != None):
        return Temp
    return "Not Found"

def ThongKe_TrangThai(list) :
    CoSan = DaMuon = 0
    for CuonSach in list :
        if CuonSach.TrangThai == "Có sẵn":
            CoSan += 1
        else :
            DaMuon += 1
    return CoSan,DaMuon

def ThongKe_TheoNam(list):
    temp = sorted(list, key=lambda t: t.NamXB)
    ThongKe = {}
    for CuonSach in temp:
        if CuonSach.NamXB not in ThongKe :
            ThongKe[CuonSach.NamXB] = 1
        else:
            ThongKe[CuonSach.NamXB] += 1
    
    return ThongKe


def sort_TheoNam(list):
    temp = sorted(list, key=lambda t: t.NamXB)
    print("Danh sách sách theo từng năm xuất bản")
    for CuonSach in temp:
        CuonSach.xuat_thong_tin()

def sort_TheoTen(list) :
    temp = sorted(list, key=lambda t: t.Ten)
    print("Danh sách sách theo tên")
    for CuonSach in temp:
        CuonSach.xuat_thong_tin()

def menu():
    list = []
    while True:
        print("\n===== MENU QUẢN LÝ SÁCH =====")
        print("1. Nhập danh sách sách")
        print("2. Xuất danh sách sách")
        print("3. Mượn sách")
        print("4. Trả sách")
        print("5. Tìm kiếm theo mã sách")
        print("6. Tìm kiếm theo tên sách")
        print("7. Tìm kiếm theo tác giả")
        print("8. Thống kê trạng thái sách")
        print("9. Thống kê số lượng sách theo năm xuất bản")
        print("10. Sắp xếp sách theo năm xuất bản")
        print("11. Sắp xếp sách theo tên")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            list = Nhap_DSQL()
        elif choice == "2":
            Xuat_DSQL(list)
        elif choice == "3":
            Muon_Sach(list)
        elif choice == "4":
            Tra_Sach(list)
        elif choice == "5":
            result = Search_By_Ma(list)
            if result == "Not Found":
                print(result)
            else :
                print(result.xuat_thong_tin())
        elif choice == "6":
            result = Search_By_Name(list)
            if result == "Not Found":
                print(result)
            else :
                print(result.xuat_thong_tin())
        elif choice == "7":
            KQ = Search_By_TacGia(list)
            if bool(KQ) == False :
                print("Not Found")
            else:
                for CuonSach in KQ:
                    CuonSach.xuat_thong_tin()
        elif choice == "8":
            CoSan, DaMuon = ThongKe_TrangThai(list)
            print(f"Có sẵn : {CoSan} | Đã mượn : {DaMuon}")
        elif choice == "9":
            ThongKe = ThongKe_TheoNam(list)
            for Nam, SoLuong in ThongKe.items():
                print(f"Năm {Nam} : {SoLuong} cuốn sách")
        elif choice == "10":
            sort_TheoNam(list)
        elif choice == "11":
            sort_TheoTen(list)
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")

menu()


sach1=Sach("S001","Lập trình Python","Nguyễn Văn A",2021)
sach2=Sach("S002","Cấu trúc dữ liệu","Trần Thị B",2019,"Đã mượn")

print("Thông tin ban đầu của 2 cuốn sách : ")
sach1.xuat_thong_tin()
sach2.xuat_thong_tin()

print("Mượn sách 1:")
sach1.muon_sach()
sach1.xuat_thong_tin()

print("Trả sách 2 :")
sach2.tra_sach()
sach2.xuat_thong_tin()

print("Đổi trạng thái sách 1:")
sach1.thay_doi_trang_thai()
sach1.xuat_thong_tin()
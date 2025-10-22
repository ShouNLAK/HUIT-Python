don_hang = {
    'DH001' : 3,
    'DH002' : 5,
    'DH003' : 2,
    'DH004' : 7, 
    'DH005' : 1,
    'DH006' : 4,
    'DH007' : 6,
    'DH008' : 8,
    'DH009' : 2,
    'DH010' : 9
}

#1.	In toàn bộ danh sách đơn hàng và số món ăn.
def Xuat_DSDH(list):
    for DonHang, SoMon in list.items():
        print(f"Ma don hang : {DonHang} | {SoMon} mon an")

#2.	Đếm tổng số đơn hàng hiện có.
def Count_DonHang(list) :
    Count = 0
    for DonHang in list :
        Count += 1
    return Count

#3.	Tính tổng số món ăn đã đặt trong tất cả các đơn.
def Count_SoLuong_MonAn(list) :
    Count = 0
    for DonHang, SoLuong in list.items():
        Count += SoLuong
    return Count

#4.	Tìm đơn hàng có số món nhiều nhất và in ra mã cùng số món.
def Max_SoLuong_MonAn(list) :
    KQ = {}
    Max = 0
    for DonHang, SoLuong in list.items():
        if SoLuong > Max :
            Max = SoLuong
    for DonHang,SoLuong in list.items():
        if SoLuong == Max :
            KQ[DonHang] = SoLuong
    return KQ

#5.	Tìm tất cả đơn hàng có số món ≤ 2 (đơn nhỏ).
def Search_DonHang_SoLuongNho(list) :
    KQ = {}
    for DonHang, SoLuong in list.items():
        if SoLuong <= 2 :
            KQ[DonHang] = SoLuong
    return KQ

#6.	In ra mã đơn hàng đầu tiên và cuối cùng trong danh sách.
def Xuat_DH_First_Last(list) :
    KQ = {}
    Now = 0
    Total = Count_DonHang(list)
    for DonHang,SoLuong in list.items() :
        Now += 1
        if Now == 1 or Now == Total :
            KQ[DonHang] = SoLuong
    return KQ

#7.	In ra tổng số món lẻ trong tất cả đơn hàng.
def Xuat_Sum_SoLuong_Le(list) :
    Sum = 0
    for DonHang, SoLuong in list.items() :
        if SoLuong %2 != 0:
            Sum += SoLuong
    return Sum
    
#8.	Viết chương trình cho phép nhập vào một mã đơn hàng và số món muốn thêm 
def Nhap_DH(list) :
    MaDH = input("Hay nhap ma don hang : ")
    SoLuong = int(input("Hay nhap so luong mon : "))
    if MaDH in list:
        #Nếu đơn tồn tại thì cập nhật số món
        print("Da cap nhat don hang da ton tai")
        list[MaDH] = SoLuong
    else :
        #Nếu đơn không tồn tại → in "Mã đơn hàng không tồn tại!".
        print("Ma don hang khong ton tai")
        
#9.	Xuất danh sách đơn hàng có số món trong khoảng [a, b] (do người dùng nhập).
def Xuat_DH_Co_DK(list) :
    a = int(input("Nhap pham vi cua a trong [a,b]: "))
    b = int(input("Nhap pham vi cua b trong [a,b]: "))
    if a > b :
        temp = a
        a = b
        b = temp
    KQ = {}
    for DonHang, SoLuong in list.items():
        if (SoLuong >= a and SoLuong <= b):
            KQ[DonHang] = SoLuong
    return KQ

#10.	Sắp xếp danh sách đơn hàng theo số món:
# Tăng dần
def sort_List_TangDan(list):
    list = dict(sorted(list.items(), key=lambda DonHang : DonHang[1]))
    return list
# Giảm dần
def sort_List_GiamDan(list):
    list = dict(sorted(list.items(), key=lambda DonHang : DonHang[1] * -1))
    return list

#11.	Xuất Top 3 đơn hàng có nhiều món nhất
def Xuat_TOP_3(list):
    temp = sort_List_GiamDan(list)
    KQ = {}
    Top = 0
    for DonHang, SoLuong in temp.items():
        Top += 1
        if (Top <= 3) :
            KQ[DonHang] = SoLuong
    return KQ

#12.	Xuất danh sách đơn hàng có nguy cơ bị hủy (ví dụ: đơn ≤ 1 món).
def Xuat_DH_Huy(list) :
    KQ = {}
    for DonHang, SoLuong in list.items():
        if SoLuong <= 1:
            KQ[DonHang] = SoLuong
    return KQ


def Menu():
    print("1. In ra toàn bộ danh sách đơn hàng và món ăn")
    print("2. Đếm tổng số đơn hàng hiện có")
    print("3. Tính tổng số món ăn đã đặt trong tất cả các đơn")
    print("4. Tìm đơn hàng có số món nhiều nhất")
    print("5. Tìm tất cả đơn hàng có số món <= 2")
    print("6. In ra mã đơn hàng đầu tiên và cuối cùng trong danh sách")
    print("7. In ra tổng số món lẻ trong tất cả đơn hàng")
    print("8. Nhập 1 đơn hàng")
    print("9. Xuất DS Đơn hàng có số món trong khoảng [a,b]")
    print("10. Sắp xếp danh sách đơn hàng theo số món tăng dần - giảm dần")
    print("11. Xuất top 3 đơn hàng đặt nhiều món nhất")
    print("12. Xuất DS Đơn hàng có nguy cơ bị hủy")
    choose = int(input("Nhập chương trình bạn muốn chạy"))
    if choose == 1:
        Xuat_DSDH(don_hang)
    elif choose == 2:
        print(f"Co tong cong : {Count_DonHang(don_hang)}")
    elif choose ==3 :
        print(f"Co tong cong : {Count_SoLuong_MonAn(don_hang)}")
    elif choose == 4:
        KQ = Max_SoLuong_MonAn(don_hang)
        for DonHang, SoLuong in KQ.items() :
            print(f"Ma don hang : {DonHang} | {SoLuong} mon an")
    elif choose == 5 :
        KQ = Search_DonHang_SoLuongNho(don_hang)
        for DonHang, SoLuong in KQ.items() :
            print(f"Ma don hang : {DonHang} | {SoLuong} mon an")
    elif choose == 6:
        KQ = Xuat_DH_First_Last(don_hang)
        for DonHang, SoLuong in KQ.items() :
            print(f"Ma don hang : {DonHang} | {SoLuong} mon an")
    elif choose == 7:
        print(f"Tong so mon le trong tat ca mon hang : {Xuat_Sum_SoLuong_Le(don_hang)}")
    elif choose == 8:
        Nhap_DH(don_hang)
        Xuat_DSDH(don_hang)
    elif choose == 9:
        KQ = Xuat_DH_Co_DK(don_hang)
        for DonHang, SoLuong in KQ.items() :
            print(f"Ma don hang : {DonHang} | {SoLuong} mon an")
    elif choose == 10:
        print("--- Tang Dan ---")
        KQ = sort_List_TangDan(don_hang)
        for DonHang, SoLuong in KQ.items() :
            print(f"Ma don hang : {DonHang} | {SoLuong} mon an")
        print("--- Giam Dan ---")
        KQ = sort_List_GiamDan(don_hang)
        for DonHang, SoLuong in KQ.items() :
            print(f"Ma don hang : {DonHang} | {SoLuong} mon an")
    elif choose == 11:
        KQ = Xuat_TOP_3(don_hang)
        for DonHang, SoLuong in KQ.items() :
            print(f"Ma don hang : {DonHang} | {SoLuong} mon an")
    elif choose == 12:
        KQ = Xuat_DH_Huy(don_hang)
        for DonHang, SoLuong in KQ.items() :
            print(f"Ma don hang : {DonHang} | {SoLuong} mon an")
    Menu()

Menu()

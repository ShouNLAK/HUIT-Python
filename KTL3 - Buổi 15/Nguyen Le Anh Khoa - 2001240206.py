import json
import tkinter as tk
from tkinter import messagebox,ttk
import re

def tai_du_lieu():
    try:
        with open("Hocsinh.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Lỗi tìm file","Hàm tai_du_lieu không tìm thấy file dữ liệu học sinh")
        return []
    
def tai_du_lieu_TC():
    try:
        with open("Thamgiatrongcay.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Lỗi tìm file","Hàm tai_du_lieu không tìm thấy file dữ liệu trồng cây")
        return []
    
def luu_du_lieu(data):
    with open("Hocsinh.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def luu_du_lieu_TC(data):
    with open("Thamgiatrongcay.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def xoa_bang():
    Tree.delete(*Tree.get_children())

def cap_nhat_bang(data_HS_):
    xoa_bang()
    for HS in data_HS_:
        Tree.insert("", "end", values=(HS.get("maHS"), HS.get("hoTen"), HS.get("lop"),HS.get("email"),HS.get("sdt")))

def GetInfo(event):
    Chon = Tree.selection()
    if not Chon:
        return
    EntryMa.delete(0, tk.END)
    EntryTen.delete(0, tk.END)
    EntryLop.delete(0, tk.END)
    EntryEmail.delete(0, tk.END)
    EntryPhone.delete(0, tk.END)
    ma, ten, lop,email,sdt = Tree.item(Chon[0])["values"]
    EntryMa.insert(0, ma)
    EntryTen.insert(0, ten)
    EntryLop.insert(0, lop)
    EntryEmail.insert(0,email)
    EntryPhone.insert(0,sdt)

def load_input():
    MaHS = EntryMa.get()
    HoTen = EntryTen.get()
    Lop = EntryLop.get()
    Email = EntryEmail.get()
    SDT = EntryPhone.get()
    return MaHS,HoTen,Lop,Email,SDT

# Câu 3 : Kiểm tra không cho trùng mã
def checkMaHStontai(ma):
    data_HS = tai_du_lieu()
    for HS in data_HS :
        if HS["maHS"] == ma:
            return True
    return False

# Câu 3 : Ràng buộc định dạng mã học sinh
def checkMaHSformat(ma):
    return bool(re.fullmatch(r"HS[0-9]{3}", ma))

# Câu 4 : Ràng buộc số điện thoại
def checkPhoneformat(Phone):
    return bool(re.fullmatch(r"(0|\+84)[0-9]{9}", Phone))

# Câu 4 : Ràng buộc Email
def checkEmailformat(Email):
    return bool(re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w+", Email))

# Câu 5 : Thêm học sinh
def Them():
    MaHS,HoTen,Lop,Email,SDT = load_input()
    if not(MaHS and HoTen and Lop and Email and SDT) :
        return messagebox.showerror("Lỗi thêm học sinh","Cần phải nhập đủ các ô")
    if (checkMaHStontai(MaHS)):
        return messagebox.showerror("Lỗi thêm học sinh",f"Đã tồn tại mã {MaHS} trong hệ thống")
    if not (checkMaHSformat(MaHS)):
        return messagebox.showerror("Lỗi thêm học sinh","Mã học sinh không đúng format : HSxxx")
    if not (checkPhoneformat(SDT)):
        return messagebox.showerror("Lỗi thêm học sinh","Số điện thoại chưa đúng định dạng")
    if not (checkEmailformat(Email)):
        return messagebox.showerror("Lỗi thêm học sinh","Email chưa đúng dịnh dạng")
    data_HS.append({"maHS":MaHS,"hoTen":HoTen,"lop":Lop,"email":Email,"sdt":SDT})
    luu_du_lieu(data_HS)
    cap_nhat_bang(data_HS)
    messagebox.showinfo("Thêm học sinh","Thành công")
    return True

# Câu 6 : Sửa học sinh
def Sua():
    MaHS,HoTen,Lop,Email,SDT = load_input()
    if not(MaHS and HoTen and Lop and Email and SDT) :
        return messagebox.showerror("Lỗi cập nhật học sinh","Cần phải nhập đủ các ô")
    if not (checkPhoneformat(SDT)):
        return messagebox.showerror("Lỗi cập nhật học sinh","Số điện thoại chưa đúng định dạng")
    if not (checkEmailformat(Email)):
        return messagebox.showerror("Lỗi cập nhật học sinh","Email chưa đúng dịnh dạng")
    data_HS = tai_du_lieu()
    found = False
    for HS in data_HS:
        if HS.get("maHS") == MaHS:
            HS["hoTen"] = HoTen
            HS["lop"] = Lop
            HS["email"] = Email
            HS["sdt"] = SDT
            found = True
            break
    if not found:
        messagebox.showerror("Lỗi cập nhật học sinh", f"Không tìm thấy học sinh {MaHS} để cập nhật.")
        return
    luu_du_lieu(data_HS)
    cap_nhat_bang(data_HS)
    messagebox.showinfo("Sửa học sinh","Thành công")

# Câu 7 : Xóa học sinh (Kèm theo xóa thông tin trồng cây nếu có)
def Xoa():
    MaHS,HoTen,Lop,Email,SDT = load_input()
    if not MaHS:
        messagebox.showerror("Lỗi xóa học sinh", "Vui lòng nhập Mã SV hoặc chọn cụ thể trong TreeView để xóa.")
        return
    data_HS = tai_du_lieu()
    new_data_HS = [HS for HS in data_HS if HS.get("maHS") != MaHS]
    if len(new_data_HS) == len(data_HS):
        messagebox.showerror("Lỗi xóa học sinh", "Không tìm thấy học sinh để xóa.")
        return
    new_data_TC = [HS for HS in data_TrongCay if HS.get("maHS") != MaHS]
    luu_du_lieu_TC(new_data_TC)
    luu_du_lieu(new_data_HS)
    data_HS = new_data_HS
    cap_nhat_bang(data_HS)
    messagebox.showinfo("Xóa học sinh","Thành công")

# Câu 8 : Chức năng tìm kiếm
def Tim():
    DS = []
    data=tai_du_lieu()
    Search = EntryFindMa.get()
    for HS in data:
        if HS["maHS"] == Search :
            DS.append(HS)
    cap_nhat_bang(DS)

# Câu 9 + 10 : Thống kê theo lớp được chỉ định và toàn hệ thống
def ThongKe_Lop():
    Count_Lop = 0
    Count_All = 0
    TK = {}
    Lop = EntryTKLop.get().strip()
    if not Lop:
        messagebox.showerror("Lỗi thống kê", "Chưa nhập lớp cần thống kê")
        return
    data = tai_du_lieu()
    data_TC = tai_du_lieu_TC()

    for HS in data:
        for HS_TC in data_TC:
            if HS.get("maHS") == HS_TC.get("maHS"):
                lop = HS.get("lop")
                TK[lop] = TK.get(lop, 0) + 1

    if not TK:
        messagebox.showinfo("Thống kê", "Chưa có dữ liệu trồng cây.")
        return

    Count_All = sum(TK.values())
    Count_Lop = TK.get(Lop, 0)
    Max = max(TK.values())
    Lop_Max = [lop for lop, soCay in TK.items() if soCay == Max]
    percent = (Count_Lop / Count_All * 100) if Count_All else 0

    messagebox.showinfo(
        "Thống kê",
        f"Số cây được trồng bởi lớp : {Lop} = {Count_Lop} cây ({percent:.2f} %)\n"
        f"Tổng số cây đã trồng theo toàn bộ danh sách = {Count_All} cây\n"
        f"Lớp trồng được nhiều cây nhất : {Lop_Max} ({Max} cây)"
    )
    
# Câu 1 : Thiết kế giao diện
root = tk.Tk()
root.title("Quản lý học sinh tham gia trồng cây")
root.geometry("1080x500")
data_HS = tai_du_lieu()
data_TrongCay = tai_du_lieu_TC()

tk.Label(text="Mã HS").grid(row=0,column=0)
EntryMa = tk.Entry()
EntryMa.grid(row = 0, column = 1,columnspan= 10)

tk.Label(text="Tên HS").grid(row=1,column=0)
EntryTen = tk.Entry()
EntryTen.grid(row=1,column=1,columnspan=10)

tk.Label(text="Lớp").grid(row=2,column=0)
EntryLop = tk.Entry()
EntryLop.grid(row=2,column=1,columnspan=10)

tk.Label(text="Email").grid(row=3,column=0)
EntryEmail = tk.Entry()
EntryEmail.grid(row=3,column=1,columnspan=10)

tk.Label(text="SĐT").grid(row=4,column=0)
EntryPhone = tk.Entry()
EntryPhone.grid(row=4,column=1,columnspan=10)

tk.Button(text="Thêm",command=Them).grid(row=5,column=0)
tk.Button(text="Sửa",command=Sua).grid(row=5,column=1)
tk.Button(text="Xóa",command=Xoa).grid(row=5,column=2)
tk.Label(text="Mã HS:").grid(row=5,column=3)
EntryFindMa = tk.Entry()
EntryFindMa.grid(row=5,column=4,columnspan=2)
tk.Button(text="Tìm",command=Tim).grid(row=5,column=6)
tk.Label(text="Lớp thống kê:").grid(row=5,column=7)
EntryTKLop = tk.Entry()
EntryTKLop.grid(row=5,column=8,columnspan=2)
tk.Button(text="Thống kê",command=ThongKe_Lop).grid(row=5,column=10)

# Câu 2 : Thiết kế TreeView
Tree = ttk.Treeview(root, columns=("maHS", "hoTen", "lop","email","sdt"), show="headings", height=10)
Tree.heading("maHS", text="Mã HS")
Tree.heading("hoTen", text="Tên HS")
Tree.heading("lop", text="Lớp")
Tree.heading("email",text="Email")
Tree.heading("sdt",text="SĐT")
Tree.bind("<<TreeviewSelect>>", GetInfo)
Tree.grid(row=6,column=0,columnspan=10)

cap_nhat_bang(data_HS)
root.mainloop()
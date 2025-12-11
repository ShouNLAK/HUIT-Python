import tkinter as tk
from tkinter import messagebox
import json
import random
from datetime import datetime

def load_Staff():
    try:
        with open("Nhanvien.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file Nhanvien.json")
        return
    
def load_Sach():
    try:
        with open("Sach.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file Sach.json")
        return
    
def load_PhieuMuon():
    try:
        with open("Phieumuon.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file Phieumuon.json")
        return

def load_DocGia():
    try:
        with open("Docgia.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file Docgia.json")
        return

def load_ChiTietPM():
    try:
        with open("Chitietphieumuon.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file Chitietphieumuon.json")
        return

def Login():
    User = EntryUser.get()
    Pass = EntryPass.get()

    for NhanVien in Staff_List:
        if NhanVien['user'] == User and NhanVien['pass'] == Pass:
            messagebox.showinfo("Đã đăng nhập", f"Chào mừng nhân viên : {NhanVien['ho_ten']}")
            root.destroy() 
            Staff_Menu(NhanVien)
            return
    messagebox.showerror("Lỗi đăng nhập", "Tên tài khoản hoặc mật khẩu không đúng\nVui lòng kiểm tra lại")

def Add_PhieuMuon(ma,docgia,nhanvien) :
    PhieuMuon_List.append({"MaDocGia": docgia, "MaPhieuMuon": ma,"MaNV": nhanvien['MaNV'], "NgayMuon": datetime.today().strftime("%Y-%m-%d")})

def Add_ChiTietPM(ma_pm, ma_sach):
    ChiTietPM_List.append({"MaPhieuMuon": ma_pm, "MaSach": ma_sach, "TinhTrang": "Còn mượn"})

def Staff_Menu(NhanVien):

    selected_docgia = {'MaDocGia': None, 'TenDocGia': None}
    so_sach_da_muon = 0

    def TraCuuDG():
        ma_dg = EntryMaDG.get()
        for DocGia in DocGia_List:
            if DocGia['MaDocGia'] == ma_dg:
                selected_docgia['MaDocGia'] = DocGia['MaDocGia']
                selected_docgia['TenDocGia'] = DocGia['TenDocGia']
                DocGia_Name.config(text=f"Họ tên độc giả: {DocGia['TenDocGia']}")
                so_sach_muon = 0
                for PhieuMuon in PhieuMuon_List:
                    if PhieuMuon['MaDocGia'] == ma_dg:
                        for ChiTietPM in ChiTietPM_List:
                            if ChiTietPM['MaPhieuMuon'] == PhieuMuon['MaPhieuMuon'] and ChiTietPM['TinhTrang'] == "Còn mượn":
                                so_sach_muon += 1
                nonlocal so_sach_da_muon
                so_sach_da_muon = so_sach_muon
                so_con_lai = 3 - so_sach_da_muon
                DocGia_Muon.config(text=f"Độc giả còn được mượn: {so_con_lai} quyển")
                return
        selected_docgia['MaDocGia'] = None
        selected_docgia['TenDocGia'] = None
        DocGia_Name.config(text="Họ tên độc giả: ")
        DocGia_Muon.config(text="Độc giả còn được mượn: ")
        messagebox.showinfo("Kết quả tra cứu", f"Không tìm thấy độc giả với mã: {ma_dg}")

    def chon_sach():
        if not selected_docgia['MaDocGia']:
            messagebox.showwarning("Chưa chọn độc giả", "Vui lòng tra cứu độc giả hợp lệ trước khi chọn sách.")
            return
        Sach_chon = listbox_sach.curselection()
        for Sach in Sach_chon:
            value = listbox_sach.get(Sach)
            ma_sach = value.split(" - ")[0]
            for i in range(listbox_chitiet.size()):
                if listbox_chitiet.get(i).startswith(ma_sach):
                    messagebox.showwarning("Trùng mã sách", "Không được chọn trùng mã sách trong phiếu mượn.")
                    return
            tong_sach = so_sach_da_muon + listbox_chitiet.size()
            if tong_sach >= 3:
                messagebox.showwarning("Vượt quá số lượng", "Độc giả không được mượn quá số lượng quy định.")
                return
            listbox_chitiet.insert(tk.END, value)
            so_con_lai = 3 - (so_sach_da_muon + listbox_chitiet.size())
            if so_con_lai < 0:
                so_con_lai = 0
            DocGia_Muon.config(text=f"Độc giả còn được mượn: {so_con_lai} quyển")

    def xuat_phieu_muon():
        if not selected_docgia['MaDocGia']:
            messagebox.showwarning("Chưa chọn độc giả", "Vui lòng tra cứu độc giả hợp lệ trước khi xuất phiếu mượn.")
            return
        if listbox_chitiet.size() == 0:
            messagebox.showwarning("Chưa chọn sách", "Vui lòng chọn ít nhất một sách để mượn.")
            return
        while True:
            ma_pm = "PM" + str(random.randint(100000, 999999))
            if not any(pm['MaPhieuMuon'] == ma_pm for pm in PhieuMuon_List):
                break
        Add_PhieuMuon(ma_pm,selected_docgia['MaDocGia'],NhanVien)
        try:
            with open("Phieumuon.json", "w", encoding="utf-8") as f:
                json.dump(PhieuMuon_List, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Lỗi ghi file", f"Lỗi ghi file Phieumuon.json: {e}")
            return
        for i in range(listbox_chitiet.size()):
            ma_sach = listbox_chitiet.get(i).split(" - ")[0]
            Add_ChiTietPM(ma_pm, ma_sach)
        try:
            with open("Chitietphieumuon.json", "w", encoding="utf-8") as f:
                json.dump(ChiTietPM_List, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Lỗi ghi file", f"Lỗi ghi file Chitietphieumuon.json: {e}")
            return
        messagebox.showinfo(
            "Phiếu mượn đã được xuất",
            f"Mã phiếu mượn: {ma_pm}\n"
            f"Tên + mã độc giả: {selected_docgia['TenDocGia']} ({selected_docgia['MaDocGia']})\n"
            f"Mã nhân viên: {NhanVien['MaNV']}\n"
            f"Ngày mượn: {datetime.today()}\n"
            f"Số sách mượn: {listbox_chitiet.size()}"
        )
        staff_root.destroy()

    staff_root = tk.Tk()
    staff_root.title("Quản lý phiếu mượn sách")
    staff_root.geometry("500x350")

    tk.Label(staff_root, text="Phiếu mượn sách", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=4)
    tk.Label(staff_root, text="Tên nhân viên đăng nhập:").grid(row=1, column=0)
    tk.Label(staff_root, text=NhanVien['ho_ten']).grid(row=1, column=1)

    tk.Label(staff_root, text="Mã đọc giả : ").grid(row=2, column=0, sticky="w")
    EntryMaDG = tk.Entry(staff_root)
    EntryMaDG.grid(row=2, column=1, sticky="w")
    tk.Button(staff_root, text="Tra cứu", command=TraCuuDG).grid(row=2, column=2, sticky="w")
    DocGia_Name = tk.Label(staff_root, text="Họ tên độc giả: ")
    DocGia_Name.grid(row=3, column=0, sticky="w", columnspan=2)
    DocGia_Muon = tk.Label(staff_root, text="Độc giả còn được mượn: ")
    DocGia_Muon.grid(row=4, column=0, sticky="w", columnspan=2)

    tk.Label(staff_root, text="Danh sách sách").grid(row=5, column=0)
    tk.Label(staff_root, text="Chi tiết mượn").grid(row=5, column=2)

    listbox_sach = tk.Listbox(staff_root, selectmode=tk.SINGLE, width=30, height=8)
    listbox_sach.grid(row=6, column=0, rowspan=4)

    listbox_chitiet = tk.Listbox(staff_root, width=30, height=8)
    listbox_chitiet.grid(row=6, column=2, rowspan=4)

    for sach in Sach_List:
        listbox_sach.insert(tk.END, f"{sach['MaSach']} - {sach['TenSach']}")

    Pick_Sach = tk.Button(staff_root, text="Chọn >>", command=chon_sach)
    Pick_Sach.grid(row=7, column=1)
    tk.Button(staff_root, text="Xuất phiếu mượn", command=xuat_phieu_muon).grid(row=11, column=0, columnspan=4)



root = tk.Tk()
root.title("Màn hình đăng nhập")
root.geometry("300x100")
Staff_List = load_Staff()
Sach_List = load_Sach()
PhieuMuon_List = load_PhieuMuon()
DocGia_List = load_DocGia()
ChiTietPM_List = load_ChiTietPM()
tk.Label(root, text="Đăng nhập").grid(row=0, column=0, columnspan=5)
tk.Label(root, text="Tên đăng nhập").grid(row=1, column=0)
EntryUser = tk.Entry(root)
EntryUser.grid(row=1, column=1, columnspan=4)
tk.Label(root, text="Mật khẩu").grid(row=2, column=0)
EntryPass = tk.Entry(root, show="*")
EntryPass.grid(row=2, column=1, columnspan=4)
tk.Button(root, text="Đăng nhập", command=Login).grid(row=3, column=0, columnspan=5)
root.mainloop()
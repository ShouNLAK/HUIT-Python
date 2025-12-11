import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

def tai_du_lieu():
    if os.path.exists("sinhvien.json"):
        with open("sinhvien.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def luu_du_lieu():
    with open("sinhvien.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    messagebox.showinfo("Đã lưu", "Dữ liệu đã được lưu.")

def xoa_bang():
    Tree.delete(*Tree.get_children())

def cap_nhat_bang(data_):
    xoa_bang()
    for SV in data_:
        Tree.insert("", "end", values=(SV.get("ma"), SV.get("ten"), SV.get("lop")))

def load_input():
    MS = EntryMS.get().strip()
    Ten = EntryTen.get().strip()
    Lop = EntryLop.get().strip()
    return MS, Ten, Lop

def TimSV():
    DS = []
    data_ = tai_du_lieu()
    Tim = EntrySV.get().strip()
    for SV in data_:
        if Tim.lower() in SV.get("ten", "").lower():
            DS.append(SV)
    cap_nhat_bang(DS if DS else data_)

def GetInfo(event):
    Chon = Tree.selection()
    if not Chon:
        return
    EntryMS.delete(0, tk.END)
    EntryTen.delete(0, tk.END)
    EntryLop.delete(0, tk.END)
    ma, ten, lop = Tree.item(Chon[0])["values"]
    EntryMS.insert(0, ma)
    EntryTen.insert(0, ten)
    EntryLop.insert(0, lop)

def Them():
    MS, Ten, Lop = load_input()
    if not (MS and Ten and Lop):
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
        return
    data_ = tai_du_lieu()
    for SV in data_:
        if SV.get("ma") == MS:
            return messagebox.showerror("Lỗi", "Trùng mã sinh viên")
    data_.append({"ma": MS, "ten": Ten, "lop": Lop})
    cap_nhat_bang(data_)
    global data
    data = data_

def Xoa():
    MS, _, _ = load_input()
    if not MS:
        messagebox.showerror("Lỗi", "Vui lòng nhập Mã SV để xóa.")
        return
    data_ = tai_du_lieu()
    new_data = [SV for SV in data_ if SV.get("ma") != MS]
    if len(new_data) == len(data_):
        messagebox.showerror("Lỗi", "Không tìm thấy sinh viên để xóa.")
        return
    cap_nhat_bang(new_data)
    global data
    data = new_data

def Sua():
    MS, Ten, Lop = load_input()
    if not (MS and Ten and Lop):
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
        return
    data_ = tai_du_lieu()
    found = False
    for SV in data_:
        if SV.get("ma") == MS:
            SV["ten"] = Ten
            SV["lop"] = Lop
            found = True
            break
    if not found:
        messagebox.showerror("Lỗi", f"Không tìm thấy sinh viên có Mã SV: {MS} để sửa.")
        return
    cap_nhat_bang(data_)
    global data
    data = data_

root = tk.Tk()
root.title("Tra cứu thông tin sinh viên")
root.geometry("800x400")

data = tai_du_lieu()

frm_top = tk.Frame(root)
frm_top.pack(fill="x", padx=10, pady=5)

tk.Label(frm_top, text="Họ tên sinh viên:").grid(row=0, column=0, sticky="w")
EntrySV = tk.Entry(frm_top, width=30)
EntrySV.grid(row=0, column=1, sticky="ew", padx=5)
tk.Button(frm_top, text="Tra cứu", width=12, command=TimSV).grid(row=0, column=2, padx=5)

frm_info = tk.LabelFrame(root, text="Thông tin bạn đang chọn", padx=10, pady=10)
frm_info.pack(fill="x", padx=10, pady=5)

tk.Label(frm_info, text="Mã SV:").grid(row=0, column=0, sticky="w")
EntryMS = tk.Entry(frm_info, width=15)
EntryMS.grid(row=0, column=1, sticky="ew", padx=5)
tk.Label(frm_info, text="Tên SV:").grid(row=0, column=2, sticky="w")
EntryTen = tk.Entry(frm_info, width=25)
EntryTen.grid(row=0, column=3, sticky="ew", padx=5)
tk.Label(frm_info, text="Lớp:").grid(row=0, column=4, sticky="w")
EntryLop = tk.Entry(frm_info, width=15)
EntryLop.grid(row=0, column=5, sticky="ew", padx=5)

frm_btn = tk.Frame(root)
frm_btn.pack(fill="x", padx=10, pady=5)
tk.Button(frm_btn, text="Thêm", width=12, command=Them).pack(side="left", padx=5)
tk.Button(frm_btn, text="Sửa", width=12, command=Sua).pack(side="left", padx=5)
tk.Button(frm_btn, text="Xóa", width=12, command=Xoa).pack(side="left", padx=5)
tk.Button(frm_btn, text="Lưu", width=12, command=luu_du_lieu).pack(side="left", padx=5)

frm_tree = tk.LabelFrame(root, text="Danh sách sinh viên", padx=10, pady=10)
frm_tree.pack(fill="both", expand=True, padx=10, pady=5)

Tree = ttk.Treeview(frm_tree, columns=("ma", "ten", "lop"), show="headings", height=10)
Tree.heading("ma", text="Mã SV")
Tree.heading("ten", text="Tên SV")
Tree.heading("lop", text="Lớp")
Tree.column("ma", width=100, anchor="center")
Tree.column("ten", width=250, anchor="w")
Tree.column("lop", width=100, anchor="center")
Tree.pack(fill="both", expand=True)
Tree.bind("<<TreeviewSelect>>", GetInfo)

cap_nhat_bang(data)
root.mainloop()
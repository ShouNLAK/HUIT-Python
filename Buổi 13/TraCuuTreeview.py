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
    
def cap_nhat_bang(data):
    xoa_bang()
    for SV in data :
        Tree.insert("", "end", values=(SV.get("ma"), SV.get("ten"),SV.get("lop")))
        
def load_input():
    MS = EntryMS.get()
    Ten = EntryTen.get()
    Lop = EntryLop.get()
    return MS,Ten,Lop

def TimSV():
    DS = []
    data = tai_du_lieu()
    for item in Tree.get_children():
        Tree.delete(item)
    Tim = EntrySV.get().strip()
    for SV in data :
        if Tim in SV.get("ten"):
            DS.append(SV)
    if DS:
        for SV in DS :
            Tree.insert("", "end", values=(SV.get("ma"), SV.get("ten"),SV.get("lop")))
    else:
        Tree.insert(data)
            
def GetInfo(event):
    Chon = Tree.selection()
    if not Chon:
        return

    EntryMS.delete(0,tk.END)
    EntryTen.delete(0,tk.END)
    EntryLop.delete(0,tk.END)
    
    ma,ten,lop = Tree.item(Chon[0])["values"]
    
    EntryMS.insert(0,ma)
    EntryTen.insert(0,ten)
    EntryLop.insert(0,lop)
    
def Them():
    MS,Ten,Lop = load_input()
    if not (MS and Ten and Lop):
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin (Mã SV) để sửa.")
        return
    data = tai_du_lieu()
    for SV in data :
        if SV.get("ma") == MS :
            return messagebox.showerror("Lỗi","Trùng mã sinh viên")
    data.append({"ma": MS, "ten": Ten, "lop": Lop})
    cap_nhat_bang(data)

def Xoa():
    MS,Ten,Lop = load_input()
    if not (MS):
        messagebox.showerror("Lỗi", "Vui lòng nhập thông tin (Mã SV) để sửa.")
        return
    data = tai_du_lieu()
    new_data = [SV for SV in data if SV.get("ma") != MS]
    data = new_data
    cap_nhat_bang(new_data)
    
def Sua():
    MS, Ten, Lop = load_input()
    if not (MS and Ten and Lop):
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin (Mã SV) để sửa.")
        return
    data = tai_du_lieu()
    found = False
    for SV in data:
        if SV.get("ma") == MS:
            SV["ten"] = Ten
            SV["lop"] = Lop
            found = True
        if SV.get("ten") == Ten and SV.get("lop") == Lop:
            found = True
            SV["ma"] = MS
    if not found:
        messagebox.showerror("Lỗi", f"Không tìm thấy sinh viên có Mã SV: {MS} để sửa.")
        return
    cap_nhat_bang(data)
    

root = tk.Tk()
root.title("Tra cứu thông tin sinh viên")
root.geometry("1000x500")

data = tai_du_lieu()

tk.Label(root,text="Họ tên sinh viên : ").grid(row=0, column = 0, sticky="w")
EntrySV = tk.Entry()
EntrySV.grid(row = 0, column = 1, sticky="w")
tk.Button(root,text="Tra cứu",command=TimSV).grid(row=0,column =2)

tk.Label(root,text="Thông tin bạn đang chọn :").grid(row=1, column = 0, sticky="w")

tk.Label(root,text="Mã SV :").grid(row=2,column=0,sticky="w")
EntryMS = tk.Entry()
EntryMS.grid(row=2,column=1,sticky="w")
tk.Label(root,text="Tên SV :").grid(row=2,column=2,sticky="w")
EntryTen = tk.Entry()
EntryTen.grid(row=2,column=3,sticky="w")
tk.Label(root,text="Lớp :").grid(row=2,column=4,sticky="w")
EntryLop = tk.Entry()
EntryLop.grid(row=2,column=5,sticky="w")

tk.Button(root, text="Thêm", width=10, command=Them).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Sửa", width=10, command=Sua).grid(row=3, column=3, padx=5, pady=5)
tk.Button(root, text="Xóa", width=10, command=Xoa).grid(row=3, column=5, padx=5, pady=5)
tk.Button(root, text="Lưu", width=10, command=luu_du_lieu).grid(row=3, column=0, padx=5, pady=5)

tk.Label(root, text="Danh sách sinh viên :").grid(row=4, column=0, sticky="w", padx=5, pady=5)

tk.Label(root,text="Danh sách sinh viên :").grid(row=5,column=0,sticky="w")
Tree = ttk.Treeview(root,columns=("ma","ten","lop"),show = "headings")
Tree.heading("ma",text="Mã SV")
Tree.heading("ten",text="Tên SV")
Tree.heading("lop",text="Lớp")
Tree.grid(row=6,column=0,columnspan=2)
Tree.bind("<<TreeviewSelect>>",GetInfo)

root.mainloop()
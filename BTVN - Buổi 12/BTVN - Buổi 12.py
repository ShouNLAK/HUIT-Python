import tkinter as tk
from tkinter import messagebox,ttk
import json


def traCuuMaKH():
    ma_kh = EntryMaKH.get()
    
    try:
        with open("DanhsachKH.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file DanhsachKH.json")
        return
    
    khach_hang = []
    for kh in data:
        if kh.get("ma_khach_hang") == ma_kh:
            khach_hang.append(kh)

    for item in tree.get_children():
        tree.delete(item)
    
    if khach_hang:
        so_nguoi = len(khach_hang)
        dinh_muc = so_nguoi * 4
        soNguoi_label.config(text=f"Số người trong hộ: {so_nguoi}")
        dinhMuc_label.config(text=f"Định mức nước (m3): {dinh_muc}")
        for nguoi in khach_hang:
            tree.insert("", "end", values=(nguoi.get("ma_dinh_danh", ""), nguoi.get("ho_ten", "")))
    else:
        messagebox.showinfo("Thông báo", f"Không tìm thấy khách hàng với mã: {ma_kh}")
        soNguoi_label.config(text="Số người trong hộ: ")
        dinhMuc_label.config(text="Định mức nước (m3): ")

root = tk.Tk()
root.title("Tra cứu định mức nước")
root.geometry("600x480")

tk.Label(root,text="Nhập mã khách hàng: ").grid(row=0,column=0,padx=10,pady=10)
EntryMaKH = tk.Entry(root)
EntryMaKH.grid(row=0,column=1)
tk.Button(root,text="Tra cứu",command = traCuuMaKH).grid(row=0,column=2)

soNguoi_label = tk.Label(root,text="Số người trong hộ: ")
soNguoi_label.grid(row=1,column=0,padx=10,pady=10,columnspan=2,sticky="w")
dinhMuc_label = tk.Label(root,text="Định mức nước (m3): ")
dinhMuc_label.grid(row=2,column=0,padx=10,pady=10,columnspan=2,sticky="w")

tk.Label(root,text="Danh sách người trong hộ:").grid(row=3,column=0,padx=10,pady=10,columnspan=2,sticky="w")
tree = ttk.Treeview(root, columns=("ma_dd", "ho_ten"), show="headings")
tree.heading("ma_dd", text="Mã Định danh")
tree.heading("ho_ten", text="Họ tên")
tree.grid(row=4,column=0,padx=10,pady=10,columnspan=2)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
    

def Input_Enough_Info(MS,Name,DT,Email):
    if (MS == None or Name == None or DT == None or Email == None):
        return False
    return True
    
def Check_Phone_Format(DT):
    if len(DT) != 10 :
        return False
    return True
    
def Check_Email_Format(Email) :
    if "@" in Email :
        if ".com" in Email :
            return True

def Check_Info():
    MSSV = EntryMSSV.get()
    Name = EntryName.get()
    SDT = EntrySDT.get()
    Email = EntryEmail.get()
    Class = EntryClass.get()
    
    if not (Input_Enough_Info(MSSV,Name,SDT,Email)):
        messagebox.showerror("Lỗi", "Bạn cần phải nhập đủ 4 trường thông tin")
        return
    if not (Check_Phone_Format(SDT)) :
        messagebox.showerror("Lỗi", "Số điện thoại phải đủ 10 chữ số")
        return
    if not (Check_Email_Format(Email)) :
        messagebox.showerror("Lỗi", "Định dạng Email phải abc@domain.com")
        return
    tree.insert("", "end", values=(MSSV, Name, Email,SDT,Class))
    messagebox.showinfo("Thành công","Đã thêm sinh viên vào danh sách")
    
    
root = tk.Tk()
root.title("Thông tin sinh viên")
root.geometry("1000x1000")

tk.Label(root,text="Mã số sinh viên : ").grid(row=0,column=0,padx=10,pady=10)
EntryMSSV = tk.Entry(root)
EntryMSSV.grid(row=0,column=1,padx=10,pady=10)

tk.Label(root,text="Họ và tên : ").grid(row=1,column=0,padx=10,pady=10)
EntryName = tk.Entry(root)
EntryName.grid(row=1,column=1,padx=10,pady=10)

tk.Label(root,text="Số điện thoại : ").grid(row=2,column=0,padx=10,pady=10)
EntrySDT = tk.Entry(root)
EntrySDT.grid(row=2,column=1,padx=10,pady=10)

tk.Label(root,text="Email : ").grid(row=3,column=0,padx=10,pady=10)
EntryEmail = tk.Entry(root)
EntryEmail.grid(row=3,column=1,padx=10,pady=10)

tk.Label(root,text="Lớp : ").grid(row=4,column=0,padx=10,pady=10)
EntryClass = tk.Entry(root)
EntryClass.grid(row=4,column=1,padx=10,pady=10)

tk.Button(root,text="Thêm sinh viên",command=Check_Info).grid(row=5,column=0,padx = 10,pady=10,columnspan=2)

tree = ttk.Treeview(root, columns=("ma_sv", "ho_ten", "email","so_dien_thoai"), show="headings")
tree.heading("ma_sv", text="Mã SV")
tree.heading("ho_ten", text="Họ tên")
tree.heading("email", text="Email")
tree.heading("so_dien_thoai", text="Số điện thoại")
tree.grid(row=6,column=0,padx=10,pady=10,columnspan=2)
try:
    with open("sinh_vien.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for sv in data:
            tree.insert("", "end", values=(sv["ma_sv"], sv["ho_ten"], sv["email"],sv["so_dien_thoai"]))
except FileNotFoundError:
    print("⚠️ Không tìm thấy file JSON! Vui lòng chắc chắn file đã đúng tên và nằm cùng thư mục với chương trình.")
    
chon_lop = ttk.Combobox(root, state="readonly")
chon_lop.grid(row=7,column=0,padx=10,pady=10,columnspan=2)

try:
    with open("sinh_vien.json", "r", encoding="utf-8") as f:
        DSSV = json.load(f)
        chon_lop["values"] = sorted(list(set([SV["lop"] for SV in DSSV])))
except FileNotFoundError:
    print("⚠️ Không tìm thấy file JSON! Vui lòng chắc chắn file đã đúng tên và nằm cùng thư mục với chương trình!")

root.mainloop()
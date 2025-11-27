import tkinter as tk
from tkinter import messagebox

def Tong() :
    try:
        so_1 = float(Entry1.get())
        so_2 = float(Entry2.get())
        tong = so_1 + so_2
        result_label.config(text=f"Kết quả = {tong}")
    except ValueError:
        messagebox.showerror("Lỗi","Vui lòng nhập số hợp lệ")
    
root = tk.Tk()
root.title("Cộng hai số")
root.geometry("300x200")

tk.Label(root,text="Số thứ nhất").pack()
Entry1=tk.Entry(root)
Entry1.pack()

tk.Label(root,text="Số thứ hai").pack()
Entry2=tk.Entry(root)
Entry2.pack()

tk.Button(root,text="Cộng",command=Tong).pack()

result_label = tk.Label(root,text="Kết quả = ")
result_label.pack()

root.mainloop()